from rest_framework.permissions import BasePermission

from users.managers import UserRoles


class IsAdAuthorOrStaff(BasePermission):
    message = "Вы не имеете право изменять это объявление"

    def has_object_permission(self, request, view, ad):
        if request.user == ad.author or request.user.role == UserRoles.ADMIN:
            return True
        return False
