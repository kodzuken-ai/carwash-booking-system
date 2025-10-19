# ⚡ Hostinger Quick Start - 15 Minutes

Fast track deployment guide. For detailed instructions, see [HOSTINGER_DEPLOYMENT.md](./HOSTINGER_DEPLOYMENT.md)

---

## Before You Start ✅

- [ ] SSH Access enabled
- [ ] MySQL database created in hPanel
- [ ] Database credentials saved

---

## 🚀 Quick Steps

### 1. Create MySQL Database (2 min)
```
hPanel → Databases → MySQL Databases → Create
Database: u842241420_carwash
User: u842241420_carwash
Password: [choose strong password]
```

### 2. Update Local Project (3 min)

**Install MySQL driver:**
```bash
pip install mysqlclient
```

**Update `requirements.txt`:**
```txt
Django==5.0.6
mysqlclient
gunicorn
whitenoise
python-decouple
requests
```

**Update `settings.py` - Database section:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u842241420_carwash',
        'USER': 'u842241420_carwash',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DEBUG = False
ALLOWED_HOSTS = ['green-tiger-9390006.hostingersite.com', '*.hostingersite.com']
```

### 3. Upload Code (2 min)
```
hPanel → File Manager → public_html
Create folder: carwash
Upload entire django_carwash folder
```

### 4. SSH Setup (5 min)

**Connect:**
```bash
ssh -p 65002 u842241420@145.79.25.46
```

**Setup environment:**
```bash
cd ~/public_html/carwash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 5. Create passenger_wsgi.py (1 min)

**File:** `~/public_html/passenger_wsgi.py`

```python
import sys
import os

project_home = '/home/u842241420/public_html/carwash'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'carwash.settings'

activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Create .htaccess (1 min)

**File:** `~/public_html/.htaccess`

```apache
PassengerEnabled On
PassengerAppRoot /home/u842241420/public_html/carwash
PassengerPython /home/u842241420/public_html/carwash/venv/bin/python3
PassengerStartupFile passenger_wsgi.py
PassengerAppType wsgi
```

### 7. Restart & Test (1 min)

```bash
touch ~/public_html/passenger_wsgi.py
```

**Visit:** `https://green-tiger-9390006.hostingersite.com`

---

## ✅ Done!

**If it works:** Congrats! 🎉  
**If 500 error:** Check `~/logs/error.log`  
**If no CSS:** Run `python manage.py collectstatic --noinput`

---

## 🆘 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| 500 Error | Check `~/logs/error.log` |
| No CSS | `python manage.py collectstatic --noinput` |
| Database error | Verify MySQL credentials |
| Module not found | `pip install -r requirements.txt` |

---

**For detailed guide, see:** [HOSTINGER_DEPLOYMENT.md](./HOSTINGER_DEPLOYMENT.md)
