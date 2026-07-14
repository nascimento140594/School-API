from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Course, Teacher


class CourseApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="admin123",
        )
        self.client.force_authenticate(self.user)

        self.teacher = Teacher.objects.create(
            first_name="Carlos",
            last_name="Oliveira",
            email="carlos@test.com",
            hire_date=date(2023, 1, 1),
        )

    def test_create_course(self):
        url = reverse("school:course-list")

        payload = {
            "name": "Python",
            "description": "Python Course",
            "teacher": self.teacher.id,
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_courses(self):
        Course.objects.create(
            name="Django",
            description="Framework",
            teacher=self.teacher,
        )

        url = reverse("school:course-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
