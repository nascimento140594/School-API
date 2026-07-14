from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    EnrollmentViewSet,
    GradeViewSet,
    StudentViewSet,
    TeacherViewSet,
    api_root,
)

app_name = "school"

router = DefaultRouter()

router.register(
    r"teachers",
    TeacherViewSet,
    basename="teacher",
)

router.register(
    r"students",
    StudentViewSet,
    basename="student",
)

router.register(
    r"courses",
    CourseViewSet,
    basename="course",
)

router.register(
    r"enrollments",
    EnrollmentViewSet,
    basename="enrollment",
)

router.register(
    r"grades",
    GradeViewSet,
    basename="grade",
)

urlpatterns = [
    path("", api_root, name="api-root"),
    path("", include(router.urls)),
]
