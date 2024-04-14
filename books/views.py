from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Books, Category
def home(request):
    context = {
        "books": Books.objects.all(),
        }
    return render(request, "index.html", context)

def about(request, slug):
    context = {
        "book": get_object_or_404(Books, slug=slug),
    }
    return render(request, "about.html", context)

def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug)
    }
    return render(request, "category.html", context)