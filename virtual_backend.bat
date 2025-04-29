@echo off
REM --------------------------------
REM LifeHub: Aktivace venv + otevreni noveho okna
REM --------------------------------

REM 1) Pokud slozka venv neexistuje, vytvor ji
IF NOT EXIST "venv\" (
    echo Venv neexistuje, vytvarim...
    python -m venv venv
)

REM 2) Spustime nove cmd okno s aktivovanym venv
echo Oteviram nove okno s aktivovanym virtualnim prostredim...
cmd /k "call venv\Scripts\activate.bat && echo ^(venv^) Virtual environment activated. Pokracujte dalsimi prikazy... && cd /d %~dp0"
