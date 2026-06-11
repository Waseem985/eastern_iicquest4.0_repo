from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# =========================
# Custom User Model
# =========================
class User(AbstractUser):
    """
    Extends Django's default user model to add roles.
    """

    CUSTOMER = "customer"
    PROVIDER = "provider"

    ROLE_CHOICES = (
        (CUSTOMER, "Customer"),
        (PROVIDER, "Provider"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )

    def __str__(self):
        return self.username


# =========================
# Provider Profile Model
# =========================
class ProviderProfile(models.Model):
    """
    Extra information for service providers.
    One-to-one relationship with User.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="provider_profile"
    )

    # Location Information
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)

    # Identity Verification
    citizenship_Num = models.CharField(max_length=100, blank=True)

    czn_front = models.ImageField(
        upload_to='credentials/citizenship_front/',
        blank=True,
        null=True
    )

    czn_back = models.ImageField(
        upload_to='credentials/citizenship_back/',
        blank=True,
        null=True
    )

    # Professional Details
    service_type = models.CharField(max_length=255, blank=True)

    experience_years = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    short_bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.service_type or 'No Service'}"


# =========================
# Contact Form Messages
# =========================
class ContactMessage(models.Model):
    """
    Stores messages from Contact Us page.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# Booking System
# =========================
class Booking(models.Model):
    """
    Handles customer bookings for providers.
    """

    # Status options
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    COMPLETED = "Completed"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (COMPLETED, "Completed"),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customer_bookings"
    )

    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="provider_bookings"
    )

    service = models.CharField(max_length=100)

    booking_date = models.DateTimeField(auto_now_add=True)

    # FIXED: now properly uses choices
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )


# =========================
# Notifications
# =========================
class Notification(models.Model):
    """
    Simple notification system for providers.
    """

    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


# =========================
# Services List
# =========================
class Service(models.Model):
    """
    Available services like electrician, plumber, etc.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name