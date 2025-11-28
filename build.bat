@echo off
echo ========================================
echo Generando ejecutable para produccion
echo ========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    pause
    exit /b 1
)

echo [1/3] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo.
echo [2/3] Instalando PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo ERROR: No se pudo instalar PyInstaller
    pause
    exit /b 1
)

echo.
echo [3/3] Generando ejecutable...
pyinstaller --onefile ^
    --name print_agent ^
    --console ^
    --hidden-import flask ^
    --hidden-import requests ^
    --clean ^
    app/server.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo generar el ejecutable
    pause
    exit /b 1
)

echo.
echo ========================================
echo EXITO! Ejecutable generado
echo ========================================
echo.
echo Archivo: dist\print_agent.exe
echo.
echo IMPORTANTE: Configurar token y dominios en app\config_seguro.py
echo antes de distribuir el ejecutable.
echo.
pause

