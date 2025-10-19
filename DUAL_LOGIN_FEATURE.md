# Dual Login Feature - Username OR Email

The login system now supports **both username and email** authentication!

---

## ✅ How It Works

### **Login with Email**
- Uses **Supabase authentication**
- Cloud-based, with email verification
- Example: `admin@carwash.com`

### **Login with Username**
- Uses **Django authentication**
- Local database authentication
- Example: `admin`

---

## 🔍 Smart Detection

The system automatically detects the input type:

```python
if '@' in username_or_email:
    # Email detected → Use Supabase auth
else:
    # Username detected → Use Django auth
```

---

## 📝 Changes Made

### **1. Template Updated**
**File**: `templates/bookings/login.html`

**Before:**
```html
<label for="email">Email Address</label>
<input type="email" id="email" name="email" ...>
```

**After:**
```html
<label for="username_or_email">Username or Email</label>
<input type="text" id="username_or_email" name="username_or_email" ...>
```

---

### **2. Login View Updated**
**File**: `bookings/views.py`

**New Logic:**
1. Get `username_or_email` from form
2. Check if it contains `@`
3. **If email**: Use Supabase authentication
4. **If username**: Use Django authentication
5. Both methods log the user into Django session

---

## 🎯 Use Cases

### **For Email Users (Supabase)**
- Register via `/register/`
- Receive email verification
- Login with: `user@example.com`
- Benefits: Cloud auth, password reset, email verification

### **For Username Users (Django)**
- Created via Django admin or `createsuperuser`
- Login with: `admin`
- Benefits: Local control, admin access

---

## 💡 Example Logins

| Input Type | Example | Auth Method |
|------------|---------|-------------|
| **Email** | `john@carwash.com` | Supabase |
| **Email** | `admin@example.com` | Supabase |
| **Username** | `admin` | Django |
| **Username** | `john_doe` | Django |

---

## 🔐 Security Features

✅ Both methods are secure  
✅ Passwords are hashed  
✅ Session management included  
✅ CSRF protection enabled  
✅ Supabase uses JWT tokens  
✅ Django uses session cookies  

---

## 🧪 Testing

### Test Email Login:
1. Register at `/register/`
2. Use email: `test@example.com`
3. Login with: `test@example.com` + password
4. ✅ Should login via Supabase

### Test Username Login:
1. Create superuser: `python manage.py createsuperuser`
2. Username: `admin`
3. Login with: `admin` + password
4. ✅ Should login via Django

---

## 📊 Authentication Flow

```
User Input: "admin@test.com"
    ↓
Contains "@"? YES
    ↓
Use Supabase Auth
    ↓
Valid? YES
    ↓
Create/Update Django User
    ↓
Login Success!

---

User Input: "admin"
    ↓
Contains "@"? NO
    ↓
Use Django Auth
    ↓
Valid? YES
    ↓
Login Success!
```

---

## ⚙️ Technical Details

### **Form Field:**
- Type: `text` (not `email` anymore)
- Name: `username_or_email`
- Required: Yes
- Placeholder: "username or email@example.com"

### **Backend Logic:**
- Checks for `@` character
- Email → Supabase API call
- Username → Django `authenticate()` function
- Both → Django `login()` for session

---

## 🎉 Benefits

1. **Flexibility** - Users choose their preferred login method
2. **Backward Compatible** - Existing Django users can still login
3. **Modern Auth** - Supabase provides email verification
4. **Admin Access** - Superusers can login with username
5. **User Friendly** - Single input field for both methods

---

## 🚀 Ready to Use!

The dual login system is now active. Users can login with:
- ✅ Email address (Supabase)
- ✅ Username (Django)

**Try it at:** http://localhost:8000/login/
