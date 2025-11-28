import os
import logging
import tempfile
from pathlib import Path
from typing import Dict, Any

import requests
from flask import Flask, request, jsonify

from app.config_seguro import ConfigSeguro as Config
from app.printer import print_file

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

Config.ensure_temp_dir()


def validate_token(token: str) -> bool:
    return Config.validate_token(token)


def validate_url(url: str) -> bool:
    return Config.validate_url(url)


@app.before_request
def validate_request():
    if request.path == '/health':
        return None
    
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.replace('Bearer ', '').strip()
    
    if not token:
        logger.warning(f"Intento de acceso sin token desde {request.remote_addr}")
        return jsonify({
            "status": "error",
            "message": "Token de autenticación requerido"
        }), 401
    
    if not validate_token(token):
        logger.warning(f"Intento de acceso con token inválido desde {request.remote_addr}")
        return jsonify({
            "status": "error",
            "message": "Token de autenticación inválido"
        }), 401
    
    return None


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Agente de impresión local está funcionando"
    })


@app.route('/print', methods=['POST'])
def print_document():
    try:
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "El contenido debe ser JSON"
            }), 400
        
        data: Dict[str, Any] = request.get_json()
        document_url = data.get("document_url")
        if not document_url:
            return jsonify({
                "status": "error",
                "message": "El campo 'document_url' es requerido"
            }), 400
        
        if not isinstance(document_url, str) or not document_url.startswith(("http://", "https://")):
            return jsonify({
                "status": "error",
                "message": "El campo 'document_url' debe ser una URL válida (http:// o https://)"
            }), 400
        
        if not validate_url(document_url):
            logger.warning(f"Intento de imprimir URL no permitida: {document_url} desde {request.remote_addr}")
            return jsonify({
                "status": "error",
                "message": "URL no permitida. Solo se permiten URLs de dominios autorizados."
            }), 403
        
        logger.info(f"Orden de impresión recibida desde {request.remote_addr}: {document_url}")
        file_path = _download_file(document_url)
        if not file_path:
            return jsonify({
                "status": "error",
                "message": "Error al descargar el archivo desde la URL proporcionada"
            }), 500
        
        logger.info(f"Archivo descargado exitosamente: {file_path}")
        success, message = print_file(file_path)
        
        try:
            os.remove(file_path)
            logger.info(f"Archivo temporal eliminado: {file_path}")
        except Exception as e:
            logger.warning(f"No se pudo eliminar el archivo temporal {file_path}: {e}")
        
        if success:
            return jsonify({
                "status": "ok",
                "message": message
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": message
            }), 500
            
    except Exception as e:
        logger.error(f"Error inesperado en /print: {e}", exc_info=True)
        return jsonify({
            "status": "error",
            "message": f"Error interno del servidor: {str(e)}"
        }), 500


def _download_file(url: str) -> str:
    try:
        logger.info(f"Descargando archivo desde: {url}")
        response = requests.get(
            url,
            timeout=Config.DOWNLOAD_TIMEOUT,
            stream=True,
            headers={
                "User-Agent": "PrintAgent/1.0"
            }
        )
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").lower()
        url_lower = url.lower()
        file_ext = ".pdf"
        if ".pdf" in content_type or url_lower.endswith(".pdf"):
            file_ext = ".pdf"
        elif "html" in content_type or url_lower.endswith((".html", ".htm")):
            file_ext = ".html"
        elif "image" in content_type or url_lower.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            if url_lower.endswith(".jpg") or url_lower.endswith(".jpeg"):
                file_ext = ".jpg"
            elif url_lower.endswith(".png"):
                file_ext = ".png"
            elif url_lower.endswith(".gif"):
                file_ext = ".gif"
            elif url_lower.endswith(".bmp"):
                file_ext = ".bmp"
            else:
                file_ext = ".jpg"
        elif url_lower.endswith(".txt"):
            file_ext = ".txt"
        elif url_lower.endswith((".doc", ".docx")):
            file_ext = ".docx" if url_lower.endswith(".docx") else ".doc"
        
        logger.info(f"Tipo de archivo detectado: {content_type}, extensión: {file_ext}")
        content_length = response.headers.get("Content-Length")
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            if size_mb > Config.MAX_FILE_SIZE_MB:
                raise ValueError(f"El archivo es demasiado grande ({size_mb:.2f} MB). Máximo: {Config.MAX_FILE_SIZE_MB} MB")
        
        temp_file = tempfile.NamedTemporaryFile(
            dir=Config.TEMP_DIR,
            suffix=file_ext,
            delete=False
        )
        temp_path = temp_file.name
        temp_file.close()
        total_size = 0
        with open(temp_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    total_size += len(chunk)
                    if total_size > Config.MAX_FILE_SIZE_MB * 1024 * 1024:
                        os.remove(temp_path)
                        raise ValueError(f"El archivo excede el tamaño máximo permitido ({Config.MAX_FILE_SIZE_MB} MB)")
        
        logger.info(f"Archivo descargado exitosamente: {temp_path} ({total_size / 1024:.2f} KB)")
        return temp_path
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error al descargar archivo: {e}")
        return None
    except Exception as e:
        logger.error(f"Error inesperado al descargar archivo: {e}", exc_info=True)
        return None


def main():
    logger.info("=" * 50)
    logger.info("Agente de Impresión Local")
    logger.info("=" * 50)
    logger.info(f"Servidor: {Config.HOST}:{Config.PORT}")
    logger.info(f"Directorio temporal: {Config.TEMP_DIR}")
    
    if Config.PRINT_TOKEN == "cambiar-este-token-en-produccion-12345":
        logger.warning("⚠️  ADVERTENCIA: Usando token por defecto. Cambiar en producción!")
    
    if not Config.ALLOWED_DOMAINS:
        logger.warning("⚠️  ADVERTENCIA: No hay whitelist de dominios. Se permiten todas las URLs.")
    
    logger.info("=" * 50)
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=False
    )


if __name__ == "__main__":
    main()

