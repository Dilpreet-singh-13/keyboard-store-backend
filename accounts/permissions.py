from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser

class FullCRUDPermission(BasePermission):
    """
    Allows anyone to access the safe methods (GET)
    Only authenticated staff and admins have full CRUD functionality
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if isinstance(request.user, AnonymousUser):
                return False
            
            user_role = request.user.user_role
            if user_role == 'customer':
                return False
            elif user_role in ["admin", "staff"]:
                return bool(request.user and request.user.is_authenticated)
            else:
                return False
        

class AdminPermissions(BasePermission):
    """
    Checks if the request user is a Admin and is authenticated
    """

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        if request.user.user_role == "admin":
            return bool(request.user and request.user.is_authenticated)
        else:
            return False

