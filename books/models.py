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
    llc = models.CharField(max_length=10, blank=True, verbose_name="رده بندی کنگره")
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=False, verbose_name="لینک")
    picture = models.ImageField(upload_to="uploads/categories/", verbose_name="عکس دسته بندی", default="default-category.jpg", blank=False)

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def persian_date_created(self):
        return date2jalali(self.date_created).strftime("%d %B %Y")
    
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
    title = models.CharField(max_length=255, verbose_name="عنوان", null=False, blank=True)
    cover_title = models.CharField(max_length=255, verbose_name="عنوان جلد", default="-", blank=True)
    volume = models.CharField(max_length=255, verbose_name="شماره جلد", default="-", blank=True)
    author = models.ManyToManyField(Author, related_name="books", blank=True ,verbose_name="نویسندگان")
    publisher = models.CharField(max_length=255, verbose_name="ناشر", default="-", blank=True)
    translator = models.CharField(max_length=150, verbose_name="مترجم", default="-", blank=True)
    nli = models.CharField(max_length=255, verbose_name="کتابخانه ملی ایران", default="-", blank=True)
    ddc = models.CharField(max_length=255, verbose_name="رده بندی دهدهی دیوئی", default="-", blank=True)
    location = models.CharField(max_length=255, verbose_name="جایگاه", default="-", blank=True)
    isbn = models.CharField(max_length=255, verbose_name="شابک(ISBN)", default="-", blank=True)
    pub_year = models.IntegerField(verbose_name="سال چاپ", default=0000, blank=True)
    edition = models.CharField(max_length=255, verbose_name="سری چاپ", default="-", blank=True)
    in_stock_user = models.IntegerField(verbose_name="موجودی رزرو نشده", default=1, blank=True)
    in_stock = models.IntegerField(verbose_name="موجودی واقعی", default=1, blank=True)
    llc = models.CharField(max_length=255, verbose_name="رده بندی کنگره", default="-", blank=True)
    
    number_of_pages = models.IntegerField(verbose_name="تعداد صفحات", default=0, blank=True)
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICES, verbose_name="زبان", default="فارسی", blank=True)
    age_category = models.CharField(max_length=15, choices=AGE_CATEGORY_CHOICES,verbose_name="گروه سنی", blank=True, default="کودک")
    
    category = models.ManyToManyField(Category, related_name="books", blank=True, verbose_name="دسته‌بندی‌ها")
    picture = models.ImageField(upload_to="uploads/books/", verbose_name="عکس کتاب", blank=True, default="default-book.jpg")
    description = RichTextField(verbose_name="توضیحات", blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    date_edited = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    slug = models.SlugField(max_length=255, verbose_name="لینک", allow_unicode=True, unique=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", verbose_name="ذخیره شده ها", blank=True)
    waiting_users = models.ManyToManyField(User, related_name="books", verbose_name="لیست انتظار", blank=True)
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

    def persian_date(self):
        return date2jalali(self.date_uploaded).strftime("%d %B %Y")
    def in_stock_email(book):
        if book.in_stock_user > 0 and book.waiting_users != None:
            for user in book.waiting_users.all():
                user = User.objects.get(id=user.id)
                subject = f'افزایش موجودی {book.title}'
                message = f'کتابخانه آنلاین دانشکده میرزا کوچک خان(سرزمین کتاب) \nسلام {user.username}، کتاب {book.title} در کتابخانه موجود شده است.\n برای ثبت درخواست رزرو، وارد لینک زیر بشوید:\nhttp://127.0.0.1:8000/book/{book.slug}/\n\nلطفا از پاسخ دادن این ایمیل خودداری فرمایید.'
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
        return self.title
    
    persian_date.short_description = "آخرین ویرایش"
    html_img.short_description = "تصویر"



class Comment(models.Model):
    STATUS_CHOICES = {
        "تایید شده":"تایید شده",
        "درحال بررسی":"درحال بررسی",
        "رد شده":"رد شده",
    }
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name='comments', verbose_name="کتاب")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments', verbose_name="کاربر")
    text = models.TextField(verbose_name="متن")
    rating = models.IntegerField(default=0, verbose_name="امتیاز")
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="درحال بررسی", verbose_name="وضعیت")
    date_created = models.DateTimeField(verbose_name="تاریخ ایجاد",auto_now_add=True)

    def __str__(self) -> str:
        if self.user:
            return f"{self.user.username} : {self.text[:30]}..."
        else:
            return f"No Author : {self.text[:30]}..."
        
    def persian_date_created(self):
        return date2jalali(self.date_created)
    persian_date_created.short_description = "تاریخ ایجاد"
    class Meta:
        ordering = ["-date_created"]
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
