@REM @echo off
@REM REM Activate the virtual environment
@REM call .venv\Scripts\activate.bat

@REM REM Change directory to the Django project folder
@REM cd stdsystem

@REM REM Start the Django development server
@REM python manage.py runserver

@REM pause


@echo off
title Starting Django Development Server
color 0A
cls

echo ====================================================
echo          DJANGO DEVELOPMENT SERVER LAUNCHER         
echo ====================================================
echo.
echo 🐍 Activating virtual environment...
call .venv\Scripts\activate.bat

echo ✅ Virtual environment activated.
echo.

echo 📁 Navigating to project folder: stdsystem
cd stdsystem

echo 🚀 Starting Django development server...
echo ----------------------------------------------------
echo Server will be available at:
echo   🌐 http://127.0.0.1:8000/
echo ----------------------------------------------------
echo.

REM Start the Django development server
python manage.py runserver

REM Once server stops
echo.
echo 🔴 Django server has stopped.
pause
