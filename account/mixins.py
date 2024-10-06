from django.core.exceptions import PermissionDenied
class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("شما ابر ادمین نیستید!")
        return super().dispatch(request, *args, **kwargs)
class UserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            raise PermissionDenied("شما کاربر ساده نیستید!")
        return super().dispatch(request, *args, **kwargs)
    
class StaffAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما ادمین نیستید!")
    





class ViewBooksAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.view_books:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی مشاهده کتاب ها را ندارید!")
class ViewAuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.view_authors:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی مشاهده نویسندگان را ندارید!")
class ViewUsersAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.view_users:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی مشاهده کاربران را ندارید!")
class ViewReservationsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.view_reservations:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی مشاهده رزرو ها را ندارید!")
class ViewCategoriesAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.view_categories:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی مشاهده دسته بندی ها را ندارید!")
class UpdateBooksAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_books:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش کتاب ها را ندارید!")
class UpdateAuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_authors:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش نویسندگان را ندارید!")
class UpdateUsersAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_users:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش کاربران را ندارید!")
class UpdateReservationsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_reservations:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش رزرو ها را ندارید!")
class UpdateCategoriesAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_categories:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش دسته بندی ها را ندارید!")
class UpdateThemeAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.update_theme:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ویرایش صفحات را ندارید!")
class CreateBooksAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.create_books:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ایجاد کتاب ها را ندارید!")
class CreateAuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.create_authors:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ایجاد نویسندگان را ندارید!")
class CreateUsersAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.create_users:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ایجاد کاربران را ندارید!")
class CreateReservationsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.create_reservations:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ایجاد رزرو ها را ندارید!")
class CreateCategoriesAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.create_categories:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی ایجاد دسته بندی ها را ندارید!")
class DeleteBooksAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.delete_books:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی حذف کتاب ها را ندارید!")
class DeleteAuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.delete_authors:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی حذف نویسندگان را ندارید!")
class DeleteUsersAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.delete_users:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی حذف کاربران را ندارید!")
class DeleteCategoriesAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.delete_categories:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی حذف دسته بندی ها را ندارید!")
class DeleteReservationsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.delete_reservations:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("شما دسترسی حذف رزرو ها را ندارید!")