# from django.contrib.auth.models import Permission
from rest_framework import permissions


class FilmePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in ["GET", "OPTIONS", "HEAD"]:
            return request.user.has_perm("filmes.view_filme")

        if request.method == "POST":
            return request.user.has_perm("filmes.add_filme")

        if request.method in ["PATCH", "PUT"]:
            return request.user.has_perm("filmes.change_filme")

        if request.method == "DELETE":
            return request.user.has_perm("filmes.delete_filme")

        return False
