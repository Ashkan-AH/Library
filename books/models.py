from extentions.utils import jalali_converter
from django.db import models
from author.models import Author

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name="نام دسته بندی")
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=False, verbose_name="لینک")

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def persian_date_created(self):
        return jalali_converter(self.date_created)
    
    persian_date_created.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.name



class Books(models.Model):
    AGE_CATEGORY_CHOICES = {
        "کودک":"کودک", 
        "نوجوان":"نوجوان", 
        "بزرگسال":"بزرگسال",
    }
    LANGUAGE_CHOICES = {
        "خارجی":{
            "انگلیسی":"انگلیسی",
            "فرانسوی":"فرانسوی",
            "آلمانی":"آلمانی",
            "عربی":"عربی",
        },
        "داخلی":{
            "فارسی":"فارسی",
            "کردی":"کردی",
            "ترکی":"ترکی",
        }
    }
    name = models.CharField(max_length=255, verbose_name="نام کتاب", null=False, blank=False)
    author = models.ManyToManyField(Author, related_name="books", blank=False)
    publisher = models.CharField(max_length=255, verbose_name="ناشر", default="نا معلوم", blank=True)
    translator = models.CharField(max_length=150, verbose_name="مترجم", default="نا معلوم", blank=True)
    number_of_pages = models.IntegerField(verbose_name="تعداد صفحات", default=0, blank=True)
    in_stock = models.IntegerField(verbose_name="موجودی", default=1, blank=True)
    category = models.ManyToManyField(Category, related_name="books", blank=False)
    pub_year = models.IntegerField(verbose_name="سال انتشار", default=0000, blank=True)
    edition = models.IntegerField(verbose_name="سری چاپ", default=1, blank=True)
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICES, verbose_name="زبان", default="فارسی", blank=True)
    picture = models.ImageField(upload_to="uploads/books/", verbose_name="عکس کتاب", blank=False)
    age_category = models.CharField(max_length=15, choices=AGE_CATEGORY_CHOICES,verbose_name="گروه سنی", blank=True, default="کودک")
    description = models.TextField(verbose_name="توضیحات", blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    date_edited = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    slug = models.SlugField(max_length=255, verbose_name="لینک", allow_unicode=True, unique=True)
    
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

    def persian_date(self):
        return jalali_converter(self.date_edited)
    
    def __str__(self) -> str:
        return self.name
    
    persian_date.short_description = "آخرین ویرایش"

