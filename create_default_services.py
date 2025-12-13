"""
Script to create default services for the booking system
Run this with: python manage.py shell < create_default_services.py
Or: python manage.py shell, then copy-paste the code
"""

from solar_app.models import Service

# Create default services if they don't exist
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

created_count = 0
for service_data in services_data:
    service, created = Service.objects.get_or_create(
        name=service_data['name'],
        defaults=service_data
    )
    if created:
        created_count += 1
        print(f"✓ Created service: {service.name}")
    else:
        print(f"- Service already exists: {service.name}")

print(f"\n{created_count} new service(s) created!")
print(f"Total active services: {Service.objects.filter(is_active=True).count()}")

