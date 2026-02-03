from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_DRIVER = 'driver'
    ROLE_HOST = 'host'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = [
        (ROLE_DRIVER, 'Driver'),
        (ROLE_HOST, 'Host'),
        (ROLE_ADMIN, 'Admin'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_DRIVER)
    # Admins can approve or deactivate accounts
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
