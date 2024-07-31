from django.db import models
from django.utils import timezone
from books.models import Books
from account.models import User
from datetime import timedelta
from jalali_date import date2jalali
from datetime import timedelta
# Create your models here.
# class ReservationQuerySet(models.QuerySet):
#     def delete_half_done_user(self):
#         date = timezone.now() - timedelta(days=1)
#         self.filter(models.Q(last_login=None), models.Q(date_joined__lt=date)).delete()
#         return self
    
# class ReservationManager(models.Manager):
#     def get_queryset(self):
#         queryset = ReservationQuerySet(self.model, using=self._db)
#         queryset.delete_half_done_user()
#         return queryset


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
        
    # def __getattribute__(self, name: str):
    #     if self.status == "تحویل داده شده" and self.delivery_remaining().days <= 0:
    #         user = User.objects.get(id=self.user_id.id)
    #         user.is_active = False
    #         user.save()
    #         self.status = "بازگردانده نشده"
    #         self.save()
    #     remaining = timezone.now().date() - self.date_added.date()
    #     if remaining.days > 7:
    #         user = User.objects.get(id=self.user_id.id)
    #         book = Books.objects.get(id=self.book_id.id)
    #         user.reservation_limit += 1
    #         user.save()
    #         self.status = "لغو رزرو"
    #         self.save()
    #         book.in_stock_user += 1
    #         book.save()
    #     return super().__getattribute__(name)
    # def not_returned(self):
    #     if self.status == "تحویل داده شده" and self.delivery_remaining().days <= 0:
    #         user = User.objects.get(id=self.user_id.id)
    #         user.is_active = False
    #         user.save()
    #         self.status = "بازگردانده نشده"
    #         self.save()
    # def reservation_expired(self):
    #     remaining = timezone.now().date() - self.date_added.date()
    #     if remaining.days > 7:
    #         user = User.objects.get(id=self.user_id.id)
    #         book = Books.objects.get(id=self.book_id.id)
    #         user.reservation_limit += 1
    #         user.save()
    #         self.status = "لغو رزرو"
    #         self.save()
    #         book.in_stock_user += 1
    #         book.save()
            
    persian_date_added.short_description = "تاریخ رزرو"
    persian_delivery_date.short_description = "تاریخ تحویل کتاب"
    deadline.short_description = "تاریخ بازگشت کتاب"
    delivery_remaining.short_description = "تعداد روز های باقی مانده"

    def __str__(self)->int:
        return str(self.reservation_id)
    
    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزرو‌ها"