from typing import Any
from django.shortcuts import get_object_or_404
from .models import Books, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

@login_required
def bookmark_add(request, id):
    book = get_object_or_404(Books, id=id)
    if book.bookmarks.filter(id=request.user.id).exists():
        book.bookmarks.remove(request.user)
    else:
        book.bookmarks.add(request.user)
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
        return context


class CategoryList(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        return selected_category.books.all()