from django.shortcuts import get_object_or_404
from .models import Author
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorList(ListView):
    model = Author


class AuthorDetail(LoginRequiredMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)
