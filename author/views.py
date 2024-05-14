from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from .models import Author
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
# def authors(request):
#     context = {
#         "authors": get_list_or_404(Author),
#     }
#     return render(request, "author/authors.html", context)
class AuthorList(LoginRequiredMixin, ListView):
    model = Author


class AuthorDetail(LoginRequiredMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)
# @login_required
# def author(request, slug):
#     context = {
#         "author": get_object_or_404(Author, slug=slug),
#     }
#     return render(request, "author/author_about.html", context)
# # Create your views here.
