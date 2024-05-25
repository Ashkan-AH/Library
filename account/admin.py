from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ("first_name", "last_name", "email", "address", "national_code", "sel_number", "home_number", "birth_date")

admin.site.register(User, UserAdmin)
