from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view.queryset.model._meta.model_name)
        print(view.queryset.model._meta.app_label)
        print(request.method)
        return True