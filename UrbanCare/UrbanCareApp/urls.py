from django.urls import path
from . import views

urlpatterns=[
    path("", views.home_page, name="homepage"),
    path("home", views.home_page, name="homepage"),
    path("provider/dashboard/", views.provider_dashboard, name="provider_dashboard"),
    path("about", views.about_page, name="about"),
    path('services', views.service_page, name='service'),
    path('contact', views.contact_us, name='contact'),
    path("registration/login/", views.login_view, name="login"),
    path("registration/signup/", views.signup_view, name="signup"),
    path('services/electrician/', views.electrcity_page, name='electrical'),
    path('services/electrician/booking/', views.customer_bookings, name="booking"),
    path("provider/profile/",views.provider_profile,name="provider_profile"),
    path("provider/notifications/",views.provider_notifications,name="provider_notifications"),
    path("provider/providerbooking/",views.provider_bookings,name="provider_booking"),
    # Accept booking
    path("provider/bookings/accept/<int:booking_id>/",views.accept_booking,name="accept_booking"),
    # Reject booking
    path( "provider/bookings/reject/<int:booking_id>/", views.reject_booking, name="reject_booking"),
    path("book/<str:service_code>/", views.book_service, name="book_service"),
]