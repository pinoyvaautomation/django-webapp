# Render Deployment - Quick Reference

## 🚀 Fresh Deployment (5 Minutes)

### 1. Render Setup
1. Go to [render.com](https://render.com) → New → Web Service
2. Connect GitHub repo → Select your Django project
3. **Settings**:
   - Build Command: `./build.sh`
   - Start Command: `gunicorn prjsystem.wsgi:application`
   - Environment: Python 3

### 2. Environment Variables
**Required** (Add in Render Dashboard > Environment):
```
SECRET_KEY = your-secret-key-here
DEBUG = False
RENDER = True
```

### 3. Deploy
Click "Create Web Service" - Render will automatically build and deploy.

---

## 🔄 Update Deployment (30 Seconds)

### Automatic (Recommended)
```bash
git add .
git commit -m "Update message"
git push origin main
# Auto-deploys if enabled
```

### Manual
1. Render Dashboard → Your Service
2. "Manual Deploy" → "Deploy latest commit"

---

## 🐛 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails | Check logs, update `requirements.txt` |
| Static files 404 | Already configured with WhiteNoise ✅ |
| App won't start | Verify environment variables set |
| Database errors | Check migration logs, may need `python manage.py migrate --run-syncdb` |

---

## 📋 Pre-Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` updated
- [ ] Environment variables configured
- [ ] `DEBUG = False` in production
- [ ] Test locally before deploying

---

## 🔗 Quick Links
- **Your App**: `https://your-service-name.onrender.com`
- **Admin**: `https://your-service-name.onrender.com/admin/`
- **Render Dashboard**: [dashboard.render.com](https://dashboard.render.com)

---
*For detailed instructions, see [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md)* 