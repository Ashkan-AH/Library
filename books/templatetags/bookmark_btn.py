from django import template
from books.models import Books
from django.db.models import Q

register = template.Library()

@register.inclusion_tag("main/books/bookmark_btn.html")
def bookmark_btn(request, book):
    book = Books.objects.get(id=book.id)
    if book.bookmarks.filter(id=request.user.id).exists():
        book.is_bookmarked = True
    return {
        "request": request, 
        "book": book,
        }


