from django.test import TestCase

from school.models import Enrollment

class EnrollmentModelTest(TestCase):
    def test_model_exists(self):
        self.assertEqual(Enrollment.objects.count(), 0)
