from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from reservation.models import Reservation
from account.models import User
from author.models import Author
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
def waiting_add(request, id):
    book = get_object_or_404(Books, id=id)
    if book.in_stock_user <= 0:
        if book.waiting_users.filter(id=request.user.id).exists():
            book.waiting_users.remove(request.user)
        else:
            book.waiting_users.add(request.user)
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
    template_name = "main/books/books.html"
    def get_queryset(self):
        books = Books.objects.all()
        for book in books:
            bookmark = bool
            if book.bookmarks.filter(id=self.request.user.id).exists():
                bookmark = True
            book.is_bookmarked = bookmark
            reserved = bool
            if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=self.request.user.id), Q(status="رزرو شده")).exists():
                reserved = True
            book.is_reserved = reserved
            waiting = bool
            if book.waiting_users.filter(id=self.request.user.id).exists():
                waiting = True
            book.is_waiting = waiting
        
        return books



def index(request):
    books = Books.objects.all()
    for book in books:
        bookmark = bool
        if book.bookmarks.filter(id=request.user.id).exists():
            bookmark = True
        book.is_bookmarked = bookmark
        reserved = bool
        if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=request.user.id), Q(status="رزرو شده")).exists():
            reserved = True
        book.is_reserved = reserved
        waiting = bool
        if book.waiting_users.filter(id=request.user.id).exists():
            waiting = True
        book.is_waiting = waiting
    context = {
        "books": books,
        "authors":Author.objects.all(),
        "categories":Category.objects.all()
    }
    return render(request, "index.html", context)
    
class AuthorBookList(ListView):
    template_name = "main/books/books.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Books.objects.filter(author__slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        book = Books.objects.filter(author__slug=slug)
        bookmark = bool
        if book.bookmarks.filter(user_id=self.request.user.id).exists():
            bookmark = True
        context["bookmark"] = bookmark
        reserved = bool
        if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=self.request.user.id), Q(status="رزرو شده")).exists():
            reserved = True
        context["reserved"] = reserved
        waiting = bool
        if book.waiting_users.filter(id=self.request.user.id).exists():
            waiting = True
        context["waiting"] = waiting
        return context
    



class BookDetail(DetailView):
    template_name = "main/books/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        return book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        bookmark = bool
        if book.bookmarks.filter(id=self.request.user.id).exists():
            bookmark = True
        context["bookmark"] = bookmark
        reserved = bool
        if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=self.request.user.id), Q(status="رزرو شده")).exists():
            reserved = True
        context["reserved"] = reserved
        waiting = bool
        if book.waiting_users.filter(id=self.request.user.id).exists():
            waiting = True
        context["waiting"] = waiting
        return context


class CategoryList(ListView):
    template_name = "main/books/categories.html"
    model = Category
class CategoryBookList(ListView):
    template_name = "main/books/books.html"
    def get_queryset(self):
        
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        books = selected_category.books.all()
        for book in books:
            bookmark = bool
            if book.bookmarks.filter(id=self.request.user.id).exists():
                bookmark = True
            book.is_bookmarked = bookmark
            reserved = bool
            if Reservation.objects.filter(Q(book_id=book.id), Q(user_id=self.request.user.id), Q(status="رزرو شده")).exists():
                reserved = True
            book.is_reserved = reserved
            waiting = bool
            if book.waiting_users.filter(id=self.request.user.id).exists():
                waiting = True
            book.is_waiting = waiting
        return books
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        context["category"] = selected_category
        return context