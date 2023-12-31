@echo off
echo █▀ █▀▀ ▀█▀ █░█ █▀█
echo ▄█ ██▄ ░█░ █▄█ █▀▀
pip install pyinstaller

cls
echo █▀ █▀▀ ▀█▀ █░█ █▀█
echo ▄█ ██▄ ░█░ █▄█ █▀▀

set /p choice=Do you want to install default modules? (Y/N): 

if /I "%choice%"=="Y" (
    pip install -r modules.txt
) else if /I "%choice%"=="N" (
    exit /b 1
) else (
    echo Invalid choice
    pause
    exit /b 1
)