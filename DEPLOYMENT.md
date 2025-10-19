# 🚀 Quick Deployment Guide

## Choose Your Platform

### 🎯 Recommended: Railway
**Best for: Most users, easiest setup**

1. Push code to GitHub
2. Visit [railway.app](https://railway.app)
3. "New Project" → "Deploy from GitHub"
4. Add PostgreSQL database
5. Add environment variables
6. Deploy!

**Cost**: $5 free credit/month

---

### 🎨 Alternative: Render
**Best for: Always-on free apps**

1. Push code to GitHub
2. Visit [render.com](https://render.com)
3. "New" → "Web Service"
4. Connect repository
5. Render auto-detects settings from `render.yaml`
6. Deploy!

**Cost**: Free forever (750 hrs/month)

---

### 🐍 Beginner Friendly: PythonAnywhere
**Best for: Simple, no GitHub needed**

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload code or git clone
3. Create virtual environment
4. Configure web app in dashboard
5. Run migrations
6. Done!

**Cost**: Always free

---

## 📋 Before You Deploy - Checklist

Make sure these files exist:

- ✅ `requirements.txt` - List of Python packages
- ✅ `Procfile` - Tells server how to run your app
- ✅ `runtime.txt` - Specifies Python version  
- ✅ `.gitignore` - Excludes sensitive files from Git
- ✅ `render.yaml` (for Render only)

---

## 🔐 Environment Variables You Need

### Required:
```
SECRET_KEY = your-django-secret-key
DEBUG = False
DATABASE_URL = (provided by platform)
ALLOWED_HOSTS = *.railway.app (or your domain)
```

### Optional (EmailJS):
```
EMAILJS_PUBLIC_KEY = your-key
EMAILJS_SERVICE_ID = your-service-id
EMAILJS_TEMPLATE_ID = your-template-id
```

### Optional (Weather):
```
OPENWEATHER_API_KEY = your-api-key
OPENWEATHER_CITY = Iligan City
```

---

## 🎬 After Deployment

### 1. Check if site is live
Visit your deployment URL

### 2. Run migrations (if needed)
Most platforms auto-run, but check logs

### 3. Create admin user
Use platform's terminal or management command

### 4. Test the system
- Register a user
- Book an appointment
- Login as admin
- Confirm booking

### 5. Monitor
Check platform dashboard for errors

---

## 🆘 Common Issues & Fixes

### "Application Error" or 500 Error
**Solution**: Check logs in platform dashboard
- Verify all environment variables are set
- Check `ALLOWED_HOSTS` includes your domain
- Ensure `DEBUG = False`

### Static files not loading (CSS/JS missing)
**Solution**:
```bash
python manage.py collectstatic --noinput
```
Or add to build command

### Database connection failed
**Solution**:
- Verify PostgreSQL is provisioned
- Check `DATABASE_URL` environment variable
- Wait for database to finish provisioning

### Module not found
**Solution**:
- Add missing package to `requirements.txt`
- Trigger rebuild/redeploy

---

## 📱 Access Your Live App

After deployment, you'll get URLs like:

- Railway: `https://your-app.railway.app`
- Render: `https://carwash-system.onrender.com`
- PythonAnywhere: `https://yourusername.pythonanywhere.com`

---

## 💡 Pro Tips

1. **Use Railway for quick testing** - $5 credit lasts a while
2. **Use Render for permanent free hosting** - Sleeps after 15 min inactive
3. **Use environment variables for ALL secrets** - Never commit API keys
4. **Monitor your app** - Check logs regularly
5. **Backup your database** - Export data periodically

---

## 🔗 Quick Links

- [Full README](./README.md) - Complete documentation
- [Railway](https://railway.app) - Recommended platform
- [Render](https://render.com) - Free alternative
- [PythonAnywhere](https://www.pythonanywhere.com) - Beginner friendly
- [Generate SECRET_KEY](https://djecrety.ir/) - For Django

---

## 🎓 First Time Deploying?

### Start with Railway:

1. Create GitHub account (if needed)
2. Push your code to GitHub
3. Sign up for Railway with GitHub
4. Click "New Project" → "Deploy from GitHub"
5. Select your repository
6. Railway handles everything automatically!
7. Add environment variables in dashboard
8. Visit your live site!

**That's it!** Your car wash system is now online! 🎉

---

Need help? Check the full [README.md](./README.md) for detailed instructions.
