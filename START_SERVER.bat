@echo off
echo Starting Car Wash System...
call venv\Scripts\activate
python manage.py runserver
pause
