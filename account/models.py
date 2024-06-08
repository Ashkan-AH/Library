from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from extentions.utils import jalali_converter

class User(AbstractUser):
    address = models.TextField(verbose_name="آدرس منزل", blank=False)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", unique=True, blank=False)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=False)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    picture = models.ImageField(upload_to="uploads/profile/", verbose_name="تصویر", blank=False)
    birth_date = models.DateField(verbose_name="تاریخ تولد", default=timezone.now, blank=False)
    reservation_limit = models.IntegerField(default=5, verbose_name="محدودیت رزرو")


    def persian_birthdate(self):
        return jalali_converter(self.birth_date)