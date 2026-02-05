from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class AuthFlowTests(TestCase):
    def test_signup_rejects_duplicate_email(self):
        User.objects.create_user(
            username="user@example.com",
            email="user@example.com",
            password="StrongPass123!",
        )

        response = self.client.post(
            reverse("signup"),
            {
                "name": "Second User",
                "email": "USER@example.com",
                "password": "StrongPass123!",
                "role": User.ROLE_DRIVER,
            },
        )

        self.assertEqual(User.objects.filter(email="user@example.com").count(), 1)
        self.assertContains(response, "A user with that email already exists")

    def test_login_with_normalized_email_redirects(self):
        User.objects.create_user(
            username="driver@example.com",
            email="driver@example.com",
            password="StrongPass123!",
        )

        response = self.client.post(
            reverse("login"),
            {"email": "DRIVER@example.com", "password": "StrongPass123!"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], reverse("driver_dashboard"))
