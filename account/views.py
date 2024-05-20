from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from books.models import Books

def home(request):
    return render(request, "account/home.html")
class BookList(LoginRequiredMixin, ListView):
    template_name = "account/books_list.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Books.objects.all()
        raise Http404


class BookCreate(LoginRequiredMixin, CreateView):
    model = Books
    fields = ["name", "author", "publisher", "translator", "number_of_pages", "in_stock", "category", "pub_year", "edition", "language", "picture", "age_category", "description", "slug"]
    template_name = "account/book-create-update.html"