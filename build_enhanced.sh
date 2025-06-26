#!/usr/bin/env bash
# Enhanced build script for Django deployment on Render
# exit on error
set -o errexit

echo "🔧 Starting Django build process..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "🗄️  Running database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist (optional, for first deployment)
echo "👤 Creating superuser (if needed)..."
python manage.py shell << EOF
from django.contrib.auth.models import User
import os

# Only create superuser if none exists and credentials are provided
if not User.objects.filter(is_superuser=True).exists():
    admin_username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    admin_email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    admin_password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    
    if admin_password:
        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        print(f"Superuser '{admin_username}' created successfully!")
    else:
        print("Skipping superuser creation (no password provided)")
else:
    print("Superuser already exists")
EOF

echo "✅ Build completed successfully!" 