from django.db import models
from django.utils import timezone
from books.models import Books
from account.models import User
from datetime import timedelta
from jalali_date import date2jalali
from datetime import timedelta

class ReservationManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        for reservation in qs:
            if reservation.status == "تحویل داده شده" and reservation.delivery_remaining() <= 0:
                user = User.objects.get(id=reservation.user.id)
                user.is_active = False
                user.save()
                reservation.status = "بازگردانده نشده"
                reservation.save()
            elif reservation.status == "رزرو شده" and reservation.reservation_deadline_remaining() <= 0:
                user = User.objects.get(id=reservation.user.id)
                book = Books.objects.get(id=reservation.book.id)
                user.reservation_limit += 1
                user.save()
                reservation.status = "لغو رزرو"
                reservation.save()
                book.in_stock_user += 1
                book.save()
        return qs

class Reservation(models.Model):
    STATUS_CHOICES = {
        "رزرو شده": "رزرو شده", 
        "لغو رزرو": "لغو رزرو", 
        "تحویل داده شده": "تحویل داده شده",
        "بازگردانده نشده": "بازگردانده نشده", 
        "بازگردانده شده": "بازگردانده شده", 
    }
    reservation_id = models.AutoField(primary_key=True, verbose_name="شماره رزرو")
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="reservations", verbose_name="کتاب")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reservations", verbose_name="کاربر")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد رزرو")
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default="رزرو شده", verbose_name="وضعیت رزرو")
    delivery_date = models.DateField(verbose_name="تاریخ تحویل", blank=True, null=True)
    deadline = models.DateField(verbose_name="تاریخ بازگشت کتاب", blank=True, null=True)
    extend_request = models.BooleanField(verbose_name="درخواست تمدید", default=False)
    extend_sluts = models.IntegerField(verbose_name="تعداد درخواست مهلت اضافه باقی مانده", default=2)

    objects = ReservationManager()



    def persian_date_added(self):
        return date2jalali(self.date_added)
    
    def persian_delivery_date(self):
        if self.delivery_date:
            return date2jalali(self.delivery_date)
        return None
    
    def persian_deadline(self):
        if self.deadline:
            return date2jalali(self.deadline)
        return None
    
    def reservation_deadline(self):
        if self.status == "رزرو شده":
            return date2jalali(self.date_added + timedelta(days=7))
        return None
    
    def reservation_deadline_remaining(self):
        if self.reservation_deadline:
            result = (self.date_added.date() + timedelta(days=7) - timezone.now().date()).days
            if result < 0:
                return 0
            else:
                return result
        return None
    
    def delivery_remaining(self):
        if self.delivery_date and self.deadline:
            result = ((self.delivery_date + timedelta(days=14)) - timezone.now().date()).days
            if result < 0:
                return 0
            else:
                return result
        return None
        
    persian_date_added.short_description = "تاریخ رزرو"
    persian_delivery_date.short_description = "تاریخ تحویل کتاب"
    delivery_remaining.short_description = "تعداد روز های باقی مانده"

    def __str__(self)->int:
        return str(self.reservation_id)
    
    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزرو‌ها"
        ordering = ["-date_added"]



