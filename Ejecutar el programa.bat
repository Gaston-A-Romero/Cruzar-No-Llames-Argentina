@echo off
setlocal enabledelayedexpansion

:: Mostrar banner simple para descartar problemas
echo.
echo ============================
echo ****Duplicados No Llames****
echo ============================
echo.         
pause

:: Cambiar al directorio del script
cd /d "%~dp0\..\Cruzar-No-Llames-Argentina"
if errorlevel 1 (
  echo * No se pudo cambiar al directorio No llames TEST
  pause
  exit /b
)

:: Verificar que Python esté disponible
where python >nul 2>&1
if errorlevel 1 (
  echo * Python no está instalado o no está en el PATH.
  pause
  exit /b
)

echo Se va a ejecutar el script.
:: Ejecutar el script
python Repetidos.py

echo.
echo * Proceso finalizado. Presiona una tecla para salir.
pause
