# Solar Energy Website - Django Backend

A complete Django backend implementation for the Solar Energy website with full CRUD functionality for managing content, contact forms, newsletter subscriptions, and more.

## Features

- **Dynamic Content Management**: Manage carousel slides, about section, services, team members, and FAQs through Django admin
- **Contact Form**: Fully functional contact form with backend storage
- **Newsletter Subscription**: Email subscription management
- **User Authentication**: Complete login/signup system with email verification
- **SMTP Email Integration**: Functional email system for user verification
- **RESTful API**: Complete REST API endpoints for all features
- **Admin Interface**: User-friendly Django admin panel for content management
- **Responsive Design**: Maintains the original responsive design

## Project Structure

```
Solar/
├── solar_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── solar_app/              # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # API views
│   ├── serializers.py      # REST API serializers
│   ├── admin.py            # Admin configuration
│   └── urls.py             # App URLs
├── templates/              # HTML templates
│   └── index.html          # Main page template
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   ├── img/
│   └── lib/
├── media/                  # User uploaded files (created after migration)
├── manage.py
└── requirements.txt
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Email account for SMTP (Gmail, Outlook, etc.)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure SMTP Settings

Edit `solar_project/settings.py` and configure your email settings:

```python
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Gmail App Password
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

**For Gmail**: You need to generate an App Password. See `AUTHENTICATION_SETUP.md` for detailed instructions.

### Step 3: Run Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Superuser

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set your username, email, and password.

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

The admin panel will be available at `http://127.0.0.1:8000/admin/`

### Step 6: Test Authentication

- Sign up: http://127.0.0.1:8000/signup/
- Login: http://127.0.0.1:8000/login/

## Usage

### Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Manage content:
   - **About**: Edit about section content
   - **Carousel Slides**: Add/edit carousel slides for the homepage
   - **Services**: Manage services/products
   - **Team Members**: Add/edit team member information
   - **FAQs**: Manage frequently asked questions
   - **Contacts**: View contact form submissions
   - **Newsletter**: View newsletter subscriptions

### API Endpoints

All API endpoints are available under `/api/`:

- `GET /api/about/` - Get about section content
- `GET /api/services/` - Get all active services
- `GET /api/team/` - Get all active team members
- `GET /api/faqs/` - Get all FAQs (grouped by type)
- `GET /api/carousel/` - Get all active carousel slides
- `POST /api/contact/` - Submit contact form
- `POST /api/newsletter/` - Subscribe to newsletter

### Adding Initial Data

You can add initial data through the admin panel or use Django shell:

```bash
python manage.py shell
```

Example: Adding a service

```python
from solar_app.models import Service

Service.objects.create(
    name="Solar System",
    description="Complete solar energy solutions for your home",
    order=1,
    is_active=True
)
```

## Models

### About
- `title`: About section title
- `subtitle`: Subtitle (optional)
- `description`: Main description text
- `experience_years`: Years of experience
- `image`: About section image

### Service
- `name`: Service name
- `description`: Service description
- `image`: Service image
- `order`: Display order
- `is_active`: Active status

### TeamMember
- `name`: Team member name
- `position`: Job position
- `bio`: Biography
- `image`: Team member photo
- `twitter_url`, `facebook_url`, `linkedin_url`: Social media links
- `order`: Display order
- `is_active`: Active status

### FAQ
- `question_type`: Type (why_solar or why_us)
- `question`: FAQ question
- `answer`: FAQ answer (optional)
- `order`: Display order
- `is_active`: Active status

### Contact
- `name`: Contact name
- `email`: Contact email
- `subject`: Message subject
- `message`: Message content
- `is_read`: Read status

### Newsletter
- `email`: Subscriber email
- `is_active`: Active subscription status

### CarouselSlide
- `title`: Slide title
- `subtitle`: Slide subtitle
- `description`: Slide description
- `image`: Slide image
- `button_text`: Button text
- `button_link`: Button link
- `order`: Display order
- `is_active`: Active status

## Static Files

Static files (CSS, JavaScript, images) are served from the `static/` directory. Make sure to run:

```bash
python manage.py collectstatic
```

This collects all static files for production use.

## Media Files

Uploaded images and files are stored in the `media/` directory. This directory is created automatically when you upload files through the admin panel.

## Development Notes

- The website uses Django REST Framework for API endpoints
- CORS is enabled for development (adjust in `settings.py` for production)
- CSRF protection is enabled for form submissions
- All API endpoints return JSON responses

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Change `SECRET_KEY` to a secure random value
4. Configure proper database (PostgreSQL recommended)
5. Set up proper static file serving (WhiteNoise or CDN)
6. Configure CORS settings appropriately
7. Set up email backend for contact form notifications

## License

This project uses the original HTML template license. Please refer to the LICENSE.txt file for details.

## Authentication

The website includes a complete authentication system:

- **Sign Up**: Users can create accounts at `/signup/`
- **Login**: Users can login at `/login/`
- **Email Verification**: New users receive verification emails
- **Logout**: Authenticated users can logout

See `AUTHENTICATION_SETUP.md` for detailed SMTP configuration instructions.

## Support

For issues or questions, please check the Django documentation or create an issue in the project repository.

