# 🚀 Deploy Django Car Wash System on Hostinger

Complete step-by-step guide to deploy your Django application on Hostinger Premium Web Hosting.

---

## 📋 Prerequisites

Before starting, make sure you have:

- ✅ Hostinger Premium Web Hosting account
- ✅ SSH access enabled (you have this!)
- ✅ Your SSH credentials ready
- ✅ FTP/File Manager access
- ✅ MySQL database access

**Your SSH Details:**
- **IP**: `145.79.25.46`
- **Port**: `65002`
- **Username**: `u842241420`

---

## 🎯 Deployment Overview

```
1. Enable SSH Access
2. Create MySQL Database
3. Upload Your Code
4. Setup Python Environment
5. Configure MySQL Database
6. Update Django Settings
7. Install Dependencies
8. Run Migrations
9. Configure Web Server (Passenger)
10. Collect Static Files
11. Test Your Site
```

---

## Step 1: Enable SSH Access ✅

1. Login to **Hostinger hPanel**
2. Go to **Advanced** → **SSH Access**
3. Click **Enable** button
4. Note your credentials (you already have these!)

---

## Step 2: Create MySQL Database 🗄️

### In Hostinger hPanel:

1. Go to **Databases** → **MySQL Databases**
2. Click **Create Database**
   - **Database Name**: `u842241420_booking`
   - **Username**: `u842241420_booking`
   - **Password**: Carwash.123
3. Click **Create**
4. **Grant all privileges** to the user

**Save these credentials - you'll need them!**

```
Database Name: u842241420_carwash
Username: u842241420_carwash
Password: [your-chosen-password]
Host: localhost
Port: 3306
```

---

## Step 3: Connect via SSH 💻

### On Windows (PowerShell or Command Prompt):

```bash
ssh -p 65002 u842241420@145.79.25.46
```

Enter your password when prompted.

### First Time? Check Python:

```bash
python3 --version
pip3 --version
```

**Expected output**: Python 3.x and pip version

---

## Step 4: Prepare Your Local Project 📦

### Update `requirements.txt`:

```txt
Django==5.0.6
mysqlclient
gunicorn
whitenoise
python-decouple
requests
```

### Update `settings.py`:

Add these imports at the top:

```python
import os
from pathlib import Path
from decouple import config
```

Update database settings:

```python
# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='u842241420_carwash'),
        'USER': config('DB_USER', default='u842241420_carwash'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

Update other settings:

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security Settings for Production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### Create `.env` file (for local testing):

```env
DEBUG=False
DB_NAME=u842241420_carwash
DB_USER=u842241420_carwash
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=green-tiger-9390006.hostingersite.com,*.hostingersite.com
SECRET_KEY=your-secret-key
```

**Note**: Don't upload `.env` to server. We'll set environment variables differently.

---

## Step 5: Upload Your Code 📤

### Option A: Using File Manager (Easier)

1. Go to **hPanel** → **File Manager**
2. Navigate to `public_html`
3. Create folder `carwash`
4. Upload your entire `django_carwash` folder into it
5. Make sure you have:
   ```
   public_html/carwash/
   ├── manage.py
   ├── carwash/
   ├── bookings/
   ├── templates/
   ├── requirements.txt
   └── ...all other files
   ```

### Option B: Using Git (Advanced)

```bash
# Connect via SSH first
ssh -p 65002 u842241420@145.79.25.46

# Navigate to public_html
cd ~/public_html

# Clone your repository
git clone https://github.com/your-username/your-repo.git carwash
cd carwash
```

---

## Step 6: Setup Python Virtual Environment 🐍

### Via SSH:

```bash
# Navigate to your project
cd ~/public_html/carwash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

**Common Issues:**

If `mysqlclient` fails to install:
```bash
# Try this instead
pip install pymysql
```

