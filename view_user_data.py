#!/usr/bin/env python
"""
View user data summary
Run: python view_user_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solar_project.settings')
django.setup()

from django.contrib.auth.models import User
from solar_app.models import Booking, Contact, Newsletter

print("=" * 60)
print("USER DATA SUMMARY")
print("=" * 60)

# Users
print("\n[USERS]")
print(f"  Total Users: {User.objects.count()}")
print(f"  Active Users: {User.objects.filter(is_active=True).count()}")
print(f"  Staff Users: {User.objects.filter(is_staff=True).count()}")
print(f"  Superusers: {User.objects.filter(is_superuser=True).count()}")

# Bookings
print("\n[BOOKINGS]")
print(f"  Total Bookings: {Booking.objects.count()}")
print(f"  Pending: {Booking.objects.filter(status='pending').count()}")
print(f"  Confirmed: {Booking.objects.filter(status='confirmed').count()}")
print(f"  Completed: {Booking.objects.filter(status='completed').count()}")
print(f"  Cancelled: {Booking.objects.filter(status='cancelled').count()}")

# Contacts
print("\n[CONTACT SUBMISSIONS]")
print(f"  Total Messages: {Contact.objects.count()}")
print(f"  Unread: {Contact.objects.filter(is_read=False).count()}")
print(f"  Read: {Contact.objects.filter(is_read=True).count()}")

# Newsletter
print("\n[NEWSLETTER SUBSCRIPTIONS]")
print(f"  Total Subscribers: {Newsletter.objects.count()}")
print(f"  Active: {Newsletter.objects.filter(is_active=True).count()}")
print(f"  Inactive: {Newsletter.objects.filter(is_active=False).count()}")

print("\n" + "=" * 60)
print("To view detailed data, go to: http://127.0.0.1:8000/admin/")
print("=" * 60)

