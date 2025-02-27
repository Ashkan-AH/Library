from django.db.models.base import Model as Model
from datetime import timedelta

from django.db.models.query import QuerySet
from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from books.models import Books, Category, Comment
from author.models import Author
from .models import User, PageTheme
from .mixins import *
from django.core.paginator import Paginator
from reservation.models import Reservation
from django.http import HttpResponse, Http404
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

#ALL
@login_required
def identifier(request):
    if request.user.is_superuser or request.user.is_staff:
        return HttpResponseRedirect(reverse_lazy("account:admin-index"))
    else:
        return HttpResponseRedirect(reverse_lazy("account:user-index"))
    

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "registration/signup.html"
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'تایید ایمیل.'
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = user.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لطفا با لینک ارسال شده ایمیلتان را تایید کنید تا فرایند ثبت نام تکمیل شود.')



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        context = {"is_valid": True}
    else:
        context = {"is_valid": False}
    return render(request, "registration/confirmation.html", context)
    

#USER
class UserProfile(LoginRequiredMixin, UserAccessMixin, TemplateView):
    template_name = "account/user/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        reserved_books = self.request.user.reservations.filter(status="رزرو شده")
        reserved_books_page_number = self.request.GET.get("reserved_books_page", 1)
        reserved_books_paginator = Paginator(reserved_books, 10)
        reserved_books_page = reserved_books_paginator.get_page(reserved_books_page_number)
        
        delivered_books = self.request.user.reservations.filter(status="تحویل داده شده")
        delivered_books_page_number = self.request.GET.get("delivered_books_page", 1)
        delivered_books_paginator = Paginator(delivered_books, 10)
        delivered_books_page = delivered_books_paginator.get_page(delivered_books_page_number)
        
        reservations = self.request.user.reservations.all()
        reservations_page_number = self.request.GET.get("reservations_page", 1)
        reservations_paginator = Paginator(reservations, 15)
        reservations_page = reservations_paginator.get_page(reservations_page_number)
        
        waiting_books = self.request.user.books.all()
        waiting_books_page_number = self.request.GET.get("waiting_books_page", 1)
        waiting_books_paginator = Paginator(waiting_books, 15)
        waiting_books_page = waiting_books_paginator.get_page(waiting_books_page_number)

        context["reserved_books_page"] = reserved_books_page
        context["reserved_books_page_range"] = get_page_range(reserved_books_page)
        

        context["delivered_books_page"] = delivered_books_page
        context["delivered_books_page_range"] = get_page_range(delivered_books_page)
        

        context["reservations_page"] = reservations_page
        context["reservations_page_range"] = get_page_range(reservations_page)
        

        context["waiting_books_page"] = waiting_books_page
        context["waiting_books_page_range"] = get_page_range(waiting_books_page)
        
        
        context["reserved_books_count"] = reserved_books.count
        context["delivered_books_count"] = delivered_books.count


        context["footer"] = PageTheme.objects.get(slug="footer")
        return context


class UserProfileUpdate(UserAccessMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "account/user/update_profile.html"
    form_class = UpdateProfileForm
    success_url = reverse_lazy("account:user-index")
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context


class UserBookmarkList(UserAccessMixin, LoginRequiredMixin, ListView):
    template_name = "account/user/bookmarks.html"
    def get_queryset(self):
        return Books.objects.filter(bookmarks__in=[self.request.user.id])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Books.objects.filter(bookmarks__in=[self.request.user.id])
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 9)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context


