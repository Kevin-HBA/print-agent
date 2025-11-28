# Instalación en Diferentes Navegadores

## Navegadores Soportados

### Chrome y Edge (Chromium)
- ✅ **Soporte completo** - Funciona directamente
- ✅ **Mismo proceso de instalación**

### Firefox
- ⚠️ **Requiere adaptación** - Usa Manifest V2 (diferente)
- Necesita modificar `manifest.json`

### Safari
- ❌ **No soportado** - Safari usa sistema diferente
- Requiere desarrollo específico para Safari

### Opera
- ✅ **Funciona** - Basado en Chromium, igual que Chrome

---

## Instrucciones por Navegador

### 1. Chrome

**Pasos:**
1. Abrir Chrome
2. Ir a: `chrome://extensions/`
3. Activar "Modo de desarrollador" (toggle superior derecha)
4. Clic en "Cargar extensión sin empaquetar"
5. Seleccionar carpeta `extension/`
6. ✅ Listo

---

### 2. Microsoft Edge

**Pasos:**
1. Abrir Edge
2. Ir a: `edge://extensions/`
3. Activar "Modo de desarrollador" (toggle superior derecha)
4. Clic en "Cargar extensión sin empaquetar"
5. Seleccionar carpeta `extension/`
6. ✅ Listo

---

### 3. Opera

**Pasos:**
1. Abrir Opera
2. Ir a: `opera://extensions/`
3. Activar "Modo de desarrollador"
4. Clic en "Cargar extensión sin empaquetar"
5. Seleccionar carpeta `extension/`
6. ✅ Listo

---

### 4. Firefox (Requiere Adaptación)

**Problema:** Firefox usa Manifest V2, la extensión actual usa V3.

**Solución:** Crear versión adaptada para Firefox.

**Pasos:**
1. Modificar `manifest.json` para Firefox (Manifest V2)
2. Cambiar `background.service_worker` por `background.scripts`
3. Adaptar código si es necesario
4. Instalar en Firefox:
   - Ir a: `about:debugging`
   - Clic en "Este Firefox"
   - "Cargar complemento temporal"
   - Seleccionar carpeta

---

### 5. Safari (No Soportado Actualmente)

**Problema:** Safari usa sistema completamente diferente (App Extensions).

**Solución:** Requiere desarrollo específico para Safari (Xcode, Swift/Objective-C).

**Alternativa:** Usar solo Chrome/Edge/Opera.

---

## Recomendación

### Opción 1: Solo Chrome/Edge (Recomendado)
- ✅ Funciona inmediatamente
- ✅ Cubre la mayoría de usuarios
- ✅ Sin adaptaciones necesarias

### Opción 2: Empaquetar y Publicar
- Subir extensión a Chrome Web Store
- Usuarios instalan con un clic
- Más fácil para usuarios

### Opción 3: Crear Versión Firefox
- Adaptar código para Manifest V2
- Distribuir ambas versiones

---

## Instalación para Usuarios

### Chrome/Edge/Opera (Mismo Proceso)

**Instrucciones para usuarios:**

1. Descargar carpeta `extension/` completa
2. Abrir navegador (Chrome/Edge/Opera)
3. Ir a extensiones:
   - Chrome: `chrome://extensions/`
   - Edge: `edge://extensions/`
   - Opera: `opera://extensions/`
4. Activar "Modo de desarrollador"
5. "Cargar extensión sin empaquetar"
6. Seleccionar carpeta `extension/`
7. ✅ Listo

---

## Distribución Masiva

### Opción A: Instalación Manual
- Enviar carpeta `extension/` a cada usuario
- Cada uno instala manualmente

### Opción B: Chrome Web Store (Recomendado)
- Empaquetar extensión
- Subir a Chrome Web Store
- Usuarios instalan con un clic desde la tienda

### Opción C: Política de Empresa (Windows)
- Si es entorno corporativo
- Instalar vía Group Policy
- Instalación automática para todos

---

## Notas Importantes

- **Chrome/Edge/Opera**: Funcionan igual, mismo proceso
- **Firefox**: Requiere adaptación del código
- **Safari**: No soportado actualmente
- **Recomendación**: Enfocarse en Chrome/Edge que cubren ~90% de usuarios

