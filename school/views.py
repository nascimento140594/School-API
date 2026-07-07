from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    Course,
    Enrollment,
    Grade,
    Student,
    Teacher,
)
from .serializers import (
    CourseSerializer,
    EnrollmentSerializer,
    GradeSerializer,
    StudentSerializer,
    TeacherSerializer,
)


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    """
    Root endpoint for the School API.
    """
    return Response(
        {
            "project": "School API",
            "version": "1.0.0",
            "description": (
                "REST API for school management built with Django REST Framework."
            ),
            "documentation": {
                "swagger": request.build_absolute_uri("/api/doc/swagger/"),
                "schema": request.build_absolute_uri("/api/schema/"),
            },
            "resources": {
                "teachers": request.build_absolute_uri("/api/teachers/"),
                "students": request.build_absolute_uri("/api/students/"),
                "courses": request.build_absolute_uri("/api/courses/"),
                "enrollments": request.build_absolute_uri("/api/enrollments/"),
                "grades": request.build_absolute_uri("/api/grades/"),
            },
        }
    )


class TeacherViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for teachers.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    filterset_fields = [
        "hire_date",
        "email",
    ]

    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]

    ordering_fields = [
        "first_name",
        "last_name",
        "hire_date",
        "email",
    ]

    ordering = [
        "last_name",
        "first_name",
    ]


class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for students.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filterset_fields = [
        "birth_date",
        "email",
    ]

    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]

    ordering_fields = [
        "first_name",
        "last_name",
        "birth_date",
        "email",
    ]

    ordering = [
        "last_name",
        "first_name",
    ]


class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for courses.
    """

    queryset = Course.objects.select_related("teacher").all()
    serializer_class = CourseSerializer

    filterset_fields = [
        "teacher",
    ]

    search_fields = [
        "name",
        "description",
        "teacher__first_name",
        "teacher__last_name",
    ]

    ordering_fields = [
        "name",
    ]

    ordering = [
        "name",
    ]


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for enrollments.
    """

    queryset = Enrollment.objects.select_related(
        "student",
        "course",
    ).all()

    serializer_class = EnrollmentSerializer

    filterset_fields = [
        "student",
        "course",
    ]

    search_fields = [
        "student__first_name",
        "student__last_name",
        "course__name",
    ]

    ordering_fields = [
        "enrolled_at",
    ]

    ordering = [
        "-enrolled_at",
    ]


class GradeViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for grades.
    """

    queryset = Grade.objects.select_related(
        "enrollment",
        "enrollment__student",
        "enrollment__course",
    ).all()

    serializer_class = GradeSerializer

    filterset_fields = [
        "status",
    ]

    search_fields = [
        "enrollment__student__first_name",
        "enrollment__student__last_name",
        "enrollment__course__name",
    ]

    ordering_fields = [
        "score",
        "status",
    ]

    ordering = [
        "-score",
    ]
