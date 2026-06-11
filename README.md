UrbanCare - All Services Portal
Overview

UrbanCare is a web-based service marketplace developed using Django that connects customers with local service providers. The platform allows users to book services such as electricians, plumbers, cleaners, and technicians while enabling providers to manage bookings and showcase their professional profiles.

The primary goal of UrbanCare is to simplify the process of finding trusted local service professionals and provide a centralized platform for service booking and management.

Features
Customer Features
User registration and login
Browse available services
Book service providers
Track booking status
Contact support through the Contact Us page
Service Provider Features
Provider registration and login
Create and manage professional profiles
Upload citizenship verification documents
Specify service category and experience
Receive booking requests
Manage booking status (Accept, Reject, Complete)
Admin Features
Manage users and providers
View customer inquiries
Monitor bookings
Verify provider information
Technology Stack
Backend
Python
Django
Frontend
HTML5
CSS3
Bootstrap 5
Database
SQLite (Development)
PostgreSQL (Production Ready)
Media Storage
Cloudinary (for document and image uploads)
Database Models
User

Custom user model with role-based authentication.

Roles:

Customer
Provider
ProviderProfile

Stores:

Location information
Citizenship details
Professional information
Service category
Experience
Bio
Booking

Stores:

Customer information
Provider information
Service booked
Booking status
ContactMessage

Stores inquiries submitted through the Contact Us page.

Notification

Stores provider notifications.

Service

Stores available service categories.

Project Structure
UrbanCare/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── homepage.html
│   ├── signup.html
│   ├── login.html
│   ├── contact.html
│   └── services/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── media/
│
├── db.sqlite3
│
└── manage.py
Installation
Clone Repository
git clone https://github.com/yourusername/urbancare.git
Create Virtual Environment
python -m venv myenv
Activate Virtual Environment

Windows:

myenv\Scripts\activate

Linux/Mac:

source myenv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Migrations
python manage.py makemigrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Start Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/
Future Improvements
        Online payment integration
        Real-time notifications
        Service provider ratings and reviews
        Chat system between customers and providers
        GPS-based provider search
        Mobile application for Android and iOS
        AI-powered service recommendations
Project Status

Currently under active development.

Author

MD Waseem

Bachelor in Computer Engineering

Developed as a learning project to explore Django, authentication systems, role-based access control, and service marketplace development.

