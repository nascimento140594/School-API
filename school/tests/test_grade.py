from django.test import TestCase

from school.models import Grade

class GradeModelTest(TestCase):
    def test_model_exists(self):
        self.assertEqual(Grade.objects.count(), 0)
