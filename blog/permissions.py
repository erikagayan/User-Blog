"""Custom permissions for the blog app."""

from rest_framework import permissions


def is_superuser_or_moderator(user):
    """Check if the user is a superuser or a moderator."""
    return user.is_superuser or user.is_moderator


class IsStaffOrReadOnly(permissions.BasePermission):
    """Permission class to allow staff members to edit, and others to read."""

    def has_permission(self, request, view):
        """Check if the user has permission to perform the action."""
        return (
            request.method in permissions.SAFE_METHODS
            or is_superuser_or_moderator(request.user)
        )

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to perform the action on the object."""
        return (
            request.method in permissions.SAFE_METHODS
            or is_superuser_or_moderator(request.user)
        )
