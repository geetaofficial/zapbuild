from rest_framework import permissions

class IsClientOnly(permissions.BasePermission):
    """
    Custom permission to only allow client
    """
    message = "You don't have Permission as you are not Client. "
    def has_permission(self, request, view):
        if  request.user.user_type == 'cln':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.user_type == 'cln':
            return True
        return False


class IsManagerOnly(permissions.BasePermission):
    """
    Custom permission to only allow client
    """
    message = "You don't have Permission as you are not Manager. "
    def has_permission(self, request, view):
        if  request.user.user_type == 'mng':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.user_type == 'mng':
            return True
        return False
        
class IsEmployeeOnly(permissions.BasePermission):
    """
    Custom permission to only allow client
    """
    message = "You don't have Permission as you are not Employee. "
    def has_permission(self, request, view):
        if  request.user.user_type == 'emp':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.user_type == 'emp':
            return True
        return False