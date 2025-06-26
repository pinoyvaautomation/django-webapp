# Django Project Deployment on Render

This guide provides step-by-step instructions for deploying your Django project (`prjsystem`) on [Render](https://render.com), a modern cloud platform that offers free and paid hosting options.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Project Overview](#project-overview)
- [Fresh Deployment](#fresh-deployment)
- [Environment Variables Configuration](#environment-variables-configuration)
- [Database Setup](#database-setup)
- [Update/Redeploy Process](#updateredeploy-process)
- [Troubleshooting](#troubleshooting)
- [Production Considerations](#production-considerations)
- [Monitoring and Maintenance](#monitoring-and-maintenance)

## 🔧 Prerequisites

Before starting the deployment process, ensure you have:

1. **Render Account**: Sign up at [render.com](https://render.com)
2. **GitHub Repository**: Your Django project code should be in a GitHub repository
3. **Project Dependencies**: Verify all required files are present:
   - `requirements.txt` ✅
   - `build.sh` ✅
   - `Procfile` ✅
   - Django settings configured for production ✅

## 📊 Project Overview

Your Django project includes:
- **Framework**: Django 5.2.3
- **Apps**: articles, download_library, inventory, shop
- **Admin Interface**: Django Jazzmin
- **Rich Text Editor**: CKEditor with file upload support
- **Static Files**: WhiteNoise middleware
- **WSGI Server**: Gunicorn
- **Database**: SQLite (default) with PostgreSQL support ready

## 🚀 Fresh Deployment

### Step 1: Prepare Your Repository

1. **Push your code to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Verify deployment files**:
   - `requirements.txt` - Contains all Python dependencies
   - `build.sh` - Build script for Render
   - `Procfile` - Defines how to run your application

### Step 2: Create a New Web Service on Render

1. **Login to Render Dashboard**
   - Go to [render.com](https://render.com) and sign in

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select your Django project repository

3. **Configure Basic Settings**
   - **Name**: Choose a unique name (e.g., `my-django-app`)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your deployment branch)

4. **Configure Build & Deploy Settings**
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn prjsystem.wsgi:application`
   - **Plan**: Choose Free or paid plan based on your needs

### Step 3: Advanced Settings

In the Advanced section:

- **Auto-Deploy**: Enable for automatic deployments on git push
- **Health Check Path**: `/admin/` (optional)

## 🔐 Environment Variables Configuration

Set up the following environment variables in Render Dashboard:

### Required Environment Variables

1. **SECRET_KEY**
   ```
   Key: SECRET_KEY
   Value: your-super-secret-django-key-here
   ```
   *Generate a secure key using Django's `get_random_secret_key()`*

2. **DEBUG**
   ```
   Key: DEBUG
   Value: False
   ```

3. **RENDER**
   ```
   Key: RENDER
   Value: True
   ```

### Optional Environment Variables

4. **DJANGO_SETTINGS_MODULE** (if using custom settings)
   ```
   Key: DJANGO_SETTINGS_MODULE
   Value: prjsystem.settings
   ```

### How to Add Environment Variables

1. Go to your Web Service dashboard on Render
2. Click on "Environment" tab
3. Click "Add Environment Variable"
4. Enter the key-value pairs listed above
5. Click "Save Changes"

## 🗄️ Database Setup

### Option 1: SQLite (Default - Suitable for small projects)

Your project is configured to use SQLite by default, which works well for development and small production apps. No additional database setup required.

### Option 2: PostgreSQL (Recommended for Production)

For production applications, consider upgrading to PostgreSQL:

1. **Create PostgreSQL Database on Render**
   - In Render Dashboard, click "New" → "PostgreSQL"
   - Choose your plan (Free tier available)
   - Note the connection details

2. **Update Django Settings**
   Add to your `settings.py`:
   ```python
   import dj_database_url
   
   # Add to requirements.txt: dj-database-url
   if 'DATABASE_URL' in os.environ:
       DATABASES = {
           'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
       }
   ```

3. **Add Database Environment Variable**
   ```
   Key: DATABASE_URL
   Value: [Your PostgreSQL connection string from Render]
   ```

## 🔄 Update/Redeploy Process

### Automatic Deployment (Recommended)

With Auto-Deploy enabled, your app redeploys automatically when you push to your main branch:

```bash
# Make your changes
git add .
git commit -m "Your update message"
git push origin main
# Render will automatically start deployment
```

### Manual Deployment

1. Go to your Web Service on Render Dashboard
2. Click "Manual Deploy" → "Deploy latest commit"
3. Or choose "Clear build cache & deploy" for a fresh build

### Deployment Monitoring

- Monitor deployment logs in Render Dashboard
- Check the "Events" tab for deployment status
- View application logs in the "Logs" tab

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Build Fails - Dependencies Issue
```
Error: Could not find a version that satisfies the requirement
```
**Solution**: Update `requirements.txt` with specific versions:
```bash
pip freeze > requirements.txt
```

#### 2. Static Files Not Loading
**Symptoms**: CSS/JS files return 404 errors

**Solution**: Ensure WhiteNoise is properly configured (already done in your project):
```python
# In settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be here
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### 3. Database Migration Issues
```bash
# Force migrate during deployment
python manage.py migrate --run-syncdb
```

#### 4. Media Files Not Accessible
For production, consider using:
- **Cloudinary** for image hosting
- **AWS S3** for file storage
- **Render's Persistent Disk** (paid plans)

#### 5. Application Won't Start
**Check logs for common issues**:
- Missing environment variables
- Database connection problems
- Import errors

**Debug steps**:
1. Check Render logs in Dashboard
2. Verify all environment variables are set
3. Ensure `Procfile` command is correct: `web: gunicorn prjsystem.wsgi`

## 🏭 Production Considerations

### Security Checklist

- [ ] `DEBUG = False` in production
- [ ] Strong `SECRET_KEY` set via environment variable
- [ ] `ALLOWED_HOSTS` properly configured
- [ ] HTTPS enabled (automatic on Render)
- [ ] Database backups configured (for PostgreSQL)

### Performance Optimization

1. **Static Files Compression**
   ```python
   # Already configured in your project
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

2. **Database Optimization**
   - Use PostgreSQL for better performance
   - Add database indexes to frequently queried fields
   - Consider connection pooling for high traffic

3. **Caching Strategy**
   ```python
   # Add to settings.py for Redis caching
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': os.environ.get('REDIS_URL'),
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }
   ```

### Monitoring Setup

1. **Health Checks**
   - Create a health check endpoint in Django
   - Configure in Render's Health Check Path

2. **Error Tracking**
   - Consider integrating Sentry for error monitoring
   - Set up logging for application monitoring

## 📊 Monitoring and Maintenance

### Regular Maintenance Tasks

1. **Monitor Application Logs**
   - Check Render Dashboard logs regularly
   - Set up alerts for critical errors

2. **Database Maintenance**
   - Regular backups (automatic with Render PostgreSQL)
   - Monitor database size and performance

3. **Security Updates**
   - Keep Django and dependencies updated
   - Monitor for security advisories

4. **Performance Monitoring**
   - Monitor response times
   - Check resource usage (CPU, memory)

### Scaling Considerations

1. **Vertical Scaling**: Upgrade Render plan for more resources
2. **Horizontal Scaling**: Use Render's autoscaling features (paid plans)
3. **Database Scaling**: Upgrade PostgreSQL plan as needed

## 🔗 Useful Links

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/configure.html)

## 📞 Support

If you encounter issues:
1. Check Render's status page
2. Review deployment logs carefully
3. Consult Django and Render documentation
4. Consider upgrading to a paid plan for priority support

---

**Last Updated**: [Current Date]
**Django Version**: 5.2.3
**Python Version**: 3.x
**Render Platform**: Web Services 