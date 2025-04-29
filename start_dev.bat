@echo off
REM — přejdeme do složky, kde je tento skript
cd /d "%~dp0"

REM — pokud neexistuje, vytvoříme virtuální prostředí
if not exist venv (
    echo Vytvarim virtualni prostredi...
    python -m venv venv
)

REM — aktivujeme venv
echo Aktivuju virtualni prostredi...
call venv\Scripts\activate.bat

REM — informační hláška
echo.
echo Virtualni prostredi je aktivni.
echo Teď můžete:
echo  - pip install -r requirements.txt     (nainstalovat zalezitosti)
echo  - python manage.py makemigrations     (vytvorit migrace)
echo  - python manage.py migrate            (aplikovat migrace)
echo  - python manage.py runserver         (spustit lokalni server)
echo.

REM — spustime dalsi cmd v ramci venv, aby okno zustalo otevrene
cmd /k
