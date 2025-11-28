# Guía de Instalación - Agente de Impresión Local

## Para Usuarios de Windows

### Paso 1: Descargar el Agente
1. Ve a: https://github.com/Kevin-HBA/print-agent/releases/tag/v1.0.0
2. En la sección "Assets", descarga el archivo **`print_agent.exe`**
3. Guarda el archivo en una carpeta fácil de encontrar (por ejemplo: `C:\PrintAgent\`)

### Paso 2: Ejecutar el Agente
1. Haz doble clic en `print_agent.exe`
2. Se abrirá una ventana negra (no la cierres, debe permanecer abierta)
3. Verás un mensaje que dice: "Agente de impresión local está funcionando"
4. **IMPORTANTE:** Deja esta ventana abierta mientras uses el sistema

### Paso 3: Instalar la Extensión del Navegador
1. En la misma página de Releases, descarga el archivo **`extension.zip`**
2. Descomprime el archivo `extension.zip` en una carpeta (por ejemplo: `C:\PrintAgent\extension\`)
3. Abre Google Chrome o Microsoft Edge
4. Ve a: `chrome://extensions/` (o `edge://extensions/` en Edge)
5. Activa el "Modo de desarrollador" (toggle en la esquina superior derecha)
6. Haz clic en "Cargar extensión sin empaquetar"
7. Selecciona la carpeta `extension` que descomprimiste
8. La extensión aparecerá instalada

### Paso 4: Verificar que Funciona
1. Abre cualquier página web con un PDF o documento
2. Haz clic en un enlace de PDF o botón de imprimir
3. El documento debería imprimirse automáticamente en tu impresora predeterminada

---

## Para Usuarios de macOS

### Paso 1: Descargar el Agente
1. Ve a: https://github.com/Kevin-HBA/print-agent/releases/tag/v1.0.0
2. En la sección "Assets", descarga el archivo **`print_agent`**
3. Guarda el archivo en una carpeta fácil de encontrar (por ejemplo: `~/PrintAgent/`)

### Paso 2: Dar Permisos de Ejecución
1. Abre la Terminal (Aplicaciones > Utilidades > Terminal)
2. Ejecuta estos comandos:
   ```bash
   cd ~/PrintAgent
   chmod +x print_agent
   ```

### Paso 3: Ejecutar el Agente
1. En la Terminal, ejecuta:
   ```bash
   ./print_agent
   ```
2. Verás mensajes que indican que el agente está funcionando
3. **IMPORTANTE:** Deja la Terminal abierta mientras uses el sistema

### Paso 4: Instalar la Extensión del Navegador
1. En la misma página de Releases, descarga el archivo **`extension.zip`**
2. Descomprime el archivo `extension.zip` en una carpeta (por ejemplo: `~/PrintAgent/extension/`)
3. Abre Google Chrome o Microsoft Edge
4. Ve a: `chrome://extensions/` (o `edge://extensions/` en Edge)
5. Activa el "Modo de desarrollador" (toggle en la esquina superior derecha)
6. Haz clic en "Cargar extensión sin empaquetar"
7. Selecciona la carpeta `extension` que descomprimiste
8. La extensión aparecerá instalada

### Paso 5: Verificar que Funciona
1. Abre cualquier página web con un PDF o documento
2. Haz clic en un enlace de PDF o botón de imprimir
3. El documento debería imprimirse automáticamente en tu impresora predeterminada

---

## Configurar Auto-Inicio (Opcional)

### Windows
1. Presiona `Win + R`
2. Escribe: `shell:startup` y presiona Enter
3. Crea un acceso directo de `print_agent.exe` en esa carpeta
4. El agente se iniciará automáticamente al encender la computadora

### macOS
1. Abre "Preferencias del Sistema" > "Usuarios y Grupos" > "Elementos de inicio de sesión"
2. Haz clic en el botón "+"
3. Selecciona el archivo `print_agent`
4. El agente se iniciará automáticamente al iniciar sesión

---

## Solución de Problemas

### El agente no inicia
- Verifica que tengas Python instalado (aunque el .exe no debería necesitarlo)
- En Windows, ejecuta como Administrador si es necesario
- Verifica que el puerto 8765 no esté en uso por otra aplicación

### La extensión no funciona
- Verifica que el agente esté ejecutándose (debe estar la ventana/terminal abierta)
- Recarga la página web después de instalar la extensión
- Verifica que la extensión esté activada en `chrome://extensions/`

### No imprime
- Verifica que tengas una impresora configurada como predeterminada
- Verifica que el agente esté ejecutándose
- Revisa los mensajes en la ventana/terminal del agente

---

## Soporte

Si tienes problemas, verifica:
- Que el agente esté ejecutándose
- Que la extensión esté instalada y activada
- Que tengas una impresora configurada

Para más información, visita: https://github.com/Kevin-HBA/print-agent

