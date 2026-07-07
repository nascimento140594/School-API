from django.contrib import admin

from .models import (
    Course,
    Enrollment,
    Grade,
    Student,
    Teacher,
)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "hire_date")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_name", "first_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "birth_date")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_name", "first_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher")
    search_fields = ("name", "teacher__first_name", "teacher__last_name")
    list_filter = ("teacher",)
    ordering = ("name",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "enrolled_at")
    search_fields = (
        "student__first_name",
        "student__last_name",
        "course__name",
    )
    list_filter = ("course", "enrolled_at")
    ordering = ("-enrolled_at",)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "score", "status")
    search_fields = (
        "enrollment__student__first_name",
        "enrollment__student__last_name",
        "enrollment__course__name",
    )
    list_filter = ("status",)
