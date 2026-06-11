UrbanCare is a web-based service marketplace designed to connect customers with trusted local service providers such as electricians, plumbers, cleaners, technicians, and other skilled professionals. The platform simplifies the process of finding, verifying, and booking services through a centralized digital system. Customers can browse available services, view provider profiles, and submit booking requests, while service providers can manage their profiles, receive notifications, and handle customer bookings efficiently. By promoting transparency, accessibility, and convenience, UrbanCare helps local professionals expand their reach and creates a reliable ecosystem for service discovery and management within communities. Built using Django, HTML, CSS, and Bootstrap, the platform aims to modernize traditional service hiring and support local economic growth through digital transformation.

Problem Statement
In many local communities, finding reliable and skilled service providers such as electricians, plumbers, cleaners, and technicians is still a time-consuming and unstructured process. Customers often rely on word-of-mouth or random contacts, which leads to issues like lack of trust, inconsistent pricing, and difficulty in verifying service quality. At the same time, many skilled service providers struggle to reach customers and grow their income due to limited visibility and lack of a digital platform.

Solution Overview
UrbanCare is a web-based service marketplace that bridges the gap between customers and local service providers. It provides a centralized platform where users can easily search, compare, and book services based on their needs. Service providers can create verified profiles, showcase their skills, and manage bookings efficiently. The system improves trust through structured profiles and booking management while increasing accessibility and convenience for both customers and providers. UrbanCare ultimately aims to digitize local service hiring and make it more transparent, efficient, and reliable.

Tech Stack
•	Frontend: HTML5, CSS3, Bootstrap 5
•	Backend: Django (Python)
•	Database: SQLite (Development) / PostgreSQL (Production-ready)
•	Authentication: Django Built-in Authentication System
•	Media Storage: Cloudinary (for document and image uploads)
•	Version Control: Git & GitHub




Setup Instructions
1. Clone Repository
git clone https://github.com/Waseem985/eastern_iicquest4.0_repo
cd urbancare
2. Create Virtual Environment
python -m venv venv
3. Activate Environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Run Migrations
python manage.py makemigrations
python manage.py migrate
6. Create Superuser
python manage.py createsuperuser
7. Run Server
python manage.py runserver
Visit:
http://127.0.0.1:8000/

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
│
├── media/
│
├── db.sqlite3
│
└── manage.py

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
team_eastern


