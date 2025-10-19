# Django Car Wash System - Setup Guide

## Complete Installation & Setup Instructions

### Prerequisites

- **Python 3.8 or higher** (Download from https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** (optional, for version control)

### Step-by-Step Setup

#### 1. Navigate to Project Directory

```bash
cd C:\Users\Admin\Desktop\carwash\django_carwash
```

#### 2. Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2.7
- requests 2.31.0 (for weather API)

#### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) and all necessary tables.

#### 5. Create Admin Superuser

```bash
python manage.py createsuperuser
```

Enter:
- Username: `admin` (or your choice)
- Email: `admin@carwash.com`
- Password: (choose a secure password)

#### 6. Set Admin Role

After creating the superuser, run Django shell:

```bash
python manage.py shell
```

Then execute:
```python
from django.contrib.auth.models import User
from bookings.models import UserProfile

user = User.objects.get(username='admin')  # Replace with your username
profile, created = UserProfile.objects.get_or_create(user=user)
profile.role = 'admin'
profile.save()
print(f"Admin role set for {user.username}")
exit()
```

#### 7. Start Development Server

```bash
python manage.py runserver
```

The server will start at **http://localhost:8000**

### Accessing the Application

1. **Homepage**: http://localhost:8000
2. **User Registration**: http://localhost:8000/register
3. **User Login**: http://localhost:8000/login
4. **Django Admin Panel**: http://localhost:8000/admin
5. **User Dashboard**: http://localhost:8000/dashboard (after login)
6. **Admin Dashboard**: http://localhost:8000/admin-dashboard (admin only)

### Creating Test Users

#### Option 1: Via Website
1. Go to http://localhost:8000/register
2. Fill in the registration form
3. Login with your credentials

#### Option 2: Via Django Admin
1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. Click "Users" → "Add User"
4. Create user and set password
5. Edit the user to add first name, last name, email
6. Go to "User Profiles" and set role (customer/admin)

### Configuration (Optional)

#### OpenWeather API Setup

1. Get free API key from https://openweathermap.org/api
2. Open `carwash/settings.py`
3. Update:
   ```python
   OPENWEATHER_API_KEY = 'your_api_key_here'
   OPENWEATHER_CITY = 'Manila'  # or your city
   ```

OR create a `.env` file:
```
OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_CITY=Manila
```

### Testing the Application

#### 1. Test User Flow
1. Register a new customer account
2. Login as customer
3. Create a booking
4. View dashboard
5. View booking details

#### 2. Test Admin Flow
1. Login with admin account
2. Go to Admin Dashboard
3. View all bookings
4. Update booking status
5. Use filters and search

#### 3. Test Django Admin Panel
1. Go to http://localhost:8000/admin
2. Login with superuser
3. Manage users, profiles, bookings
4. Try bulk actions

### Project Features

✅ **User Registration & Login** - Django built-in authentication
✅ **User Dashboard** - View personal bookings
✅ **Create Bookings** - Book car wash services
✅ **Weather Integration** - Real-time weather data
✅ **Admin Dashboard** - Manage all bookings
✅ **Role-based Access** - Customer vs Admin permissions
✅ **SQLite Database** - No external database needed
✅ **Responsive Design** - Dark theme UI

### Database Schema

The application uses these models:

**UserProfile**
- Links to Django User
- Stores: phone, role (customer/admin)

**Booking**
- Stores: customer info, vehicle info, service details
- Weather data, notes, timestamps
- Status tracking (pending, confirmed, in-progress, completed, cancelled)

### Common Issues & Solutions

#### "No such table" error
```bash
python manage.py migrate
```

#### "No module named bookings"
```bash
python manage.py makemigrations bookings
python manage.py migrate
```

#### Port already in use
```bash
python manage.py runserver 8080
```
(Use different port)

#### Admin role not working
Make sure to set profile.role = 'admin' via Django shell or admin panel

#### Weather not showing
Check OPENWEATHER_API_KEY in settings.py

### Stopping the Server

Press `Ctrl+C` in the terminal running the server.

### Deactivating Virtual Environment

```bash
deactivate
```

### Next Steps

1. **Customize**: Edit templates in `templates/bookings/`
2. **Add Features**: Extend models in `bookings/models.py`
3. **Deploy**: Follow deployment guide in README.md
4. **Test**: Create multiple bookings and test workflows

### File Structure Reference

```
django_carwash/
├── db.sqlite3              # Database (auto-created)
├── manage.py               # Management script
├── requirements.txt        # Dependencies
├── carwash/               # Project settings
│   ├── settings.py        # Main configuration
│   └── urls.py            # URL routing
├── bookings/              # Main app
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── urls.py            # App URLs
│   ├── forms.py           # Forms
│   └── admin.py           # Admin config
└── templates/             # HTML templates
    └── bookings/
```

### Development Workflow

1. Activate virtual environment: `venv\Scripts\activate`
2. Make code changes
3. Create migrations if models changed: `python manage.py makemigrations`
4. Apply migrations: `python manage.py migrate`
5. Test changes: `python manage.py runserver`
6. Deactivate when done: `deactivate`

### Production Checklist

Before deploying:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Add your domain to `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Run `python manage.py collectstatic`
- [ ] Set up proper SECRET_KEY
- [ ] Configure database backups
- [ ] Set up HTTPS/SSL
- [ ] Test all features in production mode

### Support & Resources

- **Django Docs**: https://docs.djangoproject.com/
- **Django Tutorial**: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
- **Python Docs**: https://docs.python.org/3/

---

## Quick Reference Commands

```bash
# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Check for issues
python manage.py check
```

Good luck with your Django Car Wash System! 🚗💧
