from django.contrib import admin

# Register your models here.
from .models import FileImporterModel
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(FileImporterModel)
class FileImporterModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['id','data_file', 'is_imported', 'import_type', 'created_at']
    list_filter = ['is_imported', 'import_type']
    search_fields = ['data_file']
    readonly_fields = ['is_imported', 'created_at', 'updated_at']
    fieldsets = (
        ("اطلاعات اصلی", {
            'fields': ('data_file', 'is_imported', 'import_type')
        }),
        ('تاریخ ایجاد و ویرایش', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    actions = None
