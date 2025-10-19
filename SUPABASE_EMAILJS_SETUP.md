# Supabase Auth & EmailJS Integration Guide

## ✅ What Was Added

Your Django project now includes:

1. **Supabase Authentication** - Cloud-based auth with email verification
2. **EmailJS Integration** - Contact form email functionality
3. **Hybrid Auth System** - Both Django auth AND Supabase auth available

---

## 📦 New Dependencies

```
supabase==2.3.0
python-dotenv==1.0.0
```

---

## 🔑 API Configurations

All API keys are configured in:
- **File**: `carwash/settings.py` (lines 129-141)
- **Environment**: `.env.example` (template)

### Your Current API Keys:

**Supabase:**
- URL: `https://ruxzlgrsiaepnnczfujh.supabase.co`
- Anon Key: Already configured
- Service Role Key: Already configured

**EmailJS:**
- Service ID: `service_wsiw595`
- Template ID: `template_9so55vi`
- Public Key: `QolSZZr4vcCVvE2dE`

**OpenWeather:**
- API Key: `341afd36bea135c9d90515989145e4e4`
- City: `Iligan City`

---

## 🚀 Setup Instructions

### Step 1: Install New Dependencies

```bash
cd django_carwash
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This adds the `supabase_id` field to UserProfile model.

### Step 3: Start the Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication Options

You now have **TWO authentication systems**:

### Option 1: Supabase Auth (Recommended)
- **Register**: http://localhost:8000/supabase/register/
- **Login**: http://localhost:8000/supabase/login/
- **Features**: Email verification, password reset, cloud storage

### Option 2: Django Auth (Original)
- **Register**: http://localhost:8000/register/
- **Login**: http://localhost:8000/login/
- **Features**: Local auth, no email verification

**Default Navigation**: Now shows Supabase auth links

---

## 📧 EmailJS Contact Form

### Access Contact Page:
http://localhost:8000/contact/

### How It Works:
1. User fills out contact form
2. EmailJS sends email to your configured address
3. No backend email server needed
4. Works from browser (frontend)

---

## 🗂️ New Files Created

```
django_carwash/
├── requirements.txt                          # Updated with new packages
├── .env.example                              # Updated with all API keys
│
├── carwash/
│   └── settings.py                           # Added Supabase & EmailJS config
│
├── bookings/
│   ├── models.py                             # Added supabase_id field
│   ├── urls.py                               # Added Supabase auth routes
│   ├── auth_views.py                         # NEW - Supabase authentication views
│   ├── supabase_client.py                    # NEW - Supabase client config
│   ├── context_processors.py                 # NEW - Settings in templates
│   └── views.py                              # Added contact view
│
└── templates/
    ├── base.html                             # Added EmailJS SDK
    └── bookings/
        ├── login_supabase.html               # NEW - Supabase login
        ├── register_supabase.html            # NEW - Supabase register
        ├── password_reset.html               # NEW - Password reset
        └── contact.html                      # NEW - EmailJS contact form
```

---

## 🎯 How to Use Supabase Auth

### 1. Register New User

Visit: http://localhost:8000/supabase/register/

- Enter email, password, name, phone
- User created in Supabase cloud
- Email verification sent automatically
- User created in local Django database
- UserProfile stores Supabase UUID

### 2. Login

Visit: http://localhost:8000/supabase/login/

- Enter email and password
- Authenticated via Supabase
- Django session created
- Access all app features

### 3. Password Reset

Visit: http://localhost:8000/password-reset/

- Enter email
- Supabase sends reset link
- User can reset password

---

## 📨 How to Use EmailJS

### 1. Send Test Email

Visit: http://localhost:8000/contact/

- Fill out contact form
- Click "Send Message"
- Email sent via EmailJS
- No backend configuration needed

### 2. Configure EmailJS (Optional)

If you want to use your own EmailJS account:

1. Create account at https://www.emailjs.com/
2. Create email service
3. Create email template
4. Get your API keys
5. Update in `settings.py` or `.env` file

---

## 🔧 Configuration Files

### settings.py
```python
# Supabase Configuration
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://...')
SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY', '...')
SUPABASE_SERVICE_ROLE_KEY = os.environ.get('SUPABASE_SERVICE_ROLE_KEY', '...')

