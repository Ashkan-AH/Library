from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Books
from .mixins import StaffAccessMixin, SuperuserAccessMixin

def home(request):
    return render(request, "account/home.html")

class BookDetail(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Books, slug=slug)


class BookList(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  ListView):
    template_name = "account/books_list.html"
    queryset = Books.objects.all()


class BookCreate(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  CreateView):
    model = Books
    fields = ["name", "author", "publisher", "translator", "number_of_pages", "in_stock", "category", "pub_year", "edition", "language", "picture", "age_category", "description", "slug"]
    template_name = "account/book-create-update.html"
    success_url = reverse_lazy("account:books")


class BookUpdate(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  UpdateView):
    model = Books
    fields = ["name", "author", "publisher", "translator", "number_of_pages", "in_stock", "category", "pub_year", "edition", "language", "picture", "age_category", "description"]
    template_name = "account/book-create-update.html"
    success_url = reverse_lazy("account:book-detail")


class BookDelete(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DeleteView):
    model = Books
    template_name = "account/books_comfirm_delete.html"
    success_url = reverse_lazy("account:books")


class BookPreview(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/book_preview.html"
    def get_object(self):
        return get_object_or_404(Books, slug=self.kwargs.get("slug"))