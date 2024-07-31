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

    first_name = models.CharField(verbose_name="نام", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=150, blank=True)
    email = models.EmailField(verbose_name="ایمیل", unique=True, blank=False)
    address = models.TextField(verbose_name="آدرس منزل", blank=True)
    birth_number = models.CharField(verbose_name="شماره شناسنامه", max_length=20, blank=True)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", unique=True, blank=True)
    fathers_name = models.CharField(verbose_name="نام پدر", max_length=50, blank=True)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=True)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    emergency_number = models.CharField(max_length=15, verbose_name="شماره اضطراری", blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    picture = models.ImageField(upload_to="uploads/profile/", verbose_name="تصویر", default="default.jpg")


    reservation_limit = models.IntegerField(default=5, verbose_name="محدودیت رزرو")


    role = models.CharField(verbose_name="نقش", choices=ROLE_CHOICES, max_length=7, blank=True)


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
        if self.birth_date:
            return date2jalali(self.birth_date).strftime("%Y %B %d")
    
    def is_information_compelete(self):
        if self.first_name and self.last_name and self.address and self.birth_number and self.national_code and self.fathers_name and self.sel_number and self.emergency_number and self.birth_date and self.role:
            return True
        else:
            return False
    is_information_compelete.boolean = True
    is_information_compelete.short_description = "کامل بودن پروفایل"
