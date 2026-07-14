from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="courses",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    enrolled_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.student} - {self.course}"


class Grade(models.Model):
    enrollment = models.OneToOneField(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="grade",
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)

    STATUS_CHOICES = [
        ("PASSED", "Passed"),
        ("FAILED", "Failed"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        return f"{self.enrollment} ({self.score})"
