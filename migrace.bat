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

REM Spuštění příkazu pro vytvoření migrací
echo Spoustim makemigrations...
python manage.py makemigrations

REM Spuštění migrací
echo Spoustim migrate...
python manage.py migrate

pause
