from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Teacher


class TeacherApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="admin123",
        )
        self.client.force_authenticate(self.user)

    def test_list_teachers(self):
        Teacher.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@test.com",
            hire_date=date(2024, 1, 1),
        )

        url = reverse("school:teacher-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_teacher(self):
        url = reverse("school:teacher-list")

        payload = {
            "first_name": "Maria",
            "last_name": "Silva",
            "email": "maria@test.com",
            "hire_date": "2025-01-01",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 1)
