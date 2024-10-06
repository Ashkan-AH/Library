from django import template
from books.models import Books
from reservation.models import Reservation
from django.db.models import Q

register = template.Library()

@register.inclusion_tag("main/books/reservation_btn.html")
def reservation_btn(request, book):
    book = Books.objects.get(id=book.id)
    reservation = Reservation.objects.filter(Q(book=book.id), Q(user=request.user.id), Q(status="تحویل داده شده")|Q(status="رزرو شده")).first()
    if book.waiting_users.filter(id=request.user.id).exists():
        book.is_waiting = True
    return {
        "request": request, 
        "book": book,
        "reservation": reservation,
        }