Then add to `settings.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

## Step 7: Configure Environment Variables 🔐

Create a file `~/public_html/carwash/.env.production`:

```bash
nano ~/public_html/carwash/.env.production
```

Add this content:

```env
DEBUG=False
SECRET_KEY=generate-a-new-secret-key-here
DB_NAME=u842241420_carwash
DB_USER=u842241420_carwash
DB_PASSWORD=your-mysql-password-here
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=green-tiger-9390006.hostingersite.com,*.hostingersite.com
```

**Generate SECRET_KEY:**
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Save file: `Ctrl + X`, then `Y`, then `Enter`

Update your `settings.py` to use this file:

```python
# Load environment from .env.production file
from pathlib import Path
env_file = Path(__file__).resolve().parent.parent / '.env.production'
if env_file.exists():
    from decouple import Config, RepositoryEnv
    config = Config(RepositoryEnv(str(env_file)))
else:
    from decouple import config
```

---

## Step 8: Run Django Commands 🔧

### With virtual environment activated:

```bash
cd ~/public_html/carwash

# Activate venv
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Test if Django works
python manage.py check
```

**Expected output**: `System check identified no issues (0 silenced).`

---

## Step 9: Configure Passenger WSGI 🚀

### Create `passenger_wsgi.py` in `~/public_html/`:

```bash
cd ~/public_html
nano passenger_wsgi.py
```

**Add this content:**

```python
import sys
import os

# Add your project directory to sys.path
project_home = '/home/u842241420/public_html/carwash'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'carwash.settings'
os.environ['PYTHON_ENV'] = 'production'

# Activate virtual environment
activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Get Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Save: `Ctrl + X`, `Y`, `Enter`

---

## Step 10: Configure .htaccess 📝

### Create `.htaccess` in `~/public_html/`:

```bash
cd ~/public_html
nano .htaccess
```

**Add this content:**

```apache
# Enable Passenger
PassengerEnabled On
PassengerAppRoot /home/u842241420/public_html/carwash

# Python Configuration
PassengerPython /home/u842241420/public_html/carwash/venv/bin/python3
PassengerStartupFile passenger_wsgi.py
PassengerAppType wsgi

# Set Python Path
SetEnv PYTHONPATH "/home/u842241420/public_html/carwash:/home/u842241420/public_html/carwash/venv/lib/python3.11/site-packages"

# Django Settings
SetEnv DJANGO_SETTINGS_MODULE "carwash.settings"

# Static and Media Files
<IfModule mod_alias.c>
    Alias /static /home/u842241420/public_html/carwash/static_collected
    Alias /media /home/u842241420/public_html/carwash/media
</IfModule>

<Directory /home/u842241420/public_html/carwash/static_collected>
    Require all granted
</Directory>

<Directory /home/u842241420/public_html/carwash/media>
    Require all granted
</Directory>

# Force HTTPS (Optional but recommended)
# RewriteEngine On
# RewriteCond %{HTTPS} off
# RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

Save: `Ctrl + X`, `Y`, `Enter`

---

## Step 11: Set File Permissions 🔒

```bash
# Set permissions for the project
chmod -R 755 ~/public_html/carwash

# Make sure Python can write to database folder
chmod 775 ~/public_html/carwash

# If using SQLite (not recommended)
# chmod 664 ~/public_html/carwash/db.sqlite3
```

---

## Step 12: Restart Application 🔄

```bash
# Touch passenger_wsgi.py to restart app
touch ~/public_html/passenger_wsgi.py

# Or create a tmp/restart.txt file
mkdir -p ~/public_html/tmp
touch ~/public_html/tmp/restart.txt
```

---

## Step 13: Test Your Site 🎉

1. Open browser
2. Visit: `https://green-tiger-9390006.hostingersite.com`
3. You should see your car wash homepage!

### Test Admin Panel:

1. Visit: `https://green-tiger-9390006.hostingersite.com/admin`
2. Login with superuser credentials
3. Verify everything works

### Test Booking:

1. Register a new user
2. Try to create a booking
3. Check if emails work (EmailJS)
4. Verify admin can see and manage bookings

---

## 🆘 Troubleshooting

### Issue 1: 500 Internal Server Error

**Check error logs:**
```bash
tail -f ~/logs/error.log
```

**Common causes:**
- Wrong database credentials
- Python path incorrect
- Missing dependencies
- DEBUG=True (should be False)

**Fix:**
```bash
# Verify settings
cd ~/public_html/carwash
source venv/bin/activate
python manage.py check

# Check if modules are installed
pip list

# Test database connection
python manage.py migrate --run-syncdb
```

