from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Faqat admin foydalanuvchilarga ruxsat berish, boshqalarga faqat o'qish huquqi
    """
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user and request.user.is_staff
