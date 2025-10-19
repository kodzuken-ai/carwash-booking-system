# ⚡ Railway Quick Start - 10 Minutes

Deploy your Car Wash System to Railway in 10 minutes!

---

## ✅ Prerequisites

- GitHub account
- Railway account (sign up with GitHub at [railway.app](https://railway.app))
- Git installed on your computer

---

## 🚀 Deployment Steps

### 1. Push to GitHub (3 min)

```bash
# Navigate to project
cd C:\Users\Admin\Desktop\carwash\django_carwash

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Railway deployment"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR-USERNAME/carwash.git
git branch -M main
git push -u origin main
```

---

### 2. Deploy on Railway (5 min)

1. Go to [railway.app](https://railway.app)
2. Login with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your repository
6. Click **"New"** → **"Database"** → **"Add PostgreSQL"**

---

### 3. Set Environment Variables (2 min)

Click on your service → **Variables** tab → Add:

```env
SECRET_KEY=get-from-https://djecrety.ir/
DEBUG=False
ALLOWED_HOSTS=*
```

**Optional** (for email & weather):
```env
EMAILJS_SERVICE_ID=service_wsiw595
EMAILJS_TEMPLATE_ID=template_9so55vi
EMAILJS_PUBLIC_KEY=QolSZZr4vcCVvE2dE
OPENWEATHER_API_KEY=341afd36bea135c9d90515989145e4e4
```

---

### 4. Get Your URL

1. Go to **Settings** tab
2. Click **"Generate Domain"**
3. You'll get: `https://your-app.up.railway.app`

---

### 5. Create Admin User

**Install Railway CLI:**
```bash
npm i -g @railway/cli
```

**Create superuser:**
```bash
railway login
railway link
railway run python manage.py createsuperuser
```

---

## ✅ Done!

Visit your site: `https://your-app.up.railway.app`

Admin panel: `https://your-app.up.railway.app/admin`

---

## 🆘 Issues?

**500 Error?**
- Check logs in Railway dashboard
- Verify SECRET_KEY is set

**No CSS?**
- Already configured! Should work automatically

**Can't create admin?**
- Use Railway CLI method above

---

For detailed guide, see [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md)
