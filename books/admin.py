from django.contrib import admin
from .models import Books, Category, Comment
# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name", "author"]}
    list_display = ("html_img", "name", "translator", "persian_date", "category_str")
    list_filter = ["language", "age_category"]
    search_fields = ["name", "author", "translator"]
    ordering = ["-date_edited"]
    

admin.site.register(Comment)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name"]}
    search_fields = ["name"]
    ordering = ["-date_created"]
    list_display = ("id", "name", "persian_date_created")