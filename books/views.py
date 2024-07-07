from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from reservation.models import Reservation
from account.models import User
from .models import Books, Category

@login_required
def bookmark_add(request, id):
    book = get_object_or_404(Books, id=id)
    if book.bookmarks.filter(id=request.user.id).exists():
        book.bookmarks.remove(request.user)
    else:
        book.bookmarks.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def reservation_add(request, book_id):
    book = Books.objects.get(id=book_id)
    user = User.objects.get(id=request.user.id)
    if Reservation.objects.filter(Q(book_id=book_id), Q(user_id=request.user.id), Q(status="رزرو شده")).exists():
        reservation = Reservation.objects.get(Q(book_id=book_id), Q(user_id=request.user.id), Q(status="رزرو شده"))
        reservation.status = "لغو رزرو"
        book.in_stock_user += 1
        book.save()
        reservation.save()
    else:
        if book.in_stock_user > 0 and user.reservation_limit > 0:
            Reservation.objects.create(book_id=book, user_id=user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



class BookList(ListView):
    model = Books
    

class BookDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        global book
        book = Books.objects.get(slug=slug)
        return book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookmark = bool
        if book.bookmarks.filter(id=self.request.user.id).exists():
            bookmark = True
        context["bookmark"] = bookmark
        reserved = bool
        if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=self.request.user.id), Q(status="رزرو شده")).exists():
            reserved = True
        context["reserved"] = reserved
        return context


class CategoryList(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        return selected_category.books.all()