@echo off
cd /d "%~dp0"

:: obviously adjust to your computer, demonstration below to show structure, added delay so they don't fight to start.
:: add additional helper scripts always after starting keep_alive first.

start "" ".venv\Scripts\pythonw.exe" "keep_alive.pyw"
timeout /t 2 >nul
start "" ".venv\Scripts\pythonw.exe" "smart_mouse_clicker.pyw"
