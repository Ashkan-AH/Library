from django.contrib import admin
from .models import Reservation
# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("reservation_id", "book_id", "user_id", "persian_date_added", "status", "persian_delivery_date", "deadline", "delivery_remaining")
    list_filter = ["status"]
    ordering = ["-date_added"]
