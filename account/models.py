from django.db import models
from django.contrib.auth.models import AbstractUser
from jalali_date import date2jalali
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import UserManager

class UserQuerySet(models.QuerySet):
    def delete_half_done_user(self):
        date = timezone.now() - timedelta(days=1)
        self.filter(models.Q(last_login=None), models.Q(date_joined__lt=date)).delete()
        return self
    
class UserManager2(UserManager):
    def get_queryset(self):
        queryset = UserQuerySet(self.model, using=self._db)
        queryset.delete_half_done_user()
        return queryset

class User(AbstractUser):
    ROLE_CHOICES = {
        "دانشجو":"دانشجو", 
        "استاد":"استاد", 
        "کارمند":"کارمند",
    }
    STUDENT_GRADE_CHOICES = {
        "کاردانی":"کاردانی",
        "کارشناسی":"کارشناسی",
    }
    PROFESSOR_GRADE_CHOICES = {
        "کاردانی":"کاردانی",
        "کارشناسی":"کارشناسی",
        "کاردانی و کارشناسی": "کاردانی و کارشناسی",
    }
    UNIT_CHOICES = {
        "آموزشکده فنی بندر انزلی - شهید خدادادی":"آموزشکده فنی بندر انزلی - شهید خدادادی",
        "آموزشکده فنی رستم آباد رودبار - سیدالشهداء":"آموزشکده فنی رستم آباد رودبار - سیدالشهداء",
        "آموزشکده فنی رشت - شهید چمران":"آموزشکده فنی رشت - شهید چمران",
        "آموزشکده فنی پسران آسانه اشرفیه":"آموزشکده فنی پسران آسانه اشرفیه",
        "آموزشکده فنی پسران لاهیجان-شهیدرجائی":"آموزشکده فنی پسران لاهیجان-شهیدرجائی",
        "دانشکده فنی و حرفه ای صومعه سرا":"دانشکده فنی و حرفه ای صومعه سرا",
        "آموزشکده فنی دختران رشت":"آموزشکده فنی دختران رشت",
        "دانشگاه فنی و حرفه ای استان گیلان":"دانشگاه فنی و حرفه ای استان گیلان",
        
    }
    MAJOR_CHOICES = {
        "حسابداری":"حسابداری",
        "کامپیوتر":"کامپیوتر",
        "صنایع چوب":"صنایع چوب",
        "عمران":"عمران",
        "معماری":"معماری",
        "برق":"برق",
    }

    first_name = models.CharField(verbose_name="نام", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=150, blank=True)
    email = models.EmailField(verbose_name="ایمیل", unique=True, blank=False)
    address = models.TextField(verbose_name="آدرس منزل", blank=True)
    birth_number = models.CharField(verbose_name="شماره شناسنامه", max_length=20, blank=True)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", blank=True)
    fathers_name = models.CharField(verbose_name="نام پدر", max_length=50, blank=True)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=True)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    emergency_number = models.CharField(max_length=15, verbose_name="شماره اضطراری", blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    picture = models.ImageField(upload_to="uploads/profile/", verbose_name="تصویر", default="default.jpg")


    reservation_limit = models.IntegerField(default=5, verbose_name="محدودیت رزرو")


    role = models.CharField(verbose_name="نقش", choices=ROLE_CHOICES, max_length=7, blank=True)


    st_id = models.CharField(blank=True, max_length=15, verbose_name="کد دانشجویی")
    st_major = models.CharField(max_length=15, verbose_name="رشته تحصیلی", blank=True, choices=MAJOR_CHOICES)
    st_grade = models.CharField(max_length=15, verbose_name="مقطع تحصیلی", blank=True, choices=STUDENT_GRADE_CHOICES)


    emp_id = models.CharField(blank=True, max_length=15, verbose_name="کد پرسنلی")
    emp_unit = models.CharField(max_length=50, verbose_name="محل کار", blank=True, choices=UNIT_CHOICES)
    emp_grade = models.CharField(max_length=255, verbose_name="سمت شغلی", blank=True)


    pro_id =models.CharField(blank=True, max_length=15, verbose_name="کد استادی")
    pro_major = models.CharField(max_length=15, verbose_name="رشته آموزشی", blank=True, choices=MAJOR_CHOICES)
    pro_grade = models.CharField(max_length=18, verbose_name="مقطع آموزشی", blank=True, choices=PROFESSOR_GRADE_CHOICES)


    #Permissions
    #View
    view_books = models.BooleanField(verbose_name="مشاهده کتاب ها", default=False)
    view_authors = models.BooleanField(verbose_name="مشاهده نویسندگان", default=False)
    view_reservations = models.BooleanField(verbose_name="مشاهده رزرو ها", default=False)
    view_users = models.BooleanField(verbose_name="مشاهده کاربران", default=False)
    view_categories = models.BooleanField(verbose_name="مشاهده دسته بندی ها", default=False)
    view_comments = models.BooleanField(verbose_name="مشاهده نظرات", default=False)
    #Update
    update_books = models.BooleanField(verbose_name="ویرایش کتاب ها", default=False)
    update_authors = models.BooleanField(verbose_name="ویرایش نویسندگان", default=False)
    update_reservations = models.BooleanField(verbose_name="ویرایش رزرو ها", default=False)
    update_users = models.BooleanField(verbose_name="ویرایش کاربران", default=False)
    update_categories = models.BooleanField(verbose_name="ویرایش دسته بندی", default=False)
    update_theme = models.BooleanField(verbose_name="ویرایش ظاهر سایت", default=False)
    update_comments = models.BooleanField(verbose_name="ویرایش نظرات", default=False)
    #Create
    create_books = models.BooleanField(verbose_name="ایجاد کتاب ها", default=False)
    create_authors = models.BooleanField(verbose_name="ایجاد نویسندگان", default=False)
    create_reservations = models.BooleanField(verbose_name="ایجاد رزرو ها", default=False)
    create_users = models.BooleanField(verbose_name="ایجاد کاربران", default=False)
    create_categories = models.BooleanField(verbose_name="ایجاد دسته بندی ها", default=False)
    create_comments = models.BooleanField(verbose_name="ایجاد نظرات", default=False)
    #Delete
    delete_books = models.BooleanField(verbose_name="حذف کتاب ها", default=False)
    delete_authors = models.BooleanField(verbose_name="حذف نویسندگان", default=False)
    delete_reservations = models.BooleanField(verbose_name="حذف رزرو ها", default=False)
    delete_users = models.BooleanField(verbose_name="حذف کاربران", default=False)
    delete_categories = models.BooleanField(verbose_name="حذف دسته بندی ها", default=False)
    delete_comments = models.BooleanField(verbose_name="حذف نظرات", default=False)

    objects = UserManager2()
    
    def persian_birth_date(self):
        if self.birth_date:
            return date2jalali(self.birth_date)
    def persian_last_login(self):
        if self.last_login:
            return date2jalali(self.last_login).strftime("%d %B %Y")
    def persian_date_joined(self):
        if self.date_joined:
            return date2jalali(self.date_joined).strftime("%d %B %Y")
    
    # def delete_half_done():
    #     for user in User.objects.all():
    #         if not user.last_login and (user.date_joined + timedelta(days=1)) < timezone.now():
    #             user.delete()

    def is_information_compelete(self):
        if self.first_name and self.last_name and self.address and self.birth_number and self.national_code and self.fathers_name and self.sel_number and self.emergency_number and self.birth_date and ((self.role and ((self.st_id and self.st_grade and self.st_major) or (self.emp_grade and self.emp_id and self.emp_unit) or (self.pro_grade and self.pro_id and self.pro_major))) or self.is_staff or self.is_superuser):
            return True
        else:
            return False
    is_information_compelete.boolean = True
    is_information_compelete.short_description = "کامل بودن پروفایل"






class PageTheme(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام صفحه")
    slug = models.SlugField(allow_unicode=True, max_length=255, verbose_name="آدرس صفحه ویرایش")
    thumbnail = models.ImageField(upload_to="uploads/page_theme/thumbnail/", verbose_name="تصویر پیش نمایش", blank=True, default="default-thumbnail.jpg")
    date_edited = models.DateField(verbose_name="آخرین ویرایش", auto_now=True)
    text1 = models.TextField(verbose_name="متن شماره ۱", blank=True)
    text2 = models.TextField(verbose_name="متن شماره ۲", blank=True)
    text3 = models.TextField(verbose_name="متن شماره ۳", blank=True)
    text4 = models.TextField(verbose_name="متن شماره ۴", blank=True)
    text5 = models.TextField(verbose_name="متن شماره ۵", blank=True)
    text6 = models.TextField(verbose_name="متن شماره ۶", blank=True)
    text7 = models.TextField(verbose_name="متن شماره ۷", blank=True)
    text8 = models.TextField(verbose_name="متن شماره ۸", blank=True)
    text9 = models.TextField(verbose_name="متن شماره ۹", blank=True)
    text10 = models.TextField(verbose_name="متن شماره ۱۰", blank=True)
    text11 = models.TextField(verbose_name="متن شماره ۱۱", blank=True)
    text12 = models.TextField(verbose_name="متن شماره ۱۲", blank=True)
    text13 = models.TextField(verbose_name="متن شماره ۱۳", blank=True)
    text14 = models.TextField(verbose_name="متن شماره ۱۴", blank=True)
    text15 = models.TextField(verbose_name="متن شماره ۱۵", blank=True)
    text16 = models.TextField(verbose_name="متن شماره ۱۶", blank=True)
    text17 = models.TextField(verbose_name="متن شماره ۱۷", blank=True)
    image1 = models.ImageField(upload_to=f"uploads/page_theme/", verbose_name="تصویر شماره ۱", blank=True, default="default-thumbnail.jpg")
    image2 = models.ImageField(upload_to=f"uploads/page_theme/", verbose_name="تصویر شماره ۲", blank=True, default="default-thumbnail.jpg")
    image3 = models.ImageField(upload_to=f"uploads/page_theme/", verbose_name="تصویر شماره ۳", blank=True, default="default-thumbnail.jpg")
    image4 = models.ImageField(upload_to=f"uploads/page_theme/", verbose_name="تصویر شماره ۴", blank=True, default="default-thumbnail.jpg")
    image5 = models.ImageField(upload_to=f"uploads/page_theme/", verbose_name="تصویر شماره ۵", blank=True, default="default-thumbnail.jpg")
    class Meta:
        verbose_name = "ظاهر صفحه"
        verbose_name_plural = "ظاهر صفحات"

    def __str__(self):
        return self.name