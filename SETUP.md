# Quick Setup Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Initialize Database

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3. Create Admin User

```bash
python manage.py createsuperuser
```

Enter:
- Username: (your choice)
- Email: (your email)
- Password: (your password)

## 4. Run Server

```bash
python manage.py runserver
```

## 5. Access the Website

- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 6. Add Initial Content

1. Go to Admin Panel (http://127.0.0.1:8000/admin/)
2. Login with your superuser credentials
3. Add content:
   - **Carousel Slides**: Add slides for homepage
   - **About**: Add about section content
   - **Services**: Add your services/products
   - **Team Members**: Add team member information
   - **FAQs**: Add frequently asked questions

## Testing the Features

### Contact Form
1. Scroll to the Contact section
2. Fill out the form
3. Submit - the message will be saved in the database
4. View submissions in Admin Panel → Contacts

### Newsletter
1. Scroll to the Newsletter section in footer
2. Enter your email
3. Click "Sign Up"
4. View subscriptions in Admin Panel → Newsletters

## API Endpoints

Test the API endpoints using a tool like Postman or curl:

```bash
# Get all services
curl http://127.0.0.1:8000/api/services/

# Get all team members
curl http://127.0.0.1:8000/api/team/

# Submit contact form
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","subject":"Test","message":"Hello"}'

# Subscribe to newsletter
curl -X POST http://127.0.0.1:8000/api/newsletter/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

## Troubleshooting

### Static files not loading?
Run: `python manage.py collectstatic`

### Images not displaying?
Make sure the `media/` directory exists and has proper permissions.

### CSRF errors?
The API endpoints are configured to work with AJAX. Make sure your JavaScript is sending the CSRF token correctly.

