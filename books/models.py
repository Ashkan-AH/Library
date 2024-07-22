from jalali_date import date2jalali
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from author.models import Author
from account.models import User
from django.conf import settings
from django.core.mail import send_mail

class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name="نام دسته بندی")
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=False, verbose_name="لینک")
    picture = models.ImageField(upload_to="uploads/categories/", verbose_name="عکس دسته بندی", default="default.jpg", blank=False)

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def persian_date_created(self):
        return date2jalali(self.date_created).strftime("%Y %B %d")
    
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
    author = models.ManyToManyField(Author, related_name="books", blank=False ,verbose_name="نویسندگان")
    publisher = models.CharField(max_length=255, verbose_name="ناشر", default="نا معلوم", blank=True)
    translator = models.CharField(max_length=150, verbose_name="مترجم", default="نا معلوم", blank=True)
    number_of_pages = models.IntegerField(verbose_name="تعداد صفحات", default=0, blank=True)
    in_stock_user = models.IntegerField(verbose_name="موجودی رزرو نشده", default=1, blank=True)
    in_stock = models.IntegerField(verbose_name="موجودی واقعی", default=1, blank=True)
    category = models.ManyToManyField(Category, related_name="books", blank=False, verbose_name="دسته‌بندی‌ها")
    pub_year = models.IntegerField(verbose_name="سال انتشار", default=0000, blank=True)
    edition = models.IntegerField(verbose_name="سری چاپ", default=1, blank=True)
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICES, verbose_name="زبان", default="فارسی", blank=True)
    picture = models.ImageField(upload_to="uploads/books/", verbose_name="عکس کتاب", blank=False)
    age_category = models.CharField(max_length=15, choices=AGE_CATEGORY_CHOICES,verbose_name="گروه سنی", blank=True, default="کودک")
    description = RichTextField(verbose_name="توضیحات", blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    date_edited = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    slug = models.SlugField(max_length=255, verbose_name="لینک", allow_unicode=True, unique=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", verbose_name="ذخیره شده ها", blank=True)
     
    waiting_users = models.ManyToManyField(User, related_name="books", verbose_name="لیست انتظار")
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

    def persian_date(self):
        return date2jalali(self.date_uploaded).strftime("%Y %B %d")
    def in_stock_email(book):
        if book.in_stock_user > 0 and book.waiting_users != None:
            for user in book.waiting_users.all():
                user = User.objects.get(id=user.id)
                subject = f'افزایش موجودی {book.name}'
                message = f'کتابخانه آنلاین دانشکده میرزا کوچک خان(سرزمین کتاب) \nسلام {user.username}، کتاب {book.name} در کتابخانه موجود شده است.\n برای ثبت درخواست رزرو، وارد لینک زیر بشوید:\nhttp://127.0.0.1:8000/book/{book.slug}/\n\nلطفا از پاسخ دادن این ایمیل خودداری کنید.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                book.waiting_users.remove(user)
    def get_absolute_url(self):
        return reverse("account:books")
    def html_img(self):
        return format_html(f"<img src='{self.picture.url}' width = 100px height=auto style='border-radius: 10px;'>")
    
    def author_str(self):
        return ", ".join([author.name for author in self.author.all()])
    author_str.short_description = "نویسندگان"
    
    def category_str(self):
        return ", ".join([category.name for category in self.category.all()])
    category_str.short_description = "دسته‌بندی‌ها"
    
    def __str__(self) -> str:
        return self.name
    
    persian_date.short_description = "آخرین ویرایش"
    html_img.short_description = "تصویر"

