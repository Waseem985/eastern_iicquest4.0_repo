from django.contrib import admin
from .models import User, ProviderProfile

admin.site.register(User)
admin.site.register(ProviderProfile)