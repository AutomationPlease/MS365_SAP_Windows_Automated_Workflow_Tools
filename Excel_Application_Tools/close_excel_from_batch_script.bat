:: I add this in the middle of my batch scripts for when I have trouble getting an excel window to close in a heavy workload script.
:: this will close all excel instances so don't use if you don't want excel to be completely killed.

echo Checking if Excel actually closed...
taskkill /IM excel.exe /F >nul 2>&1
if %ERRORLEVEL%==0 (
    echo Fallback used to close Excel.
) else (
    echo Excel was correctly closed, no fallback needed.
)
timeout /t 3 /nobreak >nul
echo.
