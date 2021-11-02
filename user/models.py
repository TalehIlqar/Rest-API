
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(verbose_name="Email Address", blank=True, unique=True)
    country = models.CharField(
        verbose_name="Country", max_length=255, null=True, blank=True)
    city = models.CharField(
        verbose_name="City", max_length=255, null=True, blank=True)
    phone_number = models.CharField(
        verbose_name="Phone Number", max_length=255, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.username}"
    
