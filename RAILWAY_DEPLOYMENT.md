# 🚀 Deploy Car Wash System on Railway - Complete Guide

Deploy your Django Car Wash Booking System on Railway in **10 minutes** for **FREE**!

---

## ✨ Why Railway?

- ✅ **$5 free credit/month** - Enough for small to medium apps
- ✅ **PostgreSQL included** - Free database, better than SQLite
- ✅ **Auto-deploy from GitHub** - Push code = automatic deployment
- ✅ **Free SSL certificate** - HTTPS included
- ✅ **Built for Django** - Perfect for Python apps
- ✅ **Zero configuration** - Works out of the box

---

## 📋 What You'll Get

After deployment:
- 🌐 Live website with custom Railway URL
- 🗄️ PostgreSQL database (automatically created)
- 🔒 HTTPS/SSL certificate
- 📧 Email notifications working (EmailJS)
- 👤 Admin panel accessible
- 📱 Fully functional booking system

---

## 🎯 Prerequisites

Before starting, make sure you have:

- ✅ GitHub account ([Sign up](https://github.com/signup) if needed)
- ✅ Railway account ([Sign up](https://railway.app) - use GitHub to sign in)
- ✅ Your code ready (you have this!)
- ✅ Git installed on your computer

---

## 📦 Step 1: Prepare Your Project (Already Done! ✅)

Your project is **already configured** for Railway deployment with:

### ✅ Files Created:
- `Procfile` - Tells Railway how to run your app
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists all dependencies
- `settings.py` - Configured for PostgreSQL

### ✅ Settings Updated:
- Database: Auto-switches to PostgreSQL on Railway
- Static files: WhiteNoise configured
- Environment variables: Ready for production
- Debug mode: Auto-disabled in production

**You can skip to Step 2!** 🎉

---

## 📤 Step 2: Push Your Code to GitHub

### If you haven't created a GitHub repository yet:

#### 1. Create Repository on GitHub:

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `carwash-booking-system` (or any name)
3. Description: `Django Car Wash Booking System`
4. Set to **Public** or **Private** (your choice)
5. **Don't** check "Add README" (you already have one)
6. Click **Create repository**

#### 2. Push Your Code:

Open terminal/command prompt in your project folder:

```bash
# Navigate to your project
cd C:\Users\Admin\Desktop\carwash\django_carwash

# Initialize git (if not done already)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Railway deployment"

# Add your GitHub repository (replace with your URL)
git remote add origin https://github.com/YOUR-USERNAME/carwash-booking-system.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Important**: Replace `YOUR-USERNAME` with your actual GitHub username!

### If you already have a GitHub repository:

```bash
cd C:\Users\Admin\Desktop\carwash\django_carwash
git add .
git commit -m "Configure for Railway deployment"
git push
```

---

## 🚂 Step 3: Deploy on Railway (5 minutes)

### 1. Sign Up / Login to Railway:

1. Go to [railway.app](https://railway.app)
2. Click **Login with GitHub**
3. Authorize Railway to access your GitHub

### 2. Create New Project:

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your repository: `carwash-booking-system`
4. Railway will automatically detect it's a Django app!

### 3. Add PostgreSQL Database:

1. In your project dashboard, click **"New"**
2. Select **"Database"**
3. Choose **"Add PostgreSQL"**
4. PostgreSQL will be provisioned automatically
5. Railway auto-connects it to your app! ✅

---

## ⚙️ Step 4: Configure Environment Variables

### In Railway Dashboard:

1. Click on your **web service** (the one with your app name)
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add these variables:

### Required Variables:

```env
SECRET_KEY=django-insecure-YOUR-RANDOM-SECRET-KEY-HERE
DEBUG=False
ALLOWED_HOSTS=*
```

### Optional Variables (for features):

```env
# Weather API (optional)
OPENWEATHER_API_KEY=341afd36bea135c9d90515989145e4e4
OPENWEATHER_CITY=Iligan City

# EmailJS (optional - for booking confirmations)
EMAILJS_SERVICE_ID=service_wsiw595
EMAILJS_TEMPLATE_ID=template_9so55vi
EMAILJS_PUBLIC_KEY=QolSZZr4vcCVvE2dE
```

### Generate a Secure SECRET_KEY:

**Option 1: Online Generator**
- Visit: [djecrety.ir](https://djecrety.ir/)
- Copy the generated key
- Paste as `SECRET_KEY` value

**Option 2: Python Command**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Save all variables!**

---

## 🎬 Step 5: Deploy & Wait

### Railway will automatically:

1. ✅ Install Python 3.11
2. ✅ Install dependencies from `requirements.txt`
3. ✅ Run migrations (`python manage.py migrate`)
4. ✅ Collect static files (`python manage.py collectstatic`)
5. ✅ Start gunicorn server

### Watch the deployment:

- Click **"Deployments"** tab
- Watch the build logs
- Wait for **"Success"** status (2-3 minutes)

---

## 🌐 Step 6: Access Your Live Site!

### Get your URL:

1. In Railway dashboard, click **"Settings"** tab
2. Under **"Domains"** section
3. Click **"Generate Domain"**
4. You'll get a URL like: `https://carwash-production-abc123.up.railway.app`

### Visit your site:

Click the URL or copy-paste into browser!

**Your Car Wash System is now LIVE!** 🎉

---

## 👤 Step 7: Create Admin User

You need to create a superuser to access the admin panel.

### Using Railway CLI (Recommended):

#### Install Railway CLI:

```bash
# Windows (using npm)
npm i -g @railway/cli

# Or download from railway.app/cli
```

#### Create superuser:

```bash
# Login to Railway
railway login

# Link to your project
railway link

# Run Django command
railway run python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Alternative: Using Railway Dashboard:

1. Go to your project in Railway
2. Click on your **web service**
3. Go to **"Settings"** → **"Service"**
4. Scroll to **"Custom Start Command"**
5. Temporarily change to:
   ```
   python manage.py migrate && python manage.py createsuperuser --noinput && gunicorn carwash.wsgi
   ```
6. This won't work perfectly, but you can use the Railway shell

**Easiest way**: Use Railway CLI above!

---

## ✅ Step 8: Test Everything

### 1. Homepage:
```
https://your-app.up.railway.app
```
Should show your car wash homepage ✅

### 2. Admin Panel:
```
https://your-app.up.railway.app/admin
```
Login with superuser credentials ✅

### 3. Create a Test Booking:

1. Register a new user
2. Browse services
3. Create a booking
4. Check if email confirmation works
5. Login as admin
6. Verify booking appears in dashboard

---

## 🔧 Maintenance & Updates

### Update Your App:

Whenever you make changes:

```bash
# Make your changes locally
# Then push to GitHub
git add .
git commit -m "Description of changes"
git push
```

**Railway automatically redeploys!** 🚀

### View Logs:

1. Railway Dashboard → Your service
2. Click **"Deployments"**
3. Click on latest deployment
4. View build and runtime logs

### Database Backup:

Railway provides automatic backups, but you can also:

```bash
railway run python manage.py dumpdata > backup.json
```

---

## 🆘 Troubleshooting

### Issue 1: "Application Error" or 500 Error

**Check:**
1. View logs in Railway dashboard
2. Verify `SECRET_KEY` is set
3. Check `ALLOWED_HOSTS=*` is set
4. Ensure database is connected

**Fix:**
```bash
# Check logs
railway logs

# Verify environment variables
railway variables
```

---

### Issue 2: Static Files Not Loading (No CSS)

**Symptoms**: Site loads but no styling

**Fix:**

1. Check `whitenoise` is in `requirements.txt` ✅ (already added)
2. Verify in `settings.py`:
   ```python
   MIDDLEWARE = [
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be here
       ...
   ]
   ```
3. Trigger rebuild in Railway

---

### Issue 3: Database Connection Error

**Fix:**

1. Verify PostgreSQL is added to project
2. Check `DATABASE_URL` variable exists (Railway adds this automatically)
3. Redeploy the service

---

### Issue 4: Can't Create Superuser

**Fix:**

Use Railway CLI:
```bash
railway login
railway link
railway run python manage.py createsuperuser
```

---

### Issue 5: Module Not Found Error

**Symptoms**: Build fails with "ModuleNotFoundError"

**Fix:**

1. Make sure package is in `requirements.txt`
2. Push changes to GitHub
3. Railway will redeploy automatically

---

## 🎨 Custom Domain (Optional)

### Add Your Own Domain:

1. Railway Dashboard → Settings → Domains
2. Click **"Custom Domain"**
3. Enter your domain: `carwash.yourdomain.com`
4. Add DNS records (Railway will show you):
   ```
   Type: CNAME
   Name: carwash (or @)
   Value: your-app.up.railway.app
   ```
5. Wait for DNS propagation (5-30 minutes)
6. Update `ALLOWED_HOSTS`:
   ```env
   ALLOWED_HOSTS=carwash.yourdomain.com,*.railway.app
   ```

---

## 💰 Railway Pricing & Limits

### Free Tier:
- **$5 credit/month**
- ~500 hours/month runtime
- Perfect for small apps and testing

### When you exceed free tier:
- Railway will charge beyond $5
- You can set spending limits
- Or deploy on Render (always free with limitations)

### Monitor usage:
- Railway Dashboard → Usage
- Check current spend
- Set up billing alerts

---

## 📊 Project URLs Summary

After deployment, you'll have:

| Page | URL |
|------|-----|
| **Homepage** | `https://your-app.up.railway.app` |
| **Services** | `https://your-app.up.railway.app/services` |
| **Login** | `https://your-app.up.railway.app/login` |
| **Register** | `https://your-app.up.railway.app/register` |
| **Admin Panel** | `https://your-app.up.railway.app/admin` |
| **User Dashboard** | `https://your-app.up.railway.app/dashboard` |
| **Create Booking** | `https://your-app.up.railway.app/bookings/create` |

---

## 🎯 Quick Commands Reference

```bash
# Railway CLI Commands
railway login                              # Login to Railway
railway link                               # Link to your project
railway run python manage.py migrate       # Run migrations
railway run python manage.py createsuperuser  # Create admin
railway logs                               # View logs
railway open                               # Open project in browser
railway variables                          # List environment variables

# Git Commands
git add .                                  # Stage changes
git commit -m "message"                    # Commit changes
git push                                   # Deploy to Railway

# Django Commands (via Railway)
railway run python manage.py shell         # Django shell
railway run python manage.py dbshell       # Database shell
railway run python manage.py dumpdata > backup.json  # Backup
```

---

## ✨ Features Available After Deployment

✅ **User Management**
- User registration
- Login/logout
- Role-based access (customer/admin)

✅ **Booking System**
- Browse car wash services
- Create bookings with date/time slots
- Maximum 5 bookings per time slot
- No past date bookings

✅ **Admin Dashboard**
- View all bookings
- Update booking status
- Manage services (CRUD)
- Manage users
- Filter and search

✅ **Email Notifications**
- Booking confirmations (via EmailJS)
- Status updates

✅ **Additional Features**
- Weather integration
- Service duration in hours/minutes
- Responsive design
- Dark theme UI

---

## 🎉 Success Checklist

After deployment, verify:

- [ ] Homepage loads correctly
- [ ] Can register new user
- [ ] Can login successfully
- [ ] Can view services
- [ ] Can create a booking
- [ ] Email confirmation sent
- [ ] Admin panel accessible
- [ ] Can login as admin
- [ ] Admin can see bookings
- [ ] Admin can update status
- [ ] Admin can manage services
- [ ] Static files loading (CSS/JS)
- [ ] No console errors
- [ ] Mobile responsive

---

## 📞 Getting Help

### Railway Support:
- [Railway Docs](https://docs.railway.app/)
- [Railway Discord](https://discord.gg/railway)
- [Railway Community](https://help.railway.app/)

### Django Resources:
- [Django Docs](https://docs.djangoproject.com/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)

### Your Project:
- Check `README.md` for local development
- Check deployment logs in Railway dashboard
- Use Railway CLI for debugging

---

## 🚀 You're Live!

**Congratulations!** Your Django Car Wash Booking System is now deployed and accessible worldwide!

### Next Steps:

1. ✅ Share your live URL with clients
2. ✅ Set up custom domain (optional)
3. ✅ Configure email notifications
4. ✅ Monitor usage in Railway dashboard
5. ✅ Make updates by pushing to GitHub

---

**Your Live App**: `https://your-app.up.railway.app`

**Admin Panel**: `https://your-app.up.railway.app/admin`

**Enjoy your deployed Car Wash System!** 🎊

---

*Need help? Check the troubleshooting section or Railway documentation.*
