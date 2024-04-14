from django import template
from extentions.utils import jalali_converter
from django.utils import timezone

register = template.Library()

@register.simple_tag
def today():
    return jalali_converter(timezone.now())
