@echo off
REM ----------------------------------------------------
REM  LifeHub start script
REM ----------------------------------------------------

REM 1) Vytvoření a aktivace venv
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate

REM 2) Instalace závislostí
echo Installing requirements...
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    pip install django djangorestframework django-allauth dj-rest-auth[with_social] djangorestframework-simplejwt django-cors-headers
)

REM 3) Reset databáze (vymaže SQLite soubor, pokud existuje)
if exist db.sqlite3 (
    echo Deleting old database...
    del db.sqlite3
)

REM 4) Makemigrations
echo Making migrations...
python manage.py makemigrations

REM 4.1) Aplikuj migrace pro vlastní aplikace dřív
echo Applying users migrations...
python manage.py migrate users

REM 4.2) Aplikuj zbytek migrací
echo Applying remaining migrations...
python manage.py migrate

REM 5) Spuštění dev serveru
echo Starting development server...
python manage.py runserver

REM 6) Ponech okno otevřené
pause
