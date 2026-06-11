from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
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


class ProviderProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="provider_profile" # Added for easier reverse lookups (e.g., user.provider_profile)
    )

    # Location Information
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)

    # Credentials (Cloudinary will automatically organize these into subfolders)
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
    service_type = models.CharField(
        max_length=255, 
        blank=True
    )
    
    # Refinement: Changed to PositiveIntegerField since years of experience is a number
    experience_years = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True
    )

    short_bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.service_type or 'No Service Assigned'}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):

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

    status = models.CharField(
        max_length=20,
        default="Pending"
    )


class Notification(models.Model):

    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=255)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()