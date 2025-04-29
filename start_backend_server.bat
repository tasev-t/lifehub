@echo off
REM Ověření, zda je Python dostupný v PATH
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python neni nainstalovan.
    pause
    exit /B 1
) ELSE (
    echo Python je nainstalovan, verze:
    python --version
)

REM Přechod do adresáře projektu (zůstaneme tam, kde je tento soubor)
cd /d %~dp0

REM Spuštění vývojového serveru Django
python manage.py runserver

pause
