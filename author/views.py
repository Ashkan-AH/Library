from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Author
from django.contrib.auth.decorators import login_required

@login_required
def authors(request):
    context = {
        "authors": get_list_or_404(Author),
    }
    return render(request, "author/authors.html", context)

@login_required
def author(request, slug):
    context = {
        "author": get_object_or_404(Author, slug=slug),
    }
    return render(request, "author/author_about.html", context)
# Create your views here.
