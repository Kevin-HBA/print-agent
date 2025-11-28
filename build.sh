#!/bin/bash

echo "========================================"
echo "Generando ejecutable para macOS"
echo "========================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "[0/4] Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: No se pudo crear el entorno virtual"
        exit 1
    fi
fi

# Activar entorno virtual
echo "[1/4] Activando entorno virtual..."
source venv/bin/activate

echo "[2/4] Instalando dependencias..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi

echo ""
echo "[3/4] Instalando PyInstaller..."
pip install pyinstaller
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo instalar PyInstaller"
    exit 1
fi

echo ""
echo "[4/4] Generando ejecutable..."
pyinstaller --onefile \
    --name print_agent \
    --console \
    --hidden-import flask \
    --hidden-import requests \
    --clean \
    app/server.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: No se pudo generar el ejecutable"
    exit 1
fi

echo ""
echo "========================================"
echo "EXITO! Ejecutable generado"
echo "========================================"
echo ""
echo "Archivo: dist/print_agent"
echo ""
echo "IMPORTANTE: Configurar token y dominios en app/config_seguro.py"
echo "antes de distribuir el ejecutable."
echo ""
echo "Para probarlo:"
echo "  ./dist/print_agent"
echo ""

