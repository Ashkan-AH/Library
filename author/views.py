from typing import Any
from django.shortcuts import get_object_or_404
from .models import Author
from books.models import Books
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorList(ListView):
    model = Author
    paginate_by = 21
    template_name = "main/authors/authors.html"
    


class AuthorDetail(DetailView):
    template_name = "main/authors/author_detail.html"
    def get_object(self):
        global slug
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = [author for author in Author.objects.all().order_by("?")[0:3]]
        return context