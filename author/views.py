from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Author

def authors(request):
    context = {
        "authors": get_list_or_404(Author),
    }
    return render(request, "authors.html", context)

def author(request, slug):
    context = {
        "author": get_object_or_404(Author, slug=slug),
    }
    return render(request, "author_about.html", context)
# Create your views here.
