from rest_framework.permissions import BasePermission

class IsAuth(BasePermission):
    def has_permission(self,request,view):
        if request.user.groups != None :
            if request.user.groups.all()[0].name == 'admins':
                return  True
        return False