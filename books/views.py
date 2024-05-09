from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Books, Category
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "books": Books.objects.all(),
        }
    return render(request, "books/index.html", context)

@login_required
def about(request, slug):
    context = {
        "book": get_object_or_404(Books, slug=slug),
    }
    return render(request, "books/about.html", context)

@login_required
def category(request, slug):
    selected_category = get_object_or_404(Category, slug=slug)
    context = {
        "category": selected_category,
        "books": selected_category.books.all()
    }
    return render(request, "books/index.html", context)