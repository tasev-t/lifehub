@echo off
REM Přesune se do adresáře, kde je uložen skript (uprav cestu dle potřeby)
cd /d "C:\Users\tasev\lifehub"

REM Spustí Python skript snapshot_generator.py
python snapshot_generator.py

REM Zabrání zavření okna po dokončení – čeká na stisk klávesy
pause
