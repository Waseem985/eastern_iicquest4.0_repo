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
        on_delete=models.CASCADE
    )

    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)

    experience = models.TextField(blank=True)
    citizenship_Num = models.CharField(max_length=100, blank=True)
    czn_front = models.ImageField(upload_to='citizenship/', blank=True)
    czn_back = models.ImageField(upload_to='citizenship/', blank=True)
    service_type = models.CharField(max_length=100, blank=True)
    experience_years = models.IntegerField(blank=True, null=True)
    short_bio = models.TextField(blank=True)
    password = models.CharField(max_length=128, blank=True)
    confirm_password = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return self.user.username