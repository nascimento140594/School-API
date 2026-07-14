from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):
    def test_create_token(self):
        get_user_model().objects.create_user(
            username="user",
            email="user@test.com",
            password="testpass123",
        )

        url = reverse("token_obtain_pair")

        payload = {
            "username": "user",
            "password": "testpass123",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
