from django.db import models
from django.contrib.auth.models import AbstractUser
from jalali_date import date2jalali

class User(AbstractUser):
    ROLE_CHOICES = {
        "دانشجو":"دانشجو", 
        "استاد":"استاد", 
        "کامند":"کامند",
    }
    GRADE_CHOICES = {
        "کاردانی":"کاردانی",
        "کارشناسی":"کارشناسی",
    }
    UNIT_CHOICES = {
        "آموزشکده فنی بندر انزلی - شهید خدادادی":"آموزشکده فنی بندر انزلی - شهید خدادادی",
        "آموزشکده فنی رستم آباد رودبار - سیدالشهداء":"آموزشکده فنی رستم آباد رودبار - سیدالشهداء",
        "آموزشکده فنی رشت - شهید چمران":"آموزشکده فنی رشت - شهید چمران",
        
    }
    MAJOR_CHOICES = {
        "حسابداری":"حسابداری",
        "کامپیوتر":"کامپیوتر",
        "صنایع چوب":"صنایع چوب",
        "عمران":"عمران",
        "معماری":"معماری",
        "برق":"برق",
    }

    first_name = models.CharField(verbose_name="نام", max_length=150, blank=False)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=150, blank=False)
    email = models.EmailField(verbose_name="ایمیل", unique=True, blank=False)
    address = models.TextField(verbose_name="آدرس منزل", blank=False)
    birth_number = models.CharField(verbose_name="شماره شناسنامه", max_length=20, blank=False)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", unique=True, blank=False)
    fathers_name = models.CharField(verbose_name="نام پدر", max_length=50, blank=False)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=False)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    emergency_number = models.CharField(max_length=15, verbose_name="شماره اضطراری", blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", blank=False)
    picture = models.ImageField(upload_to="uploads/profile/", verbose_name="تصویر", default="default.jpg")


    reservation_limit = models.IntegerField(default=5, verbose_name="محدودیت رزرو")


    role = models.CharField(verbose_name="نقش", choices=ROLE_CHOICES, max_length=7, blank=False)


    # st_id = models.CharField(blank=True, max_length=15, verbose_name="کد دانشجویی")
    # st_major = models.CharField(max_length=15, verbose_name="رشته تحصیلی", blank=True, choices=MAJOR_CHOICES)
    # st_grade = models.CharField(max_length=15, verbose_name="مقطع تحصیلی", blank=True, choices=GRADE_CHOICES)


    # co_id = models.CharField(blank=True, max_length=15, verbose_name="کد کارمندی")
    # co_unit = models.CharField(max_length=50, verbose_name="محل کار", blank=True, choices=UNIT_CHOICES)
    # co_grade = models.CharField(max_length=15, verbose_name="سمت شغلی", blank=True)


    # pro_id =models.CharField(blank=True, max_length=15, verbose_name="کد استادی")
    # pro_major = models.CharField(max_length=15, verbose_name="رشته درسی", blank=True, choices=MAJOR_CHOICES)
    # pro_grade = models.CharField(max_length=15, verbose_name="مقطع درسی", blank=True, choices=GRADE_CHOICES)


    def persian_birthdate(self):
        return date2jalali(self.birth_date).strftime("%Y %B %d")