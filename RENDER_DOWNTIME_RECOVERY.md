# Render Website Downtime Recovery Guide

## 🚨 When Your Website is Down

If your Django website hosted on Render is not responding or showing errors, follow these steps to quickly restore service.

## 🔧 Quick Recovery Steps

### Step 1: Check Service Status
1. Go to your Render Dashboard
2. Navigate to the **Events** tab/page: [https://dashboard.render.com/web/srv-d1e9kb95pdvs73bqqb80/events](https://dashboard.render.com/web/srv-d1e9kb95pdvs73bqqb80/events)
3. Check recent events for any deployment failures or service issues

### Step 2: Manual Deploy/Restart Service
1. From the Events page, click the **"Manual Deploy"** button
2. **Available Options**:
   - **"Restart service"** ⭐ **KEY OPTION** - Quickly restarts your service (fastest recovery)
   - **"Deploy latest commit"** - Redeploys with current code
   - **"Deploy a specific commit"** - Deploy a previous working version
   - **"Clear build cache & deploy"** - Fresh rebuild (if other options fail)

### Step 3: Monitor Recovery
1. Watch the deployment logs in real-time
2. Wait for deployment to complete (usually 2-5 minutes)
3. Test your website once deployment shows as "Live"

## 🔧 Manual Deploy Options Explained

| Option | When to Use | Speed | Description |
|--------|-------------|-------|-------------|
| **Restart service** ⭐ | Service is stuck/frozen | Fastest (30-60s) | Simply restarts the running service |
| **Deploy latest commit** | After code changes | Medium (2-5 min) | Rebuilds and deploys current code |
| **Deploy a specific commit** | Need to rollback | Medium (2-5 min) | Deploy a previous working version |
| **Clear build cache & deploy** | Build issues persist | Slowest (5-10 min) | Complete fresh rebuild |

## 📊 Common Downtime Scenarios

| Scenario | Best Solution |
|----------|---------------|
| Service sleeping (free tier) | **Restart service** |
| Service frozen/unresponsive | **Restart service** |
| Build failure | Check logs, fix issues, then **Deploy latest commit** |
| Memory/CPU limits exceeded | **Restart service**, consider upgrading plan |
| Database connection issues | **Restart service**, check DB status |
| Environment variable changes | **Deploy latest commit** to apply new settings |

## 🔍 Troubleshooting Checklist

Before manual deployment, check:
- [ ] Recent code changes that might have caused issues
- [ ] Environment variables are properly set
- [ ] No recent Render platform issues (check Render status page)
- [ ] Database service is running (if using external DB)

## ⚡ Emergency Actions

### Immediate Recovery
```
1. Go to: https://dashboard.render.com/web/srv-d1e9kb95pdvs73bqqb80/events
2. Click "Manual Deploy" → "Restart service" ⭐ (FASTEST)
3. Wait for restart completion (usually 30-60 seconds)
4. Test website functionality
```

### If Restart Service Doesn't Work
```
1. Try "Deploy latest commit" (if recent code changes might be the issue)
2. Try "Clear build cache & deploy" (for persistent build issues)
3. Check build logs for specific errors
4. Verify requirements.txt is up to date
5. Check environment variables
6. Use "Deploy a specific commit" to roll back to previous working version
```

## 🔗 Quick Access Links

- **Events Page**: [https://dashboard.render.com/web/srv-d1e9kb95pdvs73bqqb80/events](https://dashboard.render.com/web/srv-d1e9kb95pdvs73bqqb80/events)
- **Service Dashboard**: [https://dashboard.render.com/](https://dashboard.render.com/)
- **Render Status**: [https://status.render.com/](https://status.render.com/)

## 📞 When to Escalate

Contact Render support if:
- Multiple manual deploys fail
- Service shows as "Live" but website still down
- Persistent database connection issues
- Suspected platform-wide issues

## 💡 Prevention Tips

1. **Monitor Regularly**: Check your site periodically
2. **Set Up Alerts**: Use external monitoring services
3. **Test Before Deploy**: Always test changes locally
4. **Keep Backups**: Regular database backups for important data
5. **Consider Paid Plans**: For better uptime and support

---

**📋 Remember**: Most downtime issues on Render can be resolved with the **"Restart service"** option - it's the fastest way to get your website back online! Keep this guide bookmarked for quick access during emergencies.

**Last Updated**: December 2024 