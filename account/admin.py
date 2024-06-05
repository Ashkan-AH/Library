from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ("first_name", "last_name", "email", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "bookmarks", "reservation_limit")

admin.site.register(User, UserAdmin)
