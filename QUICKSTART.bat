@echo off
echo ========================================
echo  Car Wash System - Django Quick Start
echo ========================================
echo.

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo [3/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/5] Running migrations...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)

echo [5/5] Setup complete!
echo.
echo ========================================
echo  Next Steps:
echo ========================================
echo 1. Create admin user: python manage.py createsuperuser
echo 2. Start server: python manage.py runserver
echo 3. Open browser: http://localhost:8000
echo.
echo Press any key to create admin user now...
pause >nul

python manage.py createsuperuser

echo.
echo ========================================
echo Starting development server...
echo ========================================
python manage.py runserver

pause
