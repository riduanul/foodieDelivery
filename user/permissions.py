
from rest_framework.permissions import BasePermission

class IsOwnerOrEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # Check if the user is authenticated and if they have the owner or employee role
        if user.is_authenticated and user.role in ['owner', 'employee']:
            return True
        return False
