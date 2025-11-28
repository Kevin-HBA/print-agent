# 📋 Guía de Instalación - Paso a Paso

## 🎯 Resumen Rápido

Cada usuario necesita hacer **2 cosas**:
1. **Instalar el Agente** (se ejecuta en segundo plano, invisible)
2. **Instalar la Extensión del Navegador** (una sola vez)

---

## 💻 Para Usuarios de WINDOWS

### PASO 1: Descargar Archivos

1. Ve a: **https://github.com/Kevin-HBA/print-agent/releases/tag/v1.0.0**
2. Descarga estos 2 archivos:
   - `print_agent.exe` (el agente)
   - `extension.zip` (la extensión)

### PASO 2: Instalar el Agente (Se ejecuta en segundo plano)

**Opción A: Instalación Manual (Recomendada)**

1. Crea una carpeta: `C:\PrintAgent\`
2. Mueve `print_agent.exe` a esa carpeta
3. Presiona `Win + R` (tecla Windows + R)
4. Escribe: `shell:startup` y presiona Enter
5. Crea un acceso directo de `print_agent.exe` en esa carpeta de inicio
6. Ejecuta el acceso directo una vez para iniciar el agente ahora
7. **Listo:** El agente se ejecutará automáticamente cada vez que enciendas la computadora

**Opción B: Ejecutar Manualmente (Cada vez que enciendas la PC)**

1. Haz doble clic en `print_agent.exe`
2. Se abrirá una ventana negra pequeña
3. **NO CIERRES ESA VENTANA** - debe permanecer abierta
4. Minimízala si quieres, pero no la cierres

### PASO 3: Instalar la Extensión del Navegador

1. Descomprime `extension.zip` en una carpeta (ejemplo: `C:\PrintAgent\extension\`)
2. Abre **Google Chrome** o **Microsoft Edge**
3. Ve a: `chrome://extensions/` (o `edge://extensions/` en Edge)
4. Activa el **"Modo de desarrollador"** (toggle en la esquina superior derecha)
5. Haz clic en **"Cargar extensión sin empaquetar"**
6. Selecciona la carpeta `extension` que descomprimiste
7. **Listo:** La extensión quedará instalada

### PASO 4: Verificar que Funciona

1. Abre cualquier página web (tu ERP, sistema, etc.)
2. Haz clic en un PDF o botón de imprimir
3. El documento se imprimirá automáticamente en tu impresora predeterminada
4. **No aparecerá ninguna ventana de confirmación**

---

## 🍎 Para Usuarios de macOS

### PASO 1: Descargar Archivos

1. Ve a: **https://github.com/Kevin-HBA/print-agent/releases/tag/v1.0.0**
2. Descarga estos 2 archivos:
   - `print_agent` (el agente)
   - `extension.zip` (la extensión)

### PASO 2: Instalar el Agente (Se ejecuta en segundo plano)

**Opción A: Auto-Inicio (Recomendada)**

1. Crea una carpeta: `~/PrintAgent/`
2. Mueve `print_agent` a esa carpeta
3. Abre la **Terminal** (Aplicaciones > Utilidades > Terminal)
4. Ejecuta estos comandos:
   ```bash
   cd ~/PrintAgent
   chmod +x print_agent
   ```
5. Abre: **"Preferencias del Sistema"** > **"Usuarios y Grupos"** > **"Elementos de inicio de sesión"**
6. Haz clic en el botón **"+"**
7. Selecciona el archivo `print_agent`
8. Ejecuta `./print_agent` una vez en la Terminal para iniciarlo ahora
9. **Listo:** El agente se ejecutará automáticamente cada vez que inicies sesión

**Opción B: Ejecutar Manualmente (Cada vez que enciendas la Mac)**

1. Abre la **Terminal**
2. Ejecuta:
   ```bash
   cd ~/PrintAgent
   chmod +x print_agent
   ./print_agent
   ```
3. **NO CIERRES LA TERMINAL** - debe permanecer abierta
4. Minimízala si quieres, pero no la cierres

### PASO 3: Instalar la Extensión del Navegador

1. Descomprime `extension.zip` en una carpeta (ejemplo: `~/PrintAgent/extension/`)
2. Abre **Google Chrome** o **Microsoft Edge**
3. Ve a: `chrome://extensions/` (o `edge://extensions/` en Edge)
4. Activa el **"Modo de desarrollador"** (toggle en la esquina superior derecha)
5. Haz clic en **"Cargar extensión sin empaquetar"**
6. Selecciona la carpeta `extension` que descomprimiste
7. **Listo:** La extensión quedará instalada

### PASO 4: Verificar que Funciona

1. Abre cualquier página web (tu ERP, sistema, etc.)
2. Haz clic en un PDF o botón de imprimir
3. El documento se imprimirá automáticamente en tu impresora predeterminada
4. **No aparecerá ninguna ventana de confirmación**

---

## ⚠️ Puntos Importantes

### ✅ Lo que SÍ debes hacer:
- Instalar el agente UNA VEZ (configurar auto-inicio)
- Instalar la extensión UNA VESA
- Dejar el agente ejecutándose (si usas opción manual, no cerrar la ventana/terminal)

### ❌ Lo que NO debes hacer:
- Cerrar la ventana/terminal del agente (si usas opción manual)
- Desinstalar la extensión
- Mover o eliminar los archivos después de instalarlos

---

## 🔧 Solución de Problemas

### "No imprime"
1. Verifica que el agente esté ejecutándose:
   - **Windows:** Busca `print_agent.exe` en el Administrador de tareas
   - **macOS:** Ejecuta `ps aux | grep print_agent` en Terminal
2. Verifica que la extensión esté instalada y activada en `chrome://extensions/`
3. Verifica que tengas una impresora configurada como predeterminada

### "El agente no inicia"
- **Windows:** Ejecuta `print_agent.exe` como Administrador (clic derecho > Ejecutar como administrador)
- **macOS:** Verifica los permisos: `chmod +x print_agent`

### "La extensión no funciona"
- Recarga la página web después de instalar la extensión
- Verifica que el agente esté ejecutándose
- Verifica que la extensión esté activada en `chrome://extensions/`

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que el agente esté ejecutándose
2. Verifica que la extensión esté instalada
3. Verifica que tengas una impresora configurada

Para más información: https://github.com/Kevin-HBA/print-agent

