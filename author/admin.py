from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name"]}
    list_display = ("id", "name", "persian_date")
    search_fields = ["name"]
    ordering = ["-date_added"]

# Register your models here.
