from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Student


class StudentApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="admin123",
        )
        self.client.force_authenticate(self.user)

    def test_create_student(self):
        url = reverse("school:student-list")

        payload = {
            "first_name": "Pedro",
            "last_name": "Souza",
            "email": "pedro@test.com",
            "birth_date": "2005-10-15",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_students(self):
        Student.objects.create(
            first_name="Ana",
            last_name="Costa",
            email="ana@test.com",
            birth_date=date(2006, 5, 20),
        )

        url = reverse("school:student-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
