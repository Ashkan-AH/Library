from django import template
from jalali_date import date2jalali
from django.utils import timezone

register = template.Library()

@register.simple_tag
def today():
    return date2jalali(timezone.now()).strftime("%Y %B %d")
