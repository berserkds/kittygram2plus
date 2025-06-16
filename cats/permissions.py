from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class OwnerOrReadOnly(permissions.BasePermission):

    def had_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def had_object_permission(self, request, view, obj):
        return obj.owner == request.user
