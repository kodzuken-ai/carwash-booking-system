# 🚗 Car Wash Booking System

A modern, full-featured car wash booking system built with Django. Manage appointments, services, users, and bookings with an intuitive admin dashboard and customer portal.

![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue.svg)
![License](https://img.shields.io/badge/License-Educational-yellow.svg)

## ✨ Features

### For Customers:
- ✅ **User Registration & Login** - Secure authentication system
- ✅ **Browse Services** - View available car wash packages and services
- ✅ **Book Appointments** - Select date, time, and service
- ✅ **Booking Management** - View, filter, and track your bookings
- ✅ **Email Notifications** - Receive booking confirmations
- ✅ **Weather Info** - Real-time weather updates

### For Administrators:
- ✅ **Admin Dashboard** - Comprehensive management interface
- ✅ **Booking Management** - View, update, and manage all bookings
- ✅ **Service Management** - Full CRUD operations for services
- ✅ **User Management** - Manage customer accounts
- ✅ **Status Updates** - Change booking status (pending, confirmed, in-progress, completed)
- ✅ **Filtering & Search** - Find bookings by date, status, service, customer

### System Features:
- ✅ **Time Slot Management** - Maximum 5 bookings per time slot
- ✅ **Past Date Prevention** - Cannot book past dates
- ✅ **Role-based Access** - Customer and Admin roles with different permissions
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile
- ✅ **Dark Theme UI** - Modern, professional interface
- ✅ **Database Flexibility** - SQLite for development, PostgreSQL for production

## 🛠️ Tech Stack

- **Framework**: Django 5.0.6
- **Language**: Python 3.11+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Django Templates, HTML5, CSS3, JavaScript
- **Web Server**: Gunicorn (production)
- **Static Files**: WhiteNoise
- **APIs**: 
  - OpenWeather API (weather data)
  - EmailJS (email notifications)
- **Authentication**: Django built-in auth system
- **Deployment**: Railway / Render ready

## Quick Start

### 1. Install Python

Make sure you have Python 3.8+ installed:
```bash
python --version
```

### 2. Create Virtual Environment

```bash
# Navigate to project directory
cd django_carwash

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (Optional)

```bash
# Copy .env.example to .env
copy .env.example .env

# Edit .env and add your OpenWeather API key
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit **http://localhost:8000** in your browser.

## Default Accounts

After running migrations, you'll need to create accounts:

1. **Admin Account**: Create via `python manage.py createsuperuser`
2. **Regular Users**: Register via the website at `/register`

## Setting Admin Role

After creating a superuser, you need to set their role to 'admin':

1. Go to **http://localhost:8000/admin**
2. Login with your superuser credentials
3. Click on **User Profiles**
4. Find your user and change role to **admin**
5. Save

OR use Django shell:
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
from bookings.models import UserProfile

user = User.objects.get(username='your_username')
profile, created = UserProfile.objects.get_or_create(user=user)
profile.role = 'admin'
profile.save()
```

## Project Structure

```
django_carwash/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database (created after migrations)
├── carwash/                 # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── bookings/                # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # URL patterns
│   ├── forms.py             # Forms
│   ├── admin.py             # Admin configuration
│   └── signals.py           # Django signals
└── templates/               # HTML templates
    ├── base.html            # Base template
    └── bookings/            # Booking templates
        ├── home.html
        ├── login.html
        ├── register.html
        ├── dashboard.html
        ├── create_booking.html
        ├── booking_detail.html
        ├── admin_dashboard.html
        └── update_status.html
```

## Service Pricing

| Service | Price |
|---------|-------|
| Basic Wash | ₱150 |
| Premium Wash | ₱300 |
| Deluxe Wash | ₱500 |
| Interior Cleaning | ₱400 |
| Full Detail | ₱800 |

## Admin Panel

Access the Django admin panel at **http://localhost:8000/admin**

Features:
- Manage users and profiles
- View and edit all bookings
- Bulk actions for booking status updates
- Search and filter functionality

## 🚀 Deployment

### Deploy for FREE in 10 Minutes!

**Recommended Platform: Railway** ⭐

This project is configured and ready to deploy on Railway with:
- ✅ PostgreSQL database included
- ✅ Free $5 credit/month
- ✅ Automatic deployments from GitHub
- ✅ SSL certificate included
- ✅ Zero configuration needed

### 📚 Detailed Deployment Guide:

**See [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md)** for complete step-by-step instructions.

### Quick Steps:

1. Push code to GitHub
2. Sign up on [Railway.app](https://railway.app)
3. Deploy from GitHub
4. Add PostgreSQL database
5. Set environment variables
6. Done! Your site is live 🎉

**Total time: ~10 minutes**

---

## Alternative Free Hosting Platforms:

| Platform | Free Tier | Database | Setup Time | Guide |
|----------|-----------|----------|------------|-------|
| **Railway** | $5 credit/mo | PostgreSQL ✅ | 10 min | [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md) |
| **Render** | 750 hrs/mo | PostgreSQL ✅ | 15 min | [README.md](./README.md#render-deployment) |
| **PythonAnywhere** | Always free | MySQL ✅ | 20 min | [README.md](./README.md#pythonanywhere) |

---

## 📋 Project Structure

```
django_carwash/
├── carwash/                 # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── bookings/                # Main application
│   ├── models.py            # Database models (Service, Booking, UserProfile)
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── urls.py              # App URL patterns
│   └── admin.py             # Admin configuration
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── user/                # Customer templates
│   └── admin/               # Admin templates
├── static/                  # Static files (created on collectstatic)
├── staticfiles/             # Collected static files
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── Procfile                 # For Railway/Heroku deployment
├── runtime.txt              # Python version
└── README.md                # This file
```

---

## 🎓 Usage Guide

### Steps:

#### 1. Prepare Your Project

Create these files in your project root:

**`requirements.txt`**
```txt
Django==5.0.6
psycopg2-binary
gunicorn
whitenoise
python-decouple
requests
```

**`Procfile`** (create this file, no extension)
```
web: gunicorn carwash.wsgi
```

**`runtime.txt`**
```
python-3.11.0
```

**`.env.example`** (template for environment variables)
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:pass@host/db
OPENWEATHER_API_KEY=your-key
EMAILJS_PUBLIC_KEY=your-key
EMAILJS_SERVICE_ID=your-service-id
EMAILJS_TEMPLATE_ID=your-template-id
```

#### 2. Update `settings.py`

Add to top of file:
```python
import os
from decouple import config
import dj_database_url
```

Update settings:
```python
# Security
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-this')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3')
    )
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware (add WhiteNoise)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]
```

#### 3. Deploy to Railway

1. **Sign up**: Go to https://railway.app
2. **New Project**: Click "New Project"
3. **Deploy from GitHub**:
   - Connect your GitHub account
   - Select your repository
4. **Add PostgreSQL**:
   - Click "New" → "Database" → "Add PostgreSQL"
5. **Set Environment Variables**:
   - Go to your web service
   - Click "Variables" tab
   - Add:
     - `SECRET_KEY`: Generate at https://djecrety.ir/
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `*.railway.app`
     - Other API keys as needed
6. **Deploy**:
   - Railway auto-deploys on every git push
   - Wait for deployment to complete

#### 4. Run Migrations

In Railway dashboard:
- Click on your service → "Settings" → "Deploy"
- Under "Custom Build Command":
  ```bash
  python manage.py migrate && python manage.py collectstatic --noinput
  ```

#### 5. Create Admin User

Use Railway's terminal feature or add a management command.

---

## Option 2: Render 🎨

**Free tier includes:**
- ✅ **Free forever** (with limitations)
- ✅ PostgreSQL database included
- ✅ Automatic HTTPS
- ✅ 750 hours/month

### Steps:

1. **Create `render.yaml`**:
```yaml
services:
  - type: web
    name: carwash
    env: python
    buildCommand: "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate"
    startCommand: "gunicorn carwash.wsgi"
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
      - key: PYTHON_VERSION
        value: 3.11.0

databases:
  - name: carwash-db
    databaseName: carwash
    user: carwash
```

2. **Push to GitHub**

3. **Deploy on Render**:
   - Go to https://render.com
   - "New" → "Web Service"
   - Connect GitHub repository
   - Select the repo
   - Click "Create Web Service"

---

## Option 3: PythonAnywhere 🐍

**Free tier includes:**
- ✅ **Always free**
- ✅ MySQL database
- ✅ Easy Django setup
- ✅ Simple interface

### Steps:

1. **Sign up**: https://www.pythonanywhere.com

2. **Upload code**:
   - Bash console: `git clone <your-repo-url>`

3. **Setup Virtual Environment**:
```bash
mkvirtualenv --python=/usr/bin/python3.10 carwash
pip install -r requirements.txt
```

4. **Configure Web App**:
   - Web tab → "Add new web app"
   - Manual configuration → Python 3.10
   - Set paths:
     - Source code: `/home/yourusername/carwash/django_carwash`
     - Virtualenv: `/home/yourusername/.virtualenvs/carwash`

5. **Edit WSGI file**:
```python
import os
import sys

path = '/home/yourusername/carwash/django_carwash'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'carwash.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. **Run migrations**:
```bash
python manage.py migrate
python manage.py createsuperuser
```

7. **Reload web app**

---

## Option 4: Vercel (Frontend Only) ⚡

**Note**: Vercel is best for static sites. For Django, use Railway or Render.

---

## 📦 Pre-Deployment Checklist

Before deploying, make sure you have:

- [x] `requirements.txt` with all dependencies
- [x] `Procfile` for production server
- [x] `runtime.txt` specifying Python version
- [x] Updated `settings.py` with:
  - Environment variables
  - PostgreSQL database config
  - WhiteNoise for static files
  - Proper `ALLOWED_HOSTS`
  - `DEBUG = False`
- [x] `.gitignore` excluding:
  ```
  *.pyc
  __pycache__/
  db.sqlite3
  .env
  staticfiles/
  ```
- [x] Static files configured
- [x] Database migrations created
- [x] All API keys in environment variables

---

## 🔒 Production Settings

**Critical settings for production:**

```python
# settings.py

# Security
DEBUG = False
SECRET_KEY = config('SECRET_KEY')  # Never commit this!
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Database
# Use PostgreSQL in production (provided by hosting platform)
```

---

## 🎉 After Deployment

1. **Test the site**: Visit your deployed URL
2. **Create admin**: Run `python manage.py createsuperuser` on server
3. **Configure EmailJS**: Add your EmailJS keys to environment variables
4. **Test booking flow**: Create a test booking
5. **Monitor logs**: Check for errors in platform dashboard

---

## 💰 Cost Comparison

| Platform | Free Tier | Database | SSL | Best For |
|----------|-----------|----------|-----|----------|
| **Railway** | $5 credit/month | PostgreSQL ✅ | Free ✅ | Full-stack apps |
| **Render** | 750 hrs/month | PostgreSQL ✅ | Free ✅ | Always-on apps |
| **PythonAnywhere** | Always free | MySQL ✅ | Free ✅ | Beginners |
| **Heroku** | No free tier | PostgreSQL | $7/mo | ❌ Not free anymore |

---

## 🆘 Deployment Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Connection Error
- Check `DATABASE_URL` environment variable
- Verify PostgreSQL is provisioned

### Module Not Found
- Check all packages are in `requirements.txt`
- Rebuild the deployment

### Internal Server Error (500)
- Check logs in platform dashboard
- Verify `DEBUG=False` is set
- Check `ALLOWED_HOSTS` includes your domain

---

## 📚 Additional Resources

- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)
- [PythonAnywhere Django Guide](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| SECRET_KEY | Django secret key | Yes |
| DEBUG | Debug mode (True/False) | Yes |
| OPENWEATHER_API_KEY | OpenWeather API key | Optional |
| OPENWEATHER_CITY | Default city for weather | Optional |

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Django shell
python manage.py shell
```

## Troubleshooting

### "No module named 'bookings'"
Run: `python manage.py makemigrations bookings`

### Weather API not working
Check your `OPENWEATHER_API_KEY` in settings.py or .env file

### Admin role not working
Make sure you set the user's profile role to 'admin' via Django admin panel

### Static files not loading
Run: `python manage.py collectstatic`

## Support

For issues or questions, check:
1. Django documentation: https://docs.djangoproject.com/
2. Project README
3. Error logs in terminal

## License

This project is for educational purposes.
