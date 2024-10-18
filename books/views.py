from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from reservation.models import Reservation
from account.models import User, PageTheme
from author.models import Author
from .models import Books, Category, Comment
from .forms import CommentForm

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
def extend_request(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if reservation.extend_sluts > 0 and reservation.extend_request == False and  reservation.status == "تحویل داده شده":
        reservation.extend_request = True
        reservation.save()
    else:
        raise Http404("شما شرایط درخواست تمدید را ندارید.")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


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
            books = Books.objects.filter(author__slug=slug)
            books_page_number = self.request.GET.get("books_page", 1)
            books_paginator = Paginator(books, 18)
            books_page = books_paginator.get_page(books_page_number)
            context["books"] = books
            context["books_page"] = books_page
            context["books_page_range"] = get_page_range(books_page)
            context["theme"] = PageTheme.objects.get(slug="books")
            context["footer"] = PageTheme.objects.get(slug="footer")
            return context
        books = Books.objects.all()
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 18)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
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


class BookDetail(DetailView):
    template_name = "main/books/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        if book.waiting_users.filter(id=self.request.user.id).exists():
            book.is_waiting = True
        if book.bookmarks.filter(id=self.request.user.id).exists():
            book.is_bookmarked = True
        return book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        if book.comments.filter(status="تایید شده").exists():
            comments = book.comments.filter(status="تایید شده").count()
            rating0 = book.comments.filter(Q(status="تایید شده"), Q(rating=0)).count()
            rating0_percentage = rating0*100//comments
            rating1 = book.comments.filter(Q(status="تایید شده"), Q(rating=1)).count()
            rating1_percentage = rating1*100//comments
            rating2 = book.comments.filter(Q(status="تایید شده"), Q(rating=2)).count()
            rating2_percentage = rating2*100//comments
            rating3 = book.comments.filter(Q(status="تایید شده"), Q(rating=3)).count()
            rating3_percentage = rating3*100//comments
            rating4 = book.comments.filter(Q(status="تایید شده"), Q(rating=4)).count()
            rating4_percentage = rating4*100//comments
            rating5 = book.comments.filter(Q(status="تایید شده"), Q(rating=5)).count()
            rating5_percentage = rating5*100//comments
            context["rating0"] = rating0
            context["rating0_percentage"] = rating0_percentage
            context["rating1"] = rating1
            context["rating1_percentage"] = rating1_percentage
            context["rating2"] = rating2
            context["rating2_percentage"] = rating2_percentage
            context["rating3"] = rating3
            context["rating3_percentage"] = rating3_percentage
            context["rating4"] = rating4
            context["rating4_percentage"] = rating4_percentage
            context["rating5"] = rating5
            context["rating5_percentage"] = rating5_percentage
        else:
            context["rating0"] = 0
            context["rating0_percentage"] = 0
            context["rating1"] = 0
            context["rating1_percentage"] = 0
            context["rating2"] = 0
            context["rating2_percentage"] = 0
            context["rating3"] = 0
            context["rating3_percentage"] = 0
            context["rating4"] = 0
            context["rating4_percentage"] = 0
            context["rating5"] = 0
            context["rating5_percentage"] = 0

        context["reservation"] = Reservation.objects.filter(Q(book=book.id), Q(user=self.request.user.id), Q(status="تحویل داده شده")|Q(status="رزرو شده")).first()
        context["got_book"] = Reservation.objects.filter(Q(book=book.id), Q(user=self.request.user.id), (Q(status="بازگردانده شده")|Q(status="تحویل داده شده")))
        context["comments"] = book.comments.filter(status="تایید شده")
        context["form"] = CommentForm
        context["books"] = [book for book in Books.objects.filter(Q(category__in=(book.category.all())), ~Q(slug=book.slug)).order_by("?")[0:3]]
        context["theme"] = PageTheme.objects.get(slug="books")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context
    


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    def form_valid(self, form):
        slug = self.kwargs.get("slug")
        book = Books.objects.get(slug=slug)
        if self.request.user.reservations.filter(Q(book=book.id), (Q(status="بازگردانده شده")|Q(status="تحویل داده شده"))):
            comment = form.save(commit=False)
            rating = self.request.POST.get('rating')
            comment.book = book
            comment.user = self.request.user
            comment.rating = rating  # ذخیره امتیاز
            comment.save()
            return HttpResponseRedirect(reverse_lazy("books:book-detail", kwargs={"slug": slug}))


class CategoryList(ListView):
    template_name = "main/books/categories.html"
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        categories_page_number = self.request.GET.get("categories_page", 1)
        categories_paginator = Paginator(categories, 12)
        categories_page = categories_paginator.get_page(categories_page_number)
        context["categories"] = categories
        context["categories_page"] = categories_page
        context["categories_page_range"] = get_page_range(categories_page)
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
        books = selected_category.books.all()
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 18)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        context["category"] = selected_category
        context["theme"] = PageTheme.objects.get(slug="books")
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context