---

### Issue 2: Static Files Not Loading (No CSS)

```bash
cd ~/public_html/carwash
source venv/bin/activate
python manage.py collectstatic --noinput --clear
touch ~/public_html/passenger_wsgi.py
```

**Update settings.py:**
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
```

---

### Issue 3: Database Connection Error

**Verify MySQL credentials:**
```bash
mysql -u u842241420_carwash -p
# Enter your password
# If this works, connection is fine
```

**Check settings.py database config:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u842241420_carwash',
        'USER': 'u842241420_carwash',
        'PASSWORD': 'correct-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### Issue 4: Passenger Not Working

**Check if Passenger is available:**
```bash
passenger-config about version
```

**If not available:**
Contact Hostinger support and ask:
> "Can you enable Passenger/Python support for my account?"

---

### Issue 5: Import Error / Module Not Found

```bash
cd ~/public_html/carwash
source venv/bin/activate
pip install -r requirements.txt --force-reinstall
touch ~/public_html/passenger_wsgi.py
```

---

### Issue 6: Permission Denied

```bash
chmod -R 755 ~/public_html/carwash
chmod 775 ~/public_html/carwash
chown -R u842241420:u842241420 ~/public_html/carwash
```

---

## 🔧 Maintenance Commands

### Update Code:

```bash
cd ~/public_html/carwash
git pull origin main  # if using git
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
touch ~/public_html/passenger_wsgi.py
```

### View Logs:

```bash
# Error logs
tail -f ~/logs/error.log

# Access logs
tail -f ~/logs/access.log

# Django logs (if configured)
tail -f ~/public_html/carwash/django.log
```

### Backup Database:

```bash
mysqldump -u u842241420_carwash -p u842241420_carwash > backup_$(date +%Y%m%d).sql
```

### Restore Database:

```bash
mysql -u u842241420_carwash -p u842241420_carwash < backup_20251019.sql
```

---

## 📱 Custom Domain Setup (Optional)

### If you have a custom domain:

1. **In hPanel:**
   - Go to **Domains** → **Add Domain**
   - Add your custom domain

2. **Update DNS:**
   - Point A record to: `145.79.25.46`
   - Wait for propagation (up to 24 hours)

3. **Update Django settings:**
   ```python
   ALLOWED_HOSTS = [
       'yourdomain.com',
       'www.yourdomain.com',
       'green-tiger-9390006.hostingersite.com'
   ]
   ```

4. **Enable HTTPS:**
   - In hPanel → SSL → Enable for your domain

---

## 🎯 Performance Tips

### 1. Enable Caching:

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/u842241420/cache',
    }
}
```

### 2. Optimize Static Files:

```bash
pip install django-compressor
```

### 3. Use CDN (Optional):

Consider using Cloudflare for better performance.

---

## ✅ Deployment Checklist

Before going live:

- [ ] MySQL database created
- [ ] Environment variables set
- [ ] Dependencies installed
- [ ] Migrations run
- [ ] Superuser created
- [ ] Static files collected
- [ ] passenger_wsgi.py created
- [ ] .htaccess configured
- [ ] DEBUG=False in settings
- [ ] ALLOWED_HOSTS updated
- [ ] Site tested in browser
- [ ] Admin panel accessible
- [ ] Booking system works
- [ ] Email notifications work
- [ ] Error logs checked
- [ ] Backup plan in place

---

## 🎉 Success!

Your Django Car Wash System is now live on Hostinger!

**Live URL**: `https://green-tiger-9390006.hostingersite.com`

**Admin Panel**: `https://green-tiger-9390006.hostingersite.com/admin`

---

## 📞 Getting Help

### Hostinger Support:
- Live chat in hPanel
- Email support
- Knowledge base

### Common Questions:
- "How do I enable Python/Passenger?"
- "Where are my error logs?"
- "How do I increase PHP memory?" (not needed for Django)

---

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Hostinger Documentation](https://support.hostinger.com/)
- [Passenger Documentation](https://www.phusionpassenger.com/docs/)

---

**Good luck with your deployment! 🚀**

*For issues, check error logs first: `~/logs/error.log`*
