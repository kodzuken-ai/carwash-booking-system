# Email Setup Guide for Booking Confirmations

## 📧 Gmail SMTP Configuration

Your car wash system will automatically send booking confirmation emails to customers after they book a service.

---

## 🚀 Setup Steps:

### 1. **Get Gmail App Password**

Since Gmail requires 2-Step Verification for app passwords, follow these steps:

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** (left sidebar)
3. Under "How you sign in to Google", enable **2-Step Verification** (if not already enabled)
4. After enabling 2-Step, go back to Security
5. Scroll to **App passwords** section
6. Click "App passwords"
7. Select:
   - **App**: Mail
   - **Device**: Other (enter "Car Wash Django App")
8. Click **Generate**
9. **Copy the 16-character password** (it looks like: `abcd efgh ijkl mnop`)

---

### 2. **Update .env File**

Create or update your `.env` file in the project root with:

```env
# Email Configuration
EMAIL_HOST_USER=your-gmail-address@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
DEFAULT_FROM_EMAIL=Car Wash Pro <noreply@carwash.com>
```

**Example:**
```env
EMAIL_HOST_USER=carwashpro@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
DEFAULT_FROM_EMAIL=Car Wash Pro <carwashpro@gmail.com>
```

---

### 3. **Test the Email**

1. Start your Django server
2. Create a test booking
3. Check if the confirmation email arrives
4. Check your Gmail "Sent" folder to verify

---

## 📝 Email Template Details

The confirmation email includes:
- ✅ Customer name
- ✅ Service booked
- ✅ Date and time
- ✅ Vehicle details
- ✅ Location
- ✅ Price
- ✅ Professional HTML design
- ✅ Fallback plain text version

---

## 🔧 Troubleshooting

### Email not sending?

1. **Check Gmail App Password**
   - Make sure you copied the full 16-character password
   - No spaces in the password

2. **Check 2-Step Verification**
   - Must be enabled on your Google account

3. **Check Firewall/Network**
   - Port 587 must be open
   - TLS must be allowed

4. **Check Django Logs**
   - Look for error messages in console
   - Check if `EMAIL_HOST_USER` is set correctly

5. **Test with Django Shell**
   ```python
   from django.core.mail import send_mail
   send_mail(
       'Test Subject',
       'Test message',
       'your-email@gmail.com',
       ['recipient@example.com'],
       fail_silently=False,
   )
   ```

---

## 🔒 Security Notes

- ✅ **Never commit** your `.env` file to Git
- ✅ `.env` is already in `.gitignore`
- ✅ Use App Passwords, not your Gmail password
- ✅ App passwords are safer than your main password

---

## 🎨 Customize Email

To customize the email template, edit:
`bookings/emails.py` → `send_booking_confirmation_email()` function

You can change:
- Email subject line
- Company name
- Colors and styling
- Email content
- Footer text

---

## ✅ You're All Set!

Once configured, customers will automatically receive professional booking confirmation emails every time they book a service!

**Email Preview:**
```
Subject: Booking Confirmation - Car Wash Pro

Hi John Doe,

Thank you for booking with Car Wash Pro! Your carwash appointment 
has been successfully confirmed.

BOOKING DETAILS:
Service: Premium Detail
Date & Time: October 20, 2025 at 10:00 AM
Vehicle: Sedan (ABC-123)
Location: Iligan City
Price: ₱85

⚠️ This is a confirmation email only. You do not need to reply.
```

---

**Questions?** Check the Django documentation or contact support!
