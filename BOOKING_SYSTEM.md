# Service Booking System - Documentation

## Overview

A complete service booking system that allows customers to book services, view their bookings, and manage appointments. The system includes email notifications and admin management.

## Features

✅ **Complete Booking System**:
- Create service bookings
- View booking details with confirmation code
- List all bookings (for logged-in users)
- Cancel bookings
- Email confirmation notifications
- Admin interface for managing bookings

✅ **User-Friendly Interface**:
- Beautiful booking forms
- Service selection from active services
- Date and time validation
- Business hours validation (9 AM - 6 PM)
- Responsive design

✅ **Integration**:
- Integrated with services section on homepage
- "Book Now" buttons on each service
- Navbar links for easy access
- Works for both authenticated and non-authenticated users

## Database Model

### Booking Model Fields:
- `user` - ForeignKey to User (optional, for authenticated users)
- `service` - ForeignKey to Service
- `customer_name` - Full name
- `customer_email` - Email address
- `customer_phone` - Phone number (optional)
- `booking_date` - Preferred date
- `booking_time` - Preferred time
- `address` - Service location address
- `notes` - Additional notes/requirements
- `status` - Booking status (pending, confirmed, completed, cancelled)
- `confirmation_code` - Unique 8-character code
- `created_at` - Booking creation timestamp
- `updated_at` - Last update timestamp

## URLs

- `/booking/` - Create a new booking
- `/booking/service/<service_id>/` - Create booking for specific service
- `/booking/<confirmation_code>/` - View booking details
- `/booking/<confirmation_code>/cancel/` - Cancel a booking
- `/my-bookings/` - List all bookings (login required)

## Usage

### For Customers

1. **Book a Service**:
   - Click "Book Service" in navbar or "Book Now" on any service
   - Fill out the booking form
   - Submit to receive confirmation code
   - Check email for confirmation (if email is configured)

2. **View Booking**:
   - Use the confirmation code to view booking details
   - Or login and go to "My Bookings"

3. **Cancel Booking**:
   - Go to booking details page
   - Click "Cancel Booking" button
   - Confirm cancellation

### For Administrators

1. **Manage Bookings**:
   - Go to Django Admin: `/admin/`
   - Navigate to "Bookings"
   - View, edit, or change status of bookings
   - Filter by status, date, or service
   - Search by customer name, email, or confirmation code

2. **Update Booking Status**:
   - Pending → Confirmed (when you confirm the appointment)
   - Confirmed → Completed (after service is done)
   - Any status → Cancelled (if customer cancels)

## Form Validation

- **Date**: Cannot be in the past
- **Time**: 
  - Cannot be in the past for today's date
  - Must be between 9:00 AM and 6:00 PM (business hours)
- **Phone**: Must have at least 10 digits
- **Email**: Must be valid email format
- **Service**: Must be an active service

## Email Notifications

The system sends email notifications when:
- A booking is created (confirmation email with details and link)
- A booking is cancelled (cancellation notification)

**Note**: Email notifications only work if SMTP is configured in `settings.py`. If not configured, bookings will still be created but no emails will be sent.

## Admin Interface

The admin interface provides:
- List view with all bookings
- Filter by status, date, service
- Search by customer info or confirmation code
- Edit booking details
- Change booking status
- View booking history

## Integration Points

1. **Homepage Services Section**:
   - Each service card has a "Book Now" button
   - Clicking opens booking form with service pre-selected

2. **Navbar**:
   - "Book Service" link (always visible)
   - "My Bookings" link (for logged-in users)

3. **Service API**:
   - Services are loaded from the API
   - Only active services are shown in booking form

## Status Workflow

```
Pending → Confirmed → Completed
   ↓
Cancelled
```

- **Pending**: New booking, awaiting confirmation
- **Confirmed**: Booking confirmed by admin
- **Completed**: Service has been completed
- **Cancelled**: Booking cancelled (by customer or admin)

## Confirmation Code

- Automatically generated 8-character uppercase code
- Unique for each booking
- Used to view booking details without login
- Sent in confirmation email

## Customization

### Business Hours

Edit `solar_app/forms.py` in `BookingForm.clean_booking_time()`:
```python
if booking_time < time(9, 0) or booking_time > time(18, 0):
    # Change these times as needed
```

### Booking Fields

To add more fields:
1. Add field to `Booking` model in `models.py`
2. Add field to `BookingForm` in `forms.py`
3. Update templates to display new field
4. Run migrations

## Testing

1. **Create a Booking**:
   - Go to `/booking/`
   - Fill out the form
   - Submit and note the confirmation code

2. **View Booking**:
   - Go to `/booking/<confirmation_code>/`
   - Verify all details are correct

3. **List Bookings** (if logged in):
   - Login to your account
   - Go to `/my-bookings/`
   - See all your bookings

4. **Cancel Booking**:
   - Go to booking details
   - Click cancel
   - Confirm cancellation

## Troubleshooting

### Booking form not showing services
- Make sure services are created and marked as active in admin
- Check that `is_active=True` for services

### Email not sending
- Check SMTP configuration in `settings.py`
- Verify email credentials are correct
- Check server logs for email errors

### Confirmation code not working
- Make sure the code is entered correctly (case-sensitive)
- Check that booking exists in database

## Future Enhancements

Possible additions:
- Calendar view for bookings
- Recurring bookings
- Booking reminders (email/SMS)
- Payment integration
- Booking rescheduling
- Customer reviews after completion
- Booking history export

