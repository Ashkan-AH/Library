from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Books, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BookList(ListView):
    def get_queryset(self):
        return Books.objects.filter(in_stock= not 0)

class BookDetail(LoginRequiredMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        if book.in_stock != 0:
            return book
        raise Http404("چنین کتابی موجود نیست!")


class CategoryList(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        return selected_category.books.filter(in_stock= not 0)