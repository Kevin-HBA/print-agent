# Agente de Impresión Local

Servidor HTTP local que permite imprimir documentos desde aplicaciones web de forma silenciosa.

## Características

- ✅ Funciona en Windows y macOS
- ✅ Impresión silenciosa sin ventanas de confirmación
- ✅ Soporta PDF, HTML, imágenes y más formatos
- ✅ Autenticación con token
- ✅ Whitelist de URLs permitidas
- ✅ Extensión del navegador para uso automático

## Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar seguridad

Editar `app/config_seguro.py`:

```python
# Cambiar token por defecto
PRINT_TOKEN = "tu-token-secreto-aqui"

# Agregar dominios permitidos
ALLOWED_DOMAINS = [
    'erp.empresa.com',
    'documentos.empresa.com'
]
```

### 3. Ejecutar

```bash
python -m app.server
```

## Generar Ejecutable

### Windows

```bash
pip install pyinstaller
pyinstaller --onefile --name print_agent --console app/server.py
```

El ejecutable estará en `dist/print_agent.exe`

## Uso

### Opción 1: Con Extensión del Navegador (Recomendado)

1. Usuario instala `print_agent.exe`
2. Usuario instala extensión desde `extension/`
3. En tus proyectos, usar atributo `data-print`:

```html
<a href="https://ejemplo.com/documento.pdf" data-print>Imprimir</a>
```

### Opción 2: JavaScript Directo

```javascript
fetch('http://localhost:8765/print', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer tu-token-secreto'
    },
    body: JSON.stringify({
        document_url: 'https://ejemplo.com/documento.pdf'
    })
});
```

## Estructura

```
.
├── app/
│   ├── server.py          # Servidor principal
│   ├── printer.py         # Lógica de impresión
│   ├── config_seguro.py    # Configuración segura
│   └── config.py           # Configuración básica (legacy)
├── extension/              # Extensión del navegador
├── requirements.txt
└── README.md
```

## Seguridad

- Token de autenticación requerido
- Whitelist de dominios permitidos
- Solo escucha en localhost
- Rate limiting básico

Ver `SEGURIDAD.md` para más detalles.

## Documentación

- `SEGURIDAD.md` - Análisis de seguridad completo
- `extension/` - Extensión del navegador

## Licencia

Uso interno. Verificar políticas de la empresa.
