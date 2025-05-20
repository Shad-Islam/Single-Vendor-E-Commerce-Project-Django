from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    mobile = models.CharField(blank=True, max_length=15)