from django.db import models
from django.utils import timezone
from books.models import Books
from account.models import User
from datetime import timedelta
from jalali_date import date2jalali
# Create your models here.

class Reservation(models.Model):
    STATUS_CHOICES = {
        "رزرو شده": "رزرو شده", 
        "لغو رزرو": "لغو رزرو", 
        "تحویل داده شده": "تحویل داده شده",
        "بازگردانده نشده": "بازگردانده نشده", 
        "بازگردانده شده": "بازگردانده شده", 
    }
    reservation_id = models.AutoField(primary_key=True, verbose_name="شماره رزرو")
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="reservations", verbose_name="کد کتاب")
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reservations", verbose_name="کد کاربری")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد رزرو")
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default="رزرو شده", verbose_name="وضعیت رزرو")
    delivery_date = models.DateField(verbose_name="تاریخ تحویل", blank=True, null=True)
    extend_sluts = models.IntegerField(verbose_name="تعداد درخواست مهلت اضافه باقی مانده", default=2)
    def persian_date_added(self):
        return date2jalali(self.date_added).strftime("%Y %B %d")
    def persian_delivery_date(self):
        if self.delivery_date is not None:
            return date2jalali(self.delivery_date).strftime("%Y %B %d")
    def deadline(self):
        if self.delivery_date is not None:
            return date2jalali(self.delivery_date + timedelta(days=14)).strftime("%Y %B %d")
    def delivery_remaining(self):
        if self.delivery_date is not None and self.deadline is not None:
            return ((self.delivery_date + timedelta(days=14)) - timezone.now().date())
    persian_date_added.short_description = "تاریخ رزرو"
    persian_delivery_date.short_description = "تاریخ تحویل کتاب"
    deadline.short_description = "تاریخ بازگشت کتاب"
    delivery_remaining.short_description = "تعداد روز های باقی مانده"

    def __str__(self)->int:
        return str(self.reservation_id)
    
    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزرو‌ها"