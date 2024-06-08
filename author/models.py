from django.db import models
from extentions.utils import jalali_converter
from django.utils.html import format_html
from ckeditor.fields import RichTextField

class Author(models.Model):
    name = models.CharField(max_length=75, blank=False, null=False, verbose_name="نام نویسنده")
    picture = models.ImageField(upload_to="uploads/author", blank=False, verbose_name="عکس")
    description = RichTextField(blank=True, verbose_name="توضیحات")
    slug = models.SlugField(blank=False, null=False, verbose_name="لینک", allow_unicode=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def __str__(self):
        return self.name
    

    def html_img(self):
        return format_html(f"<img src='{self.picture.url}' width = 100px height=auto style='border-radius: 10px;'>")
    html_img.short_description = "تصویر"

    def persian_date(self):
        return jalali_converter(self.date_added)
# Create your models here.
