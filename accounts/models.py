from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ("admin", "admin"),
        ("staff", "staff"),
        ("customer", "customer"),
    ]

    username = models.CharField(
        max_length=200, unique=True, blank=False, null=False
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    user_role = models.CharField(
        max_length=10,
        choices=USER_ROLE_CHOICES,
        default="customer",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.username} ({self.user_role})"
