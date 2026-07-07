from rest_framework import serializers

from .models import (
    Course,
    Enrollment,
    Grade,
    Student,
    Teacher,
)


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "hire_date",
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "birth_date",
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "teacher",
            "teacher_name",
        ]

    def get_teacher_name(self, obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}"


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_name",
            "course",
            "course_name",
            "enrolled_at",
        ]

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    def get_course_name(self, obj):
        return obj.course.name


class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = [
            "id",
            "enrollment",
            "student_name",
            "course_name",
            "score",
            "status",
        ]

    def get_student_name(self, obj):
        return (
            f"{obj.enrollment.student.first_name} "
            f"{obj.enrollment.student.last_name}"
        )

    def get_course_name(self, obj):
        return obj.enrollment.course.name
