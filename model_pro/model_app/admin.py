# admin.py

from django.contrib import admin
from .models import UserProfile  # Corrected import

# Register your models here.
admin.site.register(UserProfile)