# EmailJS Configuration
EMAILJS_SERVICE_ID = os.environ.get('EMAILJS_SERVICE_ID', 'service_...')
EMAILJS_TEMPLATE_ID = os.environ.get('EMAILJS_TEMPLATE_ID', 'template_...')
EMAILJS_PUBLIC_KEY = os.environ.get('EMAILJS_PUBLIC_KEY', '...')
```

---

## 🔄 Switching Between Auth Systems

### Default (Supabase):
Navigation shows: "🔐 Supabase Login" and "🚀 Supabase Sign Up"

### To Use Django Auth:
Edit `templates/base.html` line 323-324:
```html
<li><a href="{% url 'login' %}">Login</a></li>
<li><a href="{% url 'register' %}">Register</a></li>
```

### Both Are Available:
- Django: `/login/`, `/register/`
- Supabase: `/supabase/login/`, `/supabase/register/`

---

## 🧪 Testing

### Test Supabase Registration:
```bash
1. Go to http://localhost:8000/supabase/register/
2. Register with real email
3. Check email for verification link
4. Click verification link
5. Login at http://localhost:8000/supabase/login/
```

### Test EmailJS:
```bash
1. Go to http://localhost:8000/contact/
2. Fill out form
3. Click "Send Message"
4. Check configured email inbox
```

---

## 🗄️ Database Changes

### UserProfile Model:
Added new field:
```python
supabase_id = models.CharField(max_length=255, blank=True, null=True)
```

This stores the Supabase User UUID for linking.

---

## 🌐 URLs Available

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/contact/` | Contact form (EmailJS) |
| `/login/` | Django login |
| `/register/` | Django registration |
| `/supabase/login/` | Supabase login |
| `/supabase/register/` | Supabase registration |
| `/password-reset/` | Password reset |
| `/dashboard/` | User dashboard |
| `/admin-dashboard/` | Admin dashboard |

---

## ⚡ Quick Start Commands

```bash
# Navigate to project
cd C:\Users\Admin\Desktop\carwash\django_carwash

# Activate virtual environment
venv\Scripts\activate

# Install new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver

# Open browser
# Supabase Login: http://localhost:8000/supabase/login/
# Contact Form: http://localhost:8000/contact/
```

---

## 📝 Notes

### Supabase:
- ✅ Cloud-hosted authentication
- ✅ Email verification automatic
- ✅ Password reset built-in
- ✅ User data stored in Supabase + local SQLite
- ✅ JWT tokens for sessions

### EmailJS:
- ✅ Frontend email sending
- ✅ No backend SMTP configuration
- ✅ Works in browser
- ✅ Free tier: 200 emails/month

### Both Systems:
- ✅ Can coexist
- ✅ Can switch between them
- ✅ Users can login with either
- ✅ Data syncs to local database

---

## 🐛 Troubleshooting

### "No module named 'supabase'"
```bash
pip install -r requirements.txt
```

### "UserProfile has no column named supabase_id"
```bash
python manage.py makemigrations
python manage.py migrate
```

### EmailJS not working
- Check browser console for errors
- Verify EmailJS API keys in settings.py
- Check EmailJS dashboard for quota

### Supabase auth not working
- Check Supabase dashboard
- Verify API keys in settings.py
- Check if email verification is enabled in Supabase

---

## ✅ Success Checklist

- [ ] Installed new dependencies
- [ ] Ran database migrations
- [ ] Server starts without errors
- [ ] Can access Supabase registration page
- [ ] Can access contact form
- [ ] EmailJS script loads in browser
- [ ] Supabase client initializes successfully

---

## 🎉 You're All Set!

Your Django project now has:
- ✅ Supabase cloud authentication
- ✅ EmailJS contact form
- ✅ Dual auth system (Django + Supabase)
- ✅ Email verification
- ✅ Password reset
- ✅ All previous features working

**Test it out and enjoy!** 🚀
