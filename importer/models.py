from django.db import models

from .tasks import import_excel_task


class FileImporterModel(models.Model):
    class ExcelFileType(models.TextChoices):
        NEW_LEADS = "new_leads", "مشتریان جدید"
        UPDATE_LEADS_DATA = "update_leads_data", "بروزرسانی اطلاعات مشتریان"

    data_file = models.FileField('فایل', upload_to='import_foreign_users/')
    is_imported = models.BooleanField('وارد پایگاه داده شده؟', default=False)
    import_type = models.CharField("نوع ورودی", max_length=20, choices=ExcelFileType.choices,null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)

        if not self.is_imported:
            import_excel_task.s(file_importer_id=self.id).apply_async(countdown=2)

    class Meta:
        verbose_name = 'وارد کردن اطلاعات'
        verbose_name_plural = 'وارد کردن اطلاعات'
