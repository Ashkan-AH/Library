from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from reservation.models import Reservation
from account.models import User
from author.models import Author
from .models import Books, Category
from account.forms import SearchForm

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
def reservation_add(request, book_id):
    book = Books.objects.get(id=book_id)
    user = User.objects.get(id=request.user.id)
    if Reservation.objects.filter(Q(book_id=book_id), Q(user_id=request.user.id), Q(status="رزرو شده")).exists():
        reservation = Reservation.objects.get(Q(book_id=book_id), Q(user_id=request.user.id), Q(status="رزرو شده"))
        reservation.status = "لغو رزرو"
        book.in_stock_user += 1
        user.reservation_limit += 1
        book.save()
        reservation.save()
        user.save()
    else:
        if book.in_stock_user > 0 and user.reservation_limit > 0:
            Reservation.objects.create(book_id=book, user_id=user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



def search_result(request):
    search = request.GET.get('search')
    context = {}
    context["books"] = Books.objects.filter(Q(name__icontains=search) | Q(publisher__icontains=search) | Q(translator__icontains=search))
    context["authors"] = Author.objects.filter(name__icontains=search)
    context["categories"] = Category.objects.filter(name__icontains=search)
    context["search_text"] = search
    return render(request, "search_result.html", context)





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
        return context



def index(request):
    context = {
        "books": [book for book in Books.objects.all().order_by("?")[0:8]],
        "authors": [author for author in Author.objects.all().order_by("?")[0:8]],
        "categories": [category for category in Category.objects.all()[0:4]],
        "books_number": Books.objects.all().count(),
        "reserve_number": Reservation.objects.filter(status="بازگردانده شده").count(),
        "users_number": User.objects.all().count(),
    }
    return render(request, "index.html", context)
    
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
        context["reservation"] = Reservation.objects.filter(Q(book_id=book1.id), Q(user_id=self.request.user.id), Q(status="تحویل داده شده")|Q(status="رزرو شده")).first()
        context["books"] = [book for book in Books.objects.filter(Q(category__in=(book1.category.all())), ~Q(slug=book1.slug)).order_by("?")[0:3]]
        return context
        
    

class CategoryList(ListView):
    paginate_by = 12
    template_name = "main/books/categories.html"
    model = Category
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
        return context