from django.urls import path
from . import views

# ========================
# URL Configuration
# ========================

urlpatterns = [
    # ====================
    # PUBLIC PAGES
    # ====================
    path("", views.home_page, name="homepage"),
    path("home/", views.home_page, name="homepage"),           # Alternative home route
    
    path("about/", views.about_page, name="about"),
    path("services/", views.service_page, name="services"),
    path("contact/", views.contact_us, name="contact"),

    # ====================
    # AUTHENTICATION
    # ====================
    path("registration/login/", views.login_view, name="login"),
    path("registration/signup/", views.signup_view, name="signup"),

    # ====================
    # SERVICE PAGES
    # ====================
    path("services/electrician/", views.electricity_page, name="electrical"),  # Fixed typo in view name
    path("services/homeservice/", views.HomeService_page, name="homeservice"),

    # ====================
    # CUSTOMER ROUTES
    # ====================
    path("book/<str:service_code>/", views.book_service, name="book_service"),
    
    # Customer's bookings (Note: This was previously mapped under electrician booking)
    path("my-bookings/", views.customer_bookings, name="customer_bookings"),   # Better name recommended

    # ====================
    # PROVIDER ROUTES
    # ====================
    path("provider/dashboard/", views.provider_dashboard, name="provider_dashboard"),
    path("provider/profile/", views.provider_profile, name="provider_profile"),
    path("provider/notifications/", views.provider_notifications, name="provider_notifications"),
    
    # Provider Bookings
    path("provider/bookings/", views.provider_bookings, name="provider_bookings"),  # Improved URL

    # Booking Actions
    path(
        "provider/bookings/accept/<int:booking_id>/",
        views.accept_booking,
        name="accept_booking"
    ),
    path(
        "provider/bookings/reject/<int:booking_id>/",
        views.reject_booking,
        name="reject_booking"
    ),
]