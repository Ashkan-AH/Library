from typing import Any
from django.shortcuts import get_object_or_404
from .models import Author
from django.core.paginator import Paginator
from account.models import PageTheme
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class AuthorList(ListView):
    model = Author
    template_name = "main/authors/authors.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        authors_page_number = self.request.GET.get("authors_page", 1)
        authors_paginator = Paginator(authors, 21)
        authors_page = authors_paginator.get_page(authors_page_number)
        context["authors"] = authors
        context["authors_page"] = authors_page
        context["authors_page_range"] = get_page_range(authors_page)
        context["theme"] = PageTheme.objects.get(slug="authors")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context
    


class AuthorDetail(DetailView):
    template_name = "main/authors/author_detail.html"
    def get_object(self):
        global slug
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = [author for author in Author.objects.all().order_by("?")[0:3]]
        context["theme"] = PageTheme.objects.get(slug="authors")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context
    

def get_page_range(page_obj):
    index = page_obj.number - 1
    max_index = len(page_obj.paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    return page_obj.paginator.page_range[start_index:end_index]