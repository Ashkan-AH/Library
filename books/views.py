from typing import Any
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from reservation.models import Reservation
from account.models import User, PageTheme
from author.models import Author
from .models import Books, Category

def search_item(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        results = [{"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"book"}for item in Books.objects.filter(Q(name__icontains=query) | Q(publisher__icontains=query) | Q(translator__icontains=query))]
        for item in Author.objects.filter(name__icontains=query):
            results.append({"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"author"})
        for item in Category.objects.filter(name__icontains=query):
            results.append({"name":item.name, "picture":item.picture.url, "slug":item.slug, "type":"category"})
   
    return JsonResponse(results, safe=False)



@login_required
def bookmark_add(request, id):
    book = get_object_or_404(Books, id=id)
    if book.bookmarks.filter(id=request.user.id).exists():
        book.bookmarks.remove(request.user)
    else:
        book.bookmarks.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def waiting_add(request, id):
    book = get_object_or_404(Books, id=id)
    if book.in_stock_user <= 0:
        if book.waiting_users.filter(id=request.user.id).exists():
            book.waiting_users.remove(request.user)
        else:
            book.waiting_users.add(request.user)
        return HttpResponseRedirect(request.META["HTTP_REFERER"])



@login_required
def reservation_add(request, book):
    book = Books.objects.get(id=book)
    user = User.objects.get(id=request.user.id)
    if Reservation.objects.filter(Q(book=book), Q(user=request.user.id), Q(status="رزرو شده")).exists():
        reservation = Reservation.objects.get(Q(book=book), Q(user=request.user.id), Q(status="رزرو شده"))
        reservation.status = "لغو رزرو"
        book.in_stock_user += 1
        user.reservation_limit += 1
        book.save()
        reservation.save()
        user.save()
    else:
        if book.in_stock_user > 0 and user.reservation_limit > 0:
            Reservation.objects.create(book=book, user=user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



def search_result(request):
    
    search = request.GET.get('search', "")
    if search:
        authors = Author.objects.filter(name__icontains=search)
        books = Books.objects.filter(Q(name__icontains=search) | Q(publisher__icontains=search) | Q(translator__icontains=search))
        categories = Category.objects.filter(name__icontains=search)
    else:
        authors = Author.objects.none()
        books = Books.objects.none()
        categories = Category.objects.none()

        
    books_page_number = request.GET.get("books_page", 1)
    books_paginator = Paginator(books, 12)
    books_page = books_paginator.get_page(books_page_number)

    
    authors_page_number = request.GET.get("authors_page", 1)
    authors_paginator = Paginator(authors, 12)
    authors_page = authors_paginator.get_page(authors_page_number)

    
    categories_page_number = request.GET.get("categories_page", 1)
    categories_paginator = Paginator(categories, 12)
    categories_page = categories_paginator.get_page(categories_page_number)

    context = {
    "books_page": books_page, 
    "books_page_range": get_page_range(books_page),

    "authors_page": authors_page, 
    "authors_page_range": get_page_range(authors_page),

    "categories_page": categories_page, 
    "categories_page_range": get_page_range(categories_page),

    "search_text": search, 
    "footer": PageTheme.objects.get(slug="footer"),
    "theme": PageTheme.objects.get(slug="search-result"),
    }
    return render(request, "main/search_result.html", context)

def get_page_range(page_obj):
    index = page_obj.number - 1
    max_index = len(page_obj.paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    return page_obj.paginator.page_range[start_index:end_index]



class BookList(ListView):
    template_name = "main/books/books.html"
    paginate_by = 18
    def get_queryset(self):
        if "slug" in self.kwargs:
            slug = self.kwargs.get("slug")
            return Books.objects.filter(author__slug=slug)
        return Books.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "slug" in self.kwargs:
            slug = self.kwargs.get("slug")
            context["author_name"] = Author.objects.get(slug=slug).name
        context["theme"] = PageTheme.objects.get(slug="books")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context


def index(request):
    context = {
        "theme": PageTheme.objects.get(slug="index"), 
        "footer": PageTheme.objects.get(slug="footer"), 
        "books": [book for book in Books.objects.all().order_by("?")[0:8]],
        "authors": [author for author in Author.objects.all().order_by("?")[0:8]],
        "categories": [category for category in Category.objects.all()[0:4]],
        "books_number": Books.objects.all().count(),
        "reserve_number": Reservation.objects.filter(status="بازگردانده شده").count(),
        "users_number": User.objects.all().count(),
    }
    return render(request, "main/index.html", context)
    
# class AuthorBookList(ListView):
#     paginate_by = 18
#     template_name = "main/books/books.html"
#     def get_queryset(self):
#         slug = self.kwargs.get("slug")
#         return Books.objects.filter(author__slug=slug)
        
    



class BookDetail(DetailView):
    template_name = "main/books/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        global book1
        book1 = Books.objects.get(slug=slug)
        if book1.waiting_users.filter(id=self.request.user.id).exists():
            book1.is_waiting = True
        if book1.bookmarks.filter(id=self.request.user.id).exists():
            book1.is_bookmarked = True
        return book1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservation"] = Reservation.objects.filter(Q(book=book1.id), Q(user=self.request.user.id), Q(status="تحویل داده شده")|Q(status="رزرو شده")).first()
        context["books"] = [book for book in Books.objects.filter(Q(category__in=(book1.category.all())), ~Q(slug=book1.slug)).order_by("?")[0:3]]
        context["theme"] = PageTheme.objects.get(slug="books")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context
        
    

class CategoryList(ListView):
    paginate_by = 12
    template_name = "main/books/categories.html"
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["theme"] = PageTheme.objects.get(slug="categories")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context
class CategoryBookList(ListView):
    template_name = "main/books/books.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        return selected_category.books.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        selected_category = get_object_or_404(Category, slug=slug)
        context["category"] = selected_category
        context["theme"] = PageTheme.objects.get(slug="books")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context