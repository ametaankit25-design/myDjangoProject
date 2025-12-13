#!/usr/bin/env python
"""
Create a Django superuser
Run: python create_admin.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solar_project.settings')
django.setup()

from django.contrib.auth.models import User

# Default admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@solar.com'
ADMIN_PASSWORD = 'admin123'

# Check if admin user already exists
if User.objects.filter(username=ADMIN_USERNAME).exists():
    print(f"Admin user '{ADMIN_USERNAME}' already exists!")
    print("To reset password, use: python manage.py changepassword admin")
else:
    # Create superuser
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
    print("=" * 50)
    print("ADMIN USER CREATED SUCCESSFULLY!")
    print("=" * 50)
    print(f"Username: {ADMIN_USERNAME}")
    print(f"Email: {ADMIN_EMAIL}")
    print(f"Password: {ADMIN_PASSWORD}")
    print("=" * 50)
    print("\n[IMPORTANT] Change this password after first login!")
    print("Admin Panel: http://127.0.0.1:8000/admin/")
    print("=" * 50)

