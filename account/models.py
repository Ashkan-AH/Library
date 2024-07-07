from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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
        "آموزشکده فنی پسران آستانه اشرفیه":"آموزشکده فنی پسران آستانه اشرفیه",
        "آموزشکده فنی پسران لاهیجان - شهیدرجائی":"آموزشکده فنی پسران لاهیجان - شهیدرجائی",
        "دانشکده فنی و حرفه‌ای صومعه سرا":"دانشکده فنی و حرفه‌ای صومعه سرا",
        "آموزشکده فنی دختران رشت":"آموزشکده فنی دختران رشت",
        "دانشگاه فنی و حرفه‌ای استان گیلان":"دانشگاه فنی و حرفه‌ای استان گیلان",
    }
    MAJOR_CHOICES = {
        "حسابداری":"حسابداری",
        "کامپیوتر":"کامپیوتر",
        "صنایع چوب":"صنایع چوب",
        "عمران":"عمران",
        "معماری":"معماری",
        "برق":"برق",
    }


    email = models.EmailField(verbose_name="ایمیل", unique=True, blank=True)
    address = models.TextField(verbose_name="آدرس منزل", blank=True)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", unique=True, blank=True)
    fathers_name = models.CharField(verbose_name="نام پدر", max_length=50, blank=True)
    birth_number = models.CharField(verbose_name="شماره شناسنامه", max_length=20, blank=True)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=True)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    emergency_number = models.CharField(max_length=15, verbose_name="شماره اضطراری", blank=True)
    picture = models.ImageField(upload_to="uploads/profile/", verbose_name="تصویر", blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", blank=True)
    reservation_limit = models.IntegerField(default=5, verbose_name="محدودیت رزرو")
    role = models.CharField(choices=ROLE_CHOICES, max_length=7, blank=True)
    st_id = models.CharField(blank=True, max_length=15, verbose_name="کد دانشجویی")
    st_major = models.CharField(max_length=15, verbose_name="رشته تحصیلی", blank=True, choices=MAJOR_CHOICES)
    st_grade = models.CharField(max_length=15, verbose_name="مقطع تحصیلی", blank=True, choices=GRADE_CHOICES)
    co_id = models.CharField(blank=True, max_length=15, verbose_name="کد کارمندی")
    co_unit = models.CharField(max_length=50, verbose_name="محل کار", blank=True, choices=UNIT_CHOICES)
    co_grade = models.CharField(max_length=15, verbose_name="سمت شغلی", blank=True)
    pro_id =models.CharField(blank=True, max_length=15, verbose_name="کد استادی")
    pro_major = models.CharField(max_length=15, verbose_name="رشته درسی", blank=True, choices=MAJOR_CHOICES)
    pro_grade = models.CharField(max_length=15, verbose_name="مقطع درسی", blank=True, choices=GRADE_CHOICES)

    def persian_birthdate(self):
        return date2jalali(self.birth_date).strftime("%Y %B %d")