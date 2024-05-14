from django.shortcuts import get_object_or_404
from .models import Books, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BookList(LoginRequiredMixin, ListView):
    model = Books


class BookDetail(LoginRequiredMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Books, slug=slug)


class CategoryList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        return selected_category.books.all()