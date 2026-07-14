from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_superuser
            )
        )


class IsAdminOrTeacherReadOnly(BasePermission):
    """
    Admin:
        Full CRUD.

    Teacher:
        Read only.

    Others:
        No access.
    """

    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_superuser
            )
        ):
            return True

        if (
            request.user.is_authenticated
            and request.user.groups.filter(
                name="Teachers"
            ).exists()
        ):
            return request.method in SAFE_METHODS

        return False


class IsAdminOrTeacher(BasePermission):
    """
    Admin:
        Full CRUD.

    Teacher:
        Full CRUD.

    Student:
        Read only.
    """

    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_superuser
            )
        ):
            return True

        if (
            request.user.is_authenticated
            and request.user.groups.filter(
                name="Teachers"
            ).exists()
        ):
            return True

        if (
            request.user.is_authenticated
            and request.user.groups.filter(
                name="Students"
            ).exists()
        ):
            return request.method in SAFE_METHODS

        return False
