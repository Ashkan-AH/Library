from django.http import Http404
class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404("You can't see this page.")
        return super().dispatch(request, *args, **kwargs)
    
class StaffAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You can't see this page.")
        return super().dispatch(request, *args, **kwargs)