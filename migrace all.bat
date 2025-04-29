@echo off
echo Python je nainstalovan, verze:
python --version

echo Vytvarim migrace pro users...
python manage.py makemigrations users

echo Vytvarim migrace pro nutrition...
python manage.py makemigrations nutrition

echo Vytvarim migrace pro finance...
python manage.py makemigrations finance

echo Vytvarim migrace pro pets...
python manage.py makemigrations pets

echo Vytvarim migrace pro common...
python manage.py makemigrations common

echo Probiha migrace databaze...
python manage.py migrate

echo Hotovo.
pause
