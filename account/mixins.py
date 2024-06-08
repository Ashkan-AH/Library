from django.core.exceptions import PermissionDenied
class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("You can't see this page.")
        return super().dispatch(request, *args, **kwargs)
    
class StaffAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("You can't see this page.")