#ADMIN
class AdminIndex(LoginRequiredMixin, StaffAccessMixin, TemplateView):
    template_name = "account/admin/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.order_by("-date_joined").all()[0:16]
        context["blocked_users"] = User.objects.order_by("-date_joined").filter(is_active=False)[0:16]
        context["books"] = Books.objects.order_by("-date_uploaded").all()[0:5]
        context["waiting_books"] = Books.objects.order_by("-date_uploaded").exclude(waiting_users__isnull=True)[0:5]
        context["authors"] = Author.objects.order_by("-date_added").all()[0:5]
        context["users_count"] = User.objects.all().count()
        context["books_count"] = Books.objects.all().count()
        context["admins_count"] = User.objects.filter(Q(is_staff=True)|Q(is_superuser=True)).count()
        context["reservations_count"] = Reservation.objects.filter(status="بازگردانده شده").count()
        context["reservations"] = Reservation.objects.order_by("-date_added").all()[0:5]
        return context
    

def search_item(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        results = []
        if query.isnumeric():
            query = int(query)
            if request.user.view_books:
                for item in Books.objects.filter(id__startswith=query):
                    results.append({"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"book"})
            if request.user.view_authors:
                for item in Author.objects.filter(id__startswith=query):
                    results.append({"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"author"})
            if request.user.view_categories:
                for item in Category.objects.filter(id__startswith=query):
                    results.append({"name":item.name, "picture":item.picture.url, "slug":item.slug, "type":"category"})
            if request.user.view_users:
                for item in User.objects.filter(id__startswith=query):
                    user_dict = {"username":item.username, "picture":item.picture.url, "id":item.id, "type":"user"}
                if item.is_superuser:
                    user_dict["role"] = "ابر ادمین"
                elif item.is_staff:
                    user_dict["role"] = "ادمین"
                else:
                    user_dict["role"] = item.role
                results.append(user_dict)
            if request.user.view_reservations:
                for item in Reservation.objects.filter(reservation_id__startswith=query):
                    results.append({"id":item.reservation_id, "type":"reservation"})
                
        else:
            if request.user.view_books:
                for item in Books.objects.filter(Q(name__icontains=query) | Q(publisher__icontains=query) | Q(translator__icontains=query)):
                    results.append({"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"book"})
            if request.user.view_authors:
                for item in Author.objects.filter(name__icontains=query):
                    results.append({"name":item.name, "description":item.description, "picture":item.picture.url, "slug":item.slug, "type":"author"})
            if request.user.view_categories:
                for item in Category.objects.filter(name__icontains=query):
                    results.append({"name":item.name, "picture":item.picture.url, "slug":item.slug, "type":"category"})
            if request.user.view_users:
                for item in User.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(username__icontains=query)):
                    user_dict = {"username":item.username, "picture":item.picture.url, "id":item.id, "type":"user"}
                    if item.is_superuser:
                        user_dict["role"] = "ابر ادمین"
                    elif item.is_staff:
                        user_dict["role"] = "ادمین"
                    else:
                        user_dict["role"] = item.role
                    results.append(user_dict)
   
    return JsonResponse(results, safe=False)


@login_required
def search_result(request):
    
    search = request.GET.get('search', "")
    if search:
        if search.isnumeric():
            search = int(search)
            if request.user.view_authors:
                authors = Author.objects.filter(id__startswith=search)
            else:
                authors = Author.objects.none()
            if request.user.view_books:
                books = Books.objects.filter(id__startswith=search)
            else:
                books = Books.objects.none()
            if request.user.view_users:
                users = User.objects.filter(id__startswith=search)
            else:
                users = User.objects.none()
            if request.user.view_categories:
                categories = Category.objects.filter(id__startswith=search)
            else:
                categories = Category.objects.none()
            if request.user.view_reservations:
                reservations = Reservation.objects.filter(reservation_id__startswith=search)
            else:
                reservations = Reservation.objects.none()
        else:
            if request.user.view_authors:
                authors = Author.objects.filter(name__icontains=search)
            else:
                authors = Author.objects.none()

            if request.user.view_books:
                books = Books.objects.filter(Q(name__icontains=search) | Q(publisher__icontains=search) | Q(translator__icontains=search))
            else:
                books = Books.objects.none()

            if request.user.view_users:
                users = User.objects.filter(Q(username__icontains=search) | Q(last_name__icontains=search) | Q(first_name__icontains=search))
            else:
                users = User.objects.none()

            if request.user.view_categories:
                categories = Category.objects.filter(name__icontains=search)
            else:
                categories = Category.objects.none()

            reservations = Reservation.objects.none()

    else:
        authors = Author.objects.none()
        books = Books.objects.none()
        categories = Category.objects.none()
        reservations = Reservation.objects.none()
        users = User.objects.none()

        
    books_page_number = request.GET.get("books_page", 1)
    books_paginator = Paginator(books, 12)
    books_page = books_paginator.get_page(books_page_number)


    users_page_number = request.GET.get("users_page", 1)
    users_paginator = Paginator(users, 12)
    users_page = users_paginator.get_page(users_page_number)


    reservations_page_number = request.GET.get("reservations_page", 1)
    reservations_paginator = Paginator(reservations, 12)
    reservations_page = reservations_paginator.get_page(reservations_page_number)

    
    authors_page_number = request.GET.get("authors_page", 1)
    authors_paginator = Paginator(authors, 12)
    authors_page = authors_paginator.get_page(authors_page_number)

    
    categories_page_number = request.GET.get("categories_page", 1)
    categories_paginator = Paginator(categories, 12)
    categories_page = categories_paginator.get_page(categories_page_number)

    context = {
    "books_page": books_page, 
    "books_page_range": get_page_range(books_page),

    "reservations_page": reservations_page, 
    "reservations_page_range": get_page_range(reservations_page),

    "users_page": users_page, 
    "users_page_range": get_page_range(users_page),

    "authors_page": authors_page, 
    "authors_page_range": get_page_range(authors_page),

    "categories_page": categories_page, 
    "categories_page_range": get_page_range(categories_page),

    "search_text": search, 
    }
    return render(request, "account/admin/search_result.html", context)


def get_page_range(page_obj):
    index = page_obj.number - 1
    max_index = len(page_obj.paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    return page_obj.paginator.page_range[start_index:end_index]


class AdminProfileUpdate(StaffAccessMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "account/admin/users/user_update.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("account:admin-profile")
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(id=self.request.user.id)
        return context
    

class AdminProfile(StaffAccessMixin, LoginRequiredMixin, DetailView):
    template_name = "account/admin/users/user_detail.html"
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.filter(Q(user=self.request.user.id)).order_by("status")
        return context
        

class AdminBookmarkList(StaffAccessMixin, LoginRequiredMixin, ListView):
    template_name = "account/admin/bookmarks_list.html"
    def get_queryset(self):
        return Books.objects.filter(bookmarks__in=[self.request.user.id])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Books.objects.filter(bookmarks__in=[self.request.user.id])
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 24)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        return context
        
    
class WaitingList(StaffAccessMixin, LoginRequiredMixin, ListView):
    template_name = "account/admin/waiting_list.html"
    def get_queryset(self):
        return Books.objects.exclude(waiting_users__isnull=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Books.objects.exclude(waiting_users__isnull=True)
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 15)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        return context
    

class CreationView(LoginRequiredMixin, StaffAccessMixin, TemplateView):
    template_name = "account/admin/creation.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = RegistrationForm
        context["author_form"] = AuthorForm
        context["book_form"] = BookForm
        context["category_form"] = CategoryForm
        context["reservation_form"] = ReservationForm
        context["comment_form"] = CommentForm
        return context

#----------------------------------Books----------------------------------------
class BookList(LoginRequiredMixin, StaffAccessMixin, ViewBooksAccessMixin, ListView):
    template_name = "account/admin/books/books_list.html"
    model = Books
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Books.objects.all()
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 24)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        return context


class BookDetail(LoginRequiredMixin, StaffAccessMixin, ViewBooksAccessMixin, DetailView):
    template_name = "account/admin/books/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Books, slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        book = get_object_or_404(Books, slug=slug)
        context["reading_number"] = book.reservations.filter(status="تحویل داده شده").count()
        comments = book.comments.all()
        comments_page_number = self.request.GET.get("comments_page", 1)
        comments_paginator = Paginator(comments, 10)
        comments_page = comments_paginator.get_page(comments_page_number)
        context["comments"] = comments
        context["comments_page"] = comments_page
        context["comments_page_range"] = get_page_range(comments_page)
        return context
    

class BookCreate(LoginRequiredMixin, StaffAccessMixin, CreateBooksAccessMixin, CreateView):
    model = Books
    form_class = BookForm
    success_url = reverse_lazy("account:books")


class BookUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateBooksAccessMixin, UpdateView):
    model = Books
    form_class = BookForm
    template_name = "account/admin/books/book_update.html"
    def get_success_url(self):
        slug = self.kwargs.get("slug")
        return reverse_lazy("account:book-detail", kwargs={"slug": slug})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["book"] = Books.objects.get(slug=slug)
        return context


class BookDelete(LoginRequiredMixin, StaffAccessMixin, DeleteBooksAccessMixin, DeleteView):
    model = Books
    template_name = "account/admin/books/book_confirm_delete.html"
    success_url = reverse_lazy("account:books")

#----------------------------------Categories-----------------------------------
class CategoryList(LoginRequiredMixin, StaffAccessMixin, ViewCategoriesAccessMixin, ListView):
    template_name = "account/admin/categories/categories_list.html"
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        categories_page_number = self.request.GET.get("categories_page", 1)
        categories_paginator = Paginator(categories, 18)
        categories_page = categories_paginator.get_page(categories_page_number)
        context["categories"] = categories
        context["categories_page"] = categories_page
        context["categories_page_range"] = get_page_range(categories_page)
        return context
    

class CategoryDetail(LoginRequiredMixin, StaffAccessMixin, ViewCategoriesAccessMixin, DetailView):
    template_name = "account/admin/categories/category_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return Category.objects.get(slug=slug)
    

class CategoryBooksList(LoginRequiredMixin, StaffAccessMixin, ViewCategoriesAccessMixin, ListView):
    template_name = "account/admin/books/books_list.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Books.objects.filter(category__slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        books = Books.objects.filter(category__slug=slug)
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 18)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        context["category"] = Category.objects.get(slug=slug)
        return context
    

class CategoryCreate(LoginRequiredMixin, StaffAccessMixin, CreateCategoriesAccessMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("account:categories")


class CategoryUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateCategoriesAccessMixin, UpdateView):
    model = Category
    template_name = "account/admin/categories/category_update.html"
    form_class = CategoryForm
    def get_success_url(self):
        slug = self.kwargs.get("slug")
        return reverse_lazy("account:category-detail", kwargs={"slug": slug})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["category"] = Category.objects.get(slug=slug)
        return context


class CategoryDelete(LoginRequiredMixin, StaffAccessMixin, DeleteCategoriesAccessMixin, DeleteView):
    model = Category
    template_name = "account/admin/categories/category_confirm_delete.html"
    success_url = reverse_lazy("account:categories")


#----------------------------------Authors--------------------------------------
class AuthorList(LoginRequiredMixin, StaffAccessMixin, ViewAuthorsAccessMixin, ListView):
    template_name = "account/admin/authors/authors_list.html"
    model = Author
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        authors_page_number = self.request.GET.get("authors_page", 1)
        authors_paginator = Paginator(authors, 24)
        authors_page = authors_paginator.get_page(authors_page_number)
        context["authors"] = authors
        context["authors_page"] = authors_page
        context["authors_page_range"] = get_page_range(authors_page)
        return context
    

class AuthorDetail(LoginRequiredMixin, StaffAccessMixin, ViewAuthorsAccessMixin, DetailView):
    template_name = "account/admin/authors/author_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)
    

class AuthorBooksList(LoginRequiredMixin, StaffAccessMixin, ViewAuthorsAccessMixin, ListView):
    template_name = "account/admin/books/books_list.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Books.objects.filter(author__slug=slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        books = Books.objects.filter(author__slug=slug)
        books_page_number = self.request.GET.get("books_page", 1)
        books_paginator = Paginator(books, 24)
        books_page = books_paginator.get_page(books_page_number)
        context["books"] = books
        context["books_page"] = books_page
        context["books_page_range"] = get_page_range(books_page)
        context["author"] = Author.objects.get(slug=slug)
        return context


class AuthorCreate(LoginRequiredMixin, StaffAccessMixin, CreateAuthorsAccessMixin, CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("account:authors")


class AuthorUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateAuthorsAccessMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "account/admin/authors/author_update.html"
    def get_success_url(self):
        slug = self.kwargs.get("slug")
        return reverse_lazy("account:author-detail", kwargs={"slug": slug})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["author"] = Author.objects.get(slug=slug)
        return context


class AuthorDelete(LoginRequiredMixin, StaffAccessMixin, DeleteAuthorsAccessMixin, DeleteView):
    model = Author
    template_name = "account/admin/authors/author_confirm_delete.html"
    success_url = reverse_lazy("account:authors")

#----------------------------------Users----------------------------------------
class UserList(LoginRequiredMixin, StaffAccessMixin, ViewUsersAccessMixin, ListView):
    template_name = "account/admin/users/users_list.html"
    def get_queryset(self):
        return User.objects.filter(~Q(id = self.request.user.id))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.filter(~Q(id = self.request.user.id))
        users_page_number = self.request.GET.get("users_page", 1)
        users_paginator = Paginator(users, 12)
        users_page = users_paginator.get_page(users_page_number)
        context["users"] = users
        context["users_page"] = users_page
        context["users_page_range"] = get_page_range(users_page)
        return context


class UserDetail(LoginRequiredMixin, StaffAccessMixin, ViewUsersAccessMixin, DetailView):
    template_name = "account/admin/users/user_detail.html"
    def get_object(self):
        global id
        id = self.kwargs.get('pk')
        if id != self.request.user.id:
            return get_object_or_404(User, id=id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.filter(Q(user=id)).order_by("status")
        return context


class UserCreate(LoginRequiredMixin, StaffAccessMixin, CreateUsersAccessMixin, CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy("account:users")


class UserUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateUsersAccessMixin, UpdateView):
    model = User
    template_name = "account/admin/users/user_update.html"
    form_class = UpdateUserForm
    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("account:user-detail", kwargs={"pk": pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["user"] = User.objects.get(id=pk)
        return context
    

class UserDelete(LoginRequiredMixin, StaffAccessMixin, DeleteUsersAccessMixin, DeleteView):
    model = User
    template_name = "account/admin/users/user_confirm_delete.html"
    success_url = reverse_lazy("account:users")


class BlackList(StaffAccessMixin, LoginRequiredMixin, ViewUsersAccessMixin, ListView):
    template_name = "account/admin/black_list.html"
    def get_queryset(self):
        return User.objects.filter(is_active=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.filter(is_active=False)
        users_page_number = self.request.GET.get("users_page", 1)
        users_paginator = Paginator(users, 12)
        users_page = users_paginator.get_page(users_page_number)
        context["users"] = users
        context["users_page"] = users_page
        context["users_page_range"] = get_page_range(users_page)
        return context

# ---------------------------------Reservation------------------------------
class ReservationList(LoginRequiredMixin, StaffAccessMixin, ViewReservationsAccessMixin, ListView):
    template_name = "account/admin/reservations/reservations_list.html"
    model = Reservation
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservations = Reservation.objects.all()
        reservations_page_number = self.request.GET.get("reservations_page", 1)
        reservations_paginator = Paginator(reservations, 15)
        reservations_page = reservations_paginator.get_page(reservations_page_number)
        context["reservations"] = reservations
        context["reservations_page"] = reservations_page
        context["reservations_page_range"] = get_page_range(reservations_page)
        return context


class ReservationDetail(LoginRequiredMixin, StaffAccessMixin, ViewReservationsAccessMixin, DetailView):
    template_name = "account/admin/reservations/reservation_detail.html"
    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Reservation, reservation_id=id)


class ReservationCreate(LoginRequiredMixin, StaffAccessMixin, CreateReservationsAccessMixin, CreateView):
    model = Reservation
    template_name = "account/admin/reservations/reservation_create.html"
    form_class = ReservationForm
    success_url = reverse_lazy("account:reservations")
    

class ReservationDelete(LoginRequiredMixin, StaffAccessMixin, DeleteReservationsAccessMixin, DeleteView):
    model = Reservation
    template_name = "account/admin/reservations/reservation_confirm_delete.html"
    success_url = reverse_lazy("account:reservations")

    
class ExtendList(StaffAccessMixin, ViewReservationsAccessMixin, LoginRequiredMixin, ListView):
    template_name = "account/admin/reservations/extends_list.html"
    def get_queryset(self):
        return Reservation.objects.filter(Q(extend_request=True), Q(extend_sluts__gt=0), Q(status="تحویل داده شده"))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservations = Reservation.objects.filter(Q(extend_request=True), Q(extend_sluts__gt=0), Q(status="تحویل داده شده"))
        reservations_page_number = self.request.GET.get("reservations_page", 1)
        reservations_paginator = Paginator(reservations, 15)
        reservations_page = reservations_paginator.get_page(reservations_page_number)
        context["reservations"] = reservations
        context["reservations_page"] = reservations_page
        context["reservations_page_range"] = get_page_range(reservations_page)
        return context
    

@login_required
def delivered_action(request, pk):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_reservations:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        book = get_object_or_404(Books, id=reservation.book.id)
        if reservation.status == "رزرو شده":
            reservation.status = "تحویل داده شده"
            book.in_stock -= 1
            reservation.delivery_date = timezone.now().date()
            reservation.deadline = (timezone.now().date() + timedelta(days=14))
            reservation.save()
            book.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")
    

@login_required
def cancel_action(request, pk):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_reservations:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        user = User.objects.get(id=reservation.user.id)
        book = get_object_or_404(Books, id=reservation.book.id)
        if reservation.status == "رزرو شده":
            reservation.status = "لغو رزرو"
            user.reservation_limit += 1
            book.in_stock_user += 1
            Books.in_stock_email(book)
            user.save()
            reservation.save()
            book.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")
    

@login_required
def returned_action(request, pk):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_reservations:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        book = get_object_or_404(Books, id=reservation.book.id)
        user = User.objects.get(id=reservation.user.id)
        if reservation.status == "تحویل داده شده" or reservation.status == "بازگردانده نشده":
            user.reservation_limit += 1
            user.save()
            reservation.status = "بازگردانده شده"
            reservation.save()
            book.in_stock_user += 1
            book.in_stock += 1
            Books.in_stock_email(book)
            book.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")
    

@login_required
def extend_action(request, pk):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_reservations:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        if reservation.status == "تحویل داده شده" and reservation.extend_request == True and reservation.extend_sluts > 0:
            reservation.deadline += timedelta(days=14)
            reservation.extend_sluts -= 1
            reservation.extend_request = False
            reservation.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")
    
#--------------------------------Themes--------------------------------------
class ThemeList(StaffAccessMixin, UpdateThemeAccessMixin, LoginRequiredMixin, ListView):
    model = PageTheme
    template_name = "account/admin/themes/themes_list.html"

    
class ThemeUpdate(StaffAccessMixin, UpdateThemeAccessMixin, LoginRequiredMixin, UpdateView):
    template_name = "account/admin/themes/theme_update.html"
    model = PageTheme
    form_class = UpdateThemeForm
    def get_success_url(self):
        slug = self.kwargs.get("slug")
        return reverse_lazy("account:theme-update", kwargs={"slug": slug})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["theme"] = PageTheme.objects.get(slug=slug)
        return context
    

class ThemeDetail(StaffAccessMixin, UpdateThemeAccessMixin, LoginRequiredMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return PageTheme.objects.get(slug=slug)
    
    def get_template_names(self):
        slug = self.kwargs.get("slug")
        theme = PageTheme.objects.get(slug=slug)
        if slug == "index":
            return ["account/admin/themes/index.html"]
        elif slug == "search-result":
            return ["account/admin/themes/search_result.html"]
        elif slug == "categories":
            return ["account/admin/themes/categories.html"]
        elif slug == "authors":
            return ["account/admin/themes/authors.html"]
        elif slug == "books":
            return ["account/admin/themes/books.html"]
        elif slug == "footer":
            return ["account/admin/themes/footer.html"]
        raise Http404("چنین صفحه ای یافت نشد.")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        context["theme"] = PageTheme.objects.get(slug=slug)
        context["footer"] = PageTheme.objects.get(slug="footer")
        return context

#-------------------------------Comments-------------------------------------
class CommentList(StaffAccessMixin, ViewCommentsAccessMixin, LoginRequiredMixin, ListView):
    model = Comment
    template_name = "account/admin/comments/comments_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.all()
        comments_page_number = self.request.GET.get("comments_page", 1)
        comments_paginator = Paginator(comments, 15)
        comments_page = comments_paginator.get_page(comments_page_number)
        context["comments"] = comments
        context["comments_page"] = comments_page
        context["comments_page_range"] = get_page_range(comments_page)
        return context


class CommentDetail(StaffAccessMixin, ViewCommentsAccessMixin, LoginRequiredMixin, DetailView):
    template_name = "account/admin/comments/comment_detail.html"
    def get_object(self):
        id = self.kwargs.get("id")
        return Comment.objects.get(id=id)
    


class CommentCreate(StaffAccessMixin, CreateCommentsAccessMixin, LoginRequiredMixin, CreateView):
    model=Comment
    form_class = CommentForm
    success_url="account:comments"


class CommentUpdate(StaffAccessMixin, UpdateCommentsAccessMixin, LoginRequiredMixin, UpdateView):
    model=Comment
    form_class = CommentForm
    template_name = "account/admin/comments/comment_update.html"
    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("account:comment-detail", kwargs={"id": pk})
        

class CommentDelete(LoginRequiredMixin, DeleteView):
    success_url = "account:comments"
    def get_object(self):
        pk = self.kwargs.get("pk")
        comment = Comment.objects.get(id=pk)
        if ((self.request.user.is_staff or self.request.user.is_superuser) and self.request.user.delete_comments) or self.request.user == comment.user:
            return comment
        return Http404("شما اجازه انجام این کار را ندارید.")
    
    def get_template_names(self):
        pk = self.kwargs.get("pk")
        comment = Comment.objects.get(id=pk)
        if (self.request.user is comment.user and (self.request.user.is_staff or self.request.user.is_superuser)) or ((self.request.user.is_staff or self.request.user.is_superuser) and self.request.user.delete_comments):
            return ["account/admin/comments/comment_confirm_delete.html"]
        elif self.request.user == comment.user:
            return ["account/user/comment_confirm_delete.html"]
        raise Http404("شما اجازه انجام این کار را ندارید.")


@login_required
def confirm_action(request, id):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_comments:
        comment = Comment.objects.get(id=id) 
        comment.status = "تایید شده"       
        comment.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")


@login_required
def reject_action(request, id):
    if (request.user.is_staff or request.user.is_superuser) and request.user.update_comments:
        comment = Comment.objects.get(id=id) 
        comment.status = "رد شده"       
        comment.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise Http404("اجازه انجام این کار را ندارید.")