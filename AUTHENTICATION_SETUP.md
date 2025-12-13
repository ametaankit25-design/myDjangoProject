# Authentication & SMTP Setup Guide

## Overview

The authentication system includes:
- User registration (signup) with email verification
- User login
- User logout
- SMTP email functionality for verification emails

## Setup Instructions

### 1. Configure SMTP Settings

Edit `solar_project/settings.py` and add your email configuration:

```python
# Email Configuration (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Your email
EMAIL_HOST_PASSWORD = 'your-app-password'  # App password (see below)
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### 2. Gmail Setup (Recommended)

If using Gmail:

1. **Enable 2-Step Verification**:
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password**:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Enter "Django Solar App"
   - Click "Generate"
   - Copy the 16-character password
   - Use this password in `EMAIL_HOST_PASSWORD`

**Important**: Use the App Password, NOT your regular Gmail password!

### 3. Other Email Providers

#### Outlook/Hotmail
```python
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@outlook.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

#### Yahoo
```python
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@yahoo.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Generate from Yahoo account settings
```

### 4. Run Migrations

After configuring email, run migrations to create the UserProfile model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Test Email Configuration

You can test your email setup using Django shell:

```bash
python manage.py shell
```

Then run:
```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test email from Django.',
    settings.DEFAULT_FROM_EMAIL,
    ['your-test-email@gmail.com'],
    fail_silently=False,
)
```

If successful, you should receive the test email.

## Usage

### User Registration Flow

1. User visits `/signup/`
2. User fills out registration form
3. User account is created but marked as inactive
4. Verification email is sent to user's email
5. User clicks verification link in email
6. Account is activated
7. User can now login

### User Login Flow

1. User visits `/login/`
2. User enters username and password
3. If credentials are correct and account is active, user is logged in
4. User is redirected to homepage

### URLs

- **Signup**: `/signup/`
- **Login**: `/login/`
- **Logout**: `/logout/`
- **Email Verification**: `/verify-email/<token>/`

### Accessing Authentication Pages

- From the homepage navbar, click "Login" or "Sign Up"
- Or navigate directly to:
  - http://127.0.0.1:8000/signup/
  - http://127.0.0.1:8000/login/

## Features

### Email Verification

- New users receive a verification email upon registration
- Email contains a unique verification link
- Account remains inactive until email is verified
- Verification link expires after use

### Security Features

- Password validation (minimum length, complexity)
- CSRF protection on all forms
- Secure password hashing
- Email uniqueness validation
- Username format validation

## Troubleshooting

### Email Not Sending

1. **Check SMTP settings** in `settings.py`
2. **Verify credentials** are correct
3. **Check firewall** - port 587 should be open
4. **For Gmail**: Make sure you're using App Password, not regular password
5. **Check spam folder** - verification emails might be filtered

### "Invalid verification token" Error

- Token may have expired
- Token may have already been used
- User can request a new verification email (feature to be added)

### Email in Spam Folder

- Add your email address to contacts
- Configure SPF/DKIM records for your domain (production)
- Use a professional email service (SendGrid, Mailgun, etc.) for production

## Production Recommendations

For production, consider:

1. **Use professional email service**:
   - SendGrid
   - Mailgun
   - Amazon SES
   - Postmark

2. **Environment variables** for sensitive data:
   ```python
   import os
   EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
   ```

3. **Email templates** in separate files (already implemented in HTML)

4. **Rate limiting** for signup/login attempts

5. **Password reset functionality** (can be added)

## Next Steps

- Add password reset functionality
- Add email change verification
- Add account deletion
- Add profile management page
- Add social authentication (Google, Facebook)

