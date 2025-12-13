# Where to View User Data

## 📊 Django Admin Panel (Main Location)

**URL**: http://127.0.0.1:8000/admin/

**Login Credentials**:
- Username: `admin`
- Password: `admin123`

## 📋 Available User Data Sections

### 1. **User Accounts** (Authentication)
**Location**: Admin Panel → **Users**

**What you'll see**:
- All registered users
- Usernames
- Email addresses
- Account status (active/inactive)
- Staff/superuser status
- Registration dates

**To access**: Click on "Users" in the admin panel

---

### 2. **Contact Form Submissions**
**Location**: Admin Panel → **Contacts**

**What you'll see**:
- Customer name
- Email address
- Subject
- Message content
- Read/Unread status
- Submission date/time

**To access**: Click on "Contacts" in the admin panel

**Features**:
- Mark messages as read/unread
- Search by name, email, or subject
- Filter by read status or date

---

### 3. **Newsletter Subscriptions**
**Location**: Admin Panel → **Newsletters**

**What you'll see**:
- Subscriber email addresses
- Subscription status (active/inactive)
- Subscription date

**To access**: Click on "Newsletters" in the admin panel

**Features**:
- View all subscribers
- Activate/deactivate subscriptions
- Export email list

---

### 4. **Service Bookings**
**Location**: Admin Panel → **Bookings**

**What you'll see**:
- Customer name and contact info
- Service booked
- Booking date and time
- Service address
- Booking status (pending/confirmed/completed/cancelled)
- Confirmation code
- Additional notes
- Created/updated timestamps

**To access**: Click on "Bookings" in the admin panel

**Features**:
- Filter by status, date, or service
- Search by customer name, email, or confirmation code
- Change booking status
- View booking history

---

### 5. **User Profiles**
**Location**: Admin Panel → **User Profiles**

**What you'll see**:
- User account linked
- Email verification status
- Verification token (if not verified)
- Profile creation date

**To access**: Click on "User Profiles" in the admin panel

---

## 🔍 How to View Data in Admin Panel

### Step-by-Step:

1. **Open Admin Panel**:
   - Go to: http://127.0.0.1:8000/admin/
   - Login with admin credentials

2. **Navigate to Data Section**:
   - Click on any model name (Users, Contacts, Bookings, etc.)
   - You'll see a list of all records

3. **View Individual Record**:
   - Click on any record to see full details
   - Edit if needed

4. **Search and Filter**:
   - Use the search box at the top
   - Use filters on the right sidebar
   - Sort by clicking column headers

---

## 📊 Data Summary by Section

### Users Section
- **Total Users**: See count at top
- **Active Users**: Filter by "Active" status
- **Staff Users**: Filter by "Staff status"

### Contacts Section
- **Unread Messages**: Filter by "Is read" = No
- **Recent Submissions**: Sorted by date (newest first)

### Bookings Section
- **Pending Bookings**: Filter by status = "pending"
- **Today's Bookings**: Filter by booking date
- **By Service**: Filter by specific service

### Newsletters Section
- **Active Subscribers**: Filter by "Is active" = Yes
- **Total Subscribers**: See count at top

---

## 💻 View Data via Django Shell (Advanced)

You can also view data programmatically:

```bash
python manage.py shell
```

### View All Users:
```python
from django.contrib.auth.models import User
users = User.objects.all()
for user in users:
    print(f"{user.username} - {user.email} - Active: {user.is_active}")
```

### View All Bookings:
```python
from solar_app.models import Booking
bookings = Booking.objects.all()
for booking in bookings:
    print(f"{booking.customer_name} - {booking.service.name} - {booking.booking_date}")
```

### View Contact Submissions:
```python
from solar_app.models import Contact
contacts = Contact.objects.all()
for contact in contacts:
    print(f"{contact.name} - {contact.email} - {contact.subject}")
```

### View Newsletter Subscriptions:
```python
from solar_app.models import Newsletter
subscribers = Newsletter.objects.filter(is_active=True)
for sub in subscribers:
    print(sub.email)
```

---

## 📈 Quick Stats

To get quick statistics, use Django shell:

```python
from django.contrib.auth.models import User
from solar_app.models import Booking, Contact, Newsletter

# Count users
print(f"Total Users: {User.objects.count()}")
print(f"Active Users: {User.objects.filter(is_active=True).count()}")

# Count bookings
print(f"Total Bookings: {Booking.objects.count()}")
print(f"Pending Bookings: {Booking.objects.filter(status='pending').count()}")

# Count contacts
print(f"Total Contacts: {Contact.objects.count()}")
print(f"Unread Contacts: {Contact.objects.filter(is_read=False).count()}")

# Count subscribers
print(f"Total Subscribers: {Newsletter.objects.count()}")
print(f"Active Subscribers: {Newsletter.objects.filter(is_active=True).count()}")
```

---

## 🎯 Most Common Tasks

### View Recent Bookings:
1. Go to Admin → Bookings
2. Click on any booking to see details
3. Use date filter to see bookings by date range

### View Unread Contact Messages:
1. Go to Admin → Contacts
2. Filter by "Is read" = No
3. Click on message to read and mark as read

### View User Registrations:
1. Go to Admin → Users
2. Sort by "Date joined" (newest first)
3. Click on user to see full profile

### Export Data (Manual):
- Select records in admin panel
- Copy data manually
- Or use Django shell to export to CSV (advanced)

---

## 🔐 Security Note

- Only superusers can access the admin panel
- Regular users cannot see other users' data
- All data is stored in the SQLite database (`db.sqlite3`)

---

## 📁 Database Location

The actual database file is located at:
```
Solar/db.sqlite3
```

You can view it with SQLite browser tools, but the admin panel is the recommended way.

---

## 🆘 Need Help?

If you can't see certain data:
1. Make sure you're logged in as superuser
2. Check that migrations are run: `python manage.py migrate`
3. Verify data exists: Use Django shell to check counts
4. Check admin.py to ensure models are registered

