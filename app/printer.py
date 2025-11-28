import os
import platform
import subprocess
import logging
import time
from pathlib import Path
from typing import Tuple

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = {
    '.pdf': 'PDF',
    '.html': 'HTML',
    '.htm': 'HTML',
    '.jpg': 'Imagen',
    '.jpeg': 'Imagen',
    '.png': 'Imagen',
    '.gif': 'Imagen',
    '.bmp': 'Imagen',
    '.txt': 'Texto',
    '.doc': 'Documento',
    '.docx': 'Documento',
}


def print_file(file_path: str) -> Tuple[bool, str]:
    if not os.path.exists(file_path):
        return False, f"El archivo no existe: {file_path}"
    
    file_ext = Path(file_path).suffix.lower()
    if file_ext not in SUPPORTED_FORMATS:
        logger.warning(f"Formato de archivo no reconocido: {file_ext}. Intentando imprimir de todas formas.")
    
    system = platform.system()
    
    try:
        if system == "Windows":
            return _print_windows(file_path, file_ext)
        elif system == "Darwin":
            return _print_macos(file_path, file_ext)
        else:
            return False, f"Sistema operativo no soportado: {system}"
    except Exception as e:
        logger.error(f"Error al imprimir archivo: {e}", exc_info=True)
        return False, f"Error al imprimir: {str(e)}"


def print_pdf(pdf_path: str) -> Tuple[bool, str]:
    return print_file(pdf_path)


def _print_windows(file_path: str, file_ext: str) -> Tuple[bool, str]:
    try:
        ps_command = f'''
        $file = "{file_path}"
        $printer = Get-WmiObject -Class Win32_Printer | Where-Object {{$_.Default -eq $true}} | Select-Object -First 1
        if ($printer) {{
            Start-Process -FilePath $file -Verb Print -WindowStyle Hidden -NoNewWindow -ErrorAction SilentlyContinue
        }} else {{
            Write-Error "No se encontró impresora predeterminada"
        }}
        '''
        
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_command],
            capture_output=True,
            text=True,
            timeout=15,
            creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
        )
        
        if result.returncode == 0:
            return True, "Archivo enviado a la impresora predeterminada"
        
        if file_ext in ['.html', '.htm']:
            try:
                result2 = subprocess.run(
                    ["rundll32.exe", "mshtml.dll", "PrintHTML", f'"{file_path}"'],
                    capture_output=True,
                    text=True,
                    timeout=15,
                    creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
                )
                if result2.returncode == 0:
                    return True, "Archivo HTML enviado a la impresora predeterminada"
            except Exception:
                pass
        
        try:
            subprocess.Popen(
                ["cmd", "/c", "start", "/min", "", file_path],
                shell=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
            )
            time.sleep(1)
            os.startfile(file_path, "print")
            return True, "Archivo enviado a la impresora predeterminada"
        except Exception as e:
            return False, f"Error al imprimir en Windows: {result.stderr or str(e)}"
                
    except subprocess.TimeoutExpired:
        return False, "Timeout al intentar imprimir"
    except Exception as e:
        try:
            os.startfile(file_path, "print")
            return True, "Archivo enviado a la impresora predeterminada (método alternativo)"
        except Exception as fallback_error:
            return False, f"Error al imprimir: {str(fallback_error)}"


def _print_macos(file_path: str, file_ext: str) -> Tuple[bool, str]:
    try:
        if file_ext in ['.html', '.htm']:
            try:
                result = subprocess.run(
                    ["cupsfilter", "-o", "fit-to-page", file_path],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                if result.returncode == 0:
                    return True, "Archivo HTML enviado a la impresora predeterminada"
            except FileNotFoundError:
                pass
            
            try:
                rtf_path = file_path.replace('.html', '.rtf').replace('.htm', '.rtf')
                subprocess.run(
                    ["textutil", "-convert", "rtf", "-output", rtf_path, file_path],
                    capture_output=True,
                    timeout=15
                )
                if os.path.exists(rtf_path):
                    result = subprocess.run(
                        ["lp", "-o", "silent", rtf_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                try:
                    os.remove(rtf_path)
                except:
                    pass
                if result.returncode == 0:
                        return True, "Archivo HTML enviado a la impresora predeterminada"
            except Exception:
                pass
        
        result = subprocess.run(
            ["lp", "-o", "silent", "-o", "fit-to-page", file_path],
            capture_output=True,
            text=True,
            timeout=15
        )
        
        if result.returncode == 0:
            return True, "Archivo enviado a la impresora predeterminada"
        else:
            result2 = subprocess.run(
                ["lp", file_path],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result2.returncode == 0:
                return True, "Archivo enviado a la impresora predeterminada"
            else:
                return False, f"Error al imprimir: {result2.stderr or 'Error desconocido'}"
                
    except subprocess.TimeoutExpired:
        return False, "Timeout al intentar imprimir"
    except FileNotFoundError:
        return False, "El comando 'lp' no está disponible en el sistema"
    except Exception as e:
        return False, f"Error al imprimir en macOS: {str(e)}"

