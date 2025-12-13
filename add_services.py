#!/usr/bin/env python
"""
Add default services to the database
Run: python add_services.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solar_project.settings')
django.setup()

from solar_app.models import Service

# Default services
services_data = [
    {
        'name': 'Solar System Installation',
        'description': 'Complete solar panel system installation for your home or business',
        'order': 1,
        'is_active': True
    },
    {
        'name': 'Wind Turbine Installation',
        'description': 'Professional wind turbine installation and setup',
        'order': 2,
        'is_active': True
    },
    {
        'name': 'Wind Generator Installation',
        'description': 'Wind generator system installation and maintenance',
        'order': 3,
        'is_active': True
    },
    {
        'name': 'Solar Panel Maintenance',
        'description': 'Regular maintenance and cleaning of solar panel systems',
        'order': 4,
        'is_active': True
    },
    {
        'name': 'Energy Consultation',
        'description': 'Expert consultation on renewable energy solutions',
        'order': 5,
        'is_active': True
    }
]

print("Creating default services...\n")
created_count = 0

for service_data in services_data:
    service, created = Service.objects.get_or_create(
        name=service_data['name'],
        defaults=service_data
    )
    if created:
        created_count += 1
        print(f"[OK] Created: {service.name}")
    else:
        # Update existing service to ensure it's active
        service.is_active = True
        service.order = service_data['order']
        service.description = service_data['description']
        service.save()
        print(f"[UPDATE] Updated: {service.name}")

print(f"\n[SUCCESS] {created_count} new service(s) created!")
print(f"[INFO] Total active services: {Service.objects.filter(is_active=True).count()}")
print("\nServices are now available in the booking form!")

