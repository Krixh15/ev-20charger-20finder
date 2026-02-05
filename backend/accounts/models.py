from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class NormalizedUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if email:
            email = email.strip().lower()
        if username:
            username = username.strip().lower()
        return super()._create_user(username, email, password, **extra_fields)


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

    objects = NormalizedUserManager()

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.strip().lower()
        if self.username:
            self.username = self.username.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
