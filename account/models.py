from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    address = models.TextField(verbose_name="آدرس منزل", blank=False)
    national_code = models.CharField(max_length=10, verbose_name="کدملی", unique=True, blank=False)
    sel_number = models.CharField(max_length=15, verbose_name="تلفن همراه", blank=False)
    home_number = models.CharField(max_length=11, blank=True, verbose_name="تلفن ثابت")
    birth_date = models.DateField(verbose_name="تاریخ تولد", default=timezone.now, blank=False)
