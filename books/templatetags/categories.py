from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("books/categories.html")
def categories():
    return {"categories": Category.objects.all()}