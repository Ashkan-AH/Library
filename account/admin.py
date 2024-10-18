from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PageTheme

UserAdmin.fieldsets[1][1]['fields'] = ("first_name", "last_name", "email", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "reservation_limit", "role", "st_id", "st_major", "st_grade", "emp_id", "emp_unit", "emp_grade", "pro_id", "pro_major", "pro_grade", "view_books", "view_authors", "view_reservations", "view_users", "view_categories", "view_comments", "update_books", "update_authors", "update_reservations", "update_users", "update_categories","update_theme", "update_comments", "create_books", "create_authors", "create_reservations", "create_users", "create_categories", "create_comments", "delete_books", "delete_authors", "delete_reservations", "delete_users", "delete_categories", "delete_comments",)

admin.site.register(User, UserAdmin)
admin.site.register(PageTheme)
