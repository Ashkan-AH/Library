from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Books, Category
from author.models import Author
from .models import User
from .mixins import StaffAccessMixin, SuperuserAccessMixin

#----------------------------------Books-------------------------------------------

class BookDetail(LoginRequiredMixin, StaffAccessMixin, DetailView):
    template_name = "account/books/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Books, slug=slug)


class BookList(LoginRequiredMixin, StaffAccessMixin, ListView):
    template_name = "account/books/books_list.html"
    def get_queryset(self):
        global searchForm
        searchForm = SearchForm(self.request.GET)
        if searchForm.is_valid():
            data = searchForm.cleaned_data["search"]
            if data.isdecimal():
                data = int(searchForm.cleaned_data["search"])
                return Books.objects.filter(id=data)
            return Books.objects.filter(Q(name__icontains=data) | Q(author__name__icontains=data) | Q(publisher__icontains=data) | Q(translator__icontains=data) | Q(description__icontains=data))
        return Books.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchForm"] = searchForm
        return context


class BookCreate(LoginRequiredMixin, StaffAccessMixin, CreateView):
    model = Books
    form_class = BookForm
    success_url = reverse_lazy("account:books")
    template_name = "account/books/book_create_update.html"


class BookUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateView):
    model = Books
    form_class = BookForm
    template_name = "account/books/book_create_update.html"
    success_url = reverse_lazy("account:books")


class BookDelete(LoginRequiredMixin, StaffAccessMixin, DeleteView):
    model = Books
    template_name = "account/books/book_comfirm_delete.html"
    success_url = reverse_lazy("account:books")


class BookPreview(LoginRequiredMixin, StaffAccessMixin, DetailView):
    template_name = "account/books/book_preview.html"
    def get_object(self):
        return get_object_or_404(Books, slug=self.kwargs.get("slug"))
    

# def bookList(request):
#     searchForm = BookSearch(request.GET)
#     if searchForm.is_valid():
#         data = searchForm.cleaned_data["bookSearch"]
#         object_list = Books.objects.filter(Q(name__icontains=data) | Q(author__name__icontains=data) | Q(publisher__icontains=data) | Q(translator__icontains=data) | Q(category__name__icontains=data))
#     else:
#         object_list = Books.objects.all()
#     context = {
#         "searchForm": searchForm, 
#         "object_list": object_list,
#     }
#     return render(request, "account/books/books_list.html", context)

# def bookCreate(request):
#     if request.method == "POST":
#         bookForm = BookForm(request.POST)
#         if bookForm.is_valid():
#             bookForm.save()
#             return HttpResponseRedirect(reverse("account:books"))
#     else:
#         bookForm = BookForm()

#     context = {"bookForm": bookForm, }
#     return render(request, "account/book-create-update.html", context)


# def bookUpdate(request, slug):
#     book = Books.objects.get(slug=slug)
#     if request.method == "POST":
#         bookForm = BookForm(request.POST, instance=book)
#         if bookForm.is_valid():
#             bookForm.save()
#             return HttpResponseRedirect(reverse("account:books"))
#     else:
#         bookForm = BookForm(instance=book)

#     context = {"bookForm": bookForm, }
#     return render(request, "account/book-create-update.html", context)

#----------------------------------Categories--------------------------------------

class CategoryCreate(LoginRequiredMixin, StaffAccessMixin, CreateView):
    model = Category
    template_name = "account/categories/category_create_update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("account:categories")


class CategoryUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateView):
    model = Category
    template_name = "account/categories/category_create_update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("account:categories")


class CategoryDelete(LoginRequiredMixin, StaffAccessMixin, DeleteView):
    model = Category
    template_name = "account/categories/category_confirm_delete.html"
    success_url = reverse_lazy("account:categories")



class CategoryList(LoginRequiredMixin, StaffAccessMixin, ListView):
    template_name = "account/categories/categories_list.html"
    def get_queryset(self):
        global searchForm
        searchForm = SearchForm(self.request.GET)
        if searchForm.is_valid():
            data = searchForm.cleaned_data["search"]
            if data.isdecimal():
                data = int(searchForm.cleaned_data["search"])
                return Category.objects.filter(id=data)
            return Category.objects.filter(name__icontains=data)
        return Category.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchForm"] = searchForm
        return context

#----------------------------------Authors-----------------------------------------


class AuthorCreate(LoginRequiredMixin, StaffAccessMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "account/authors/author_create_update.html"
    success_url = reverse_lazy("account:authors")



class AuthorUpdate(LoginRequiredMixin, StaffAccessMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "account/authors/author_create_update.html"
    success_url = reverse_lazy("account:authors")



class AuthorDelete(LoginRequiredMixin, StaffAccessMixin, DeleteView):
    model = Author
    template_name = "account/authors/author_confirm_delete.html"
    success_url = reverse_lazy("account:authors")



    
class AuthorDetail(LoginRequiredMixin, StaffAccessMixin, DetailView):
    template_name = "account/authors/author_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=slug)



class AuthorList(LoginRequiredMixin, StaffAccessMixin, ListView):
    template_name = "account/authors/authors_list.html"
    def get_queryset(self):
        global searchForm
        searchForm = SearchForm(self.request.GET)
        if searchForm.is_valid():
            data = searchForm.cleaned_data["search"]
            if data.isdecimal():
                data = int(searchForm.cleaned_data["search"])
                return Author.objects.filter(id=data)
            return Author.objects.filter(Q(name__icontains=data) | Q(description__icontains=data))
        return Author.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchForm"] = searchForm
        return context


#----------------------------------Users-------------------------------------------

class UserList(LoginRequiredMixin, SuperuserAccessMixin, ListView):
    template_name = "account/users/users_list.html"
    def get_queryset(self):
        global searchForm
        searchForm = SearchForm(self.request.GET)
        if searchForm.is_valid():
            data = searchForm.cleaned_data["search"]
            if data.isdecimal():
                data = int(searchForm.cleaned_data["search"])
                return User.objects.filter(id=data)
            return User.objects.filter(Q(username__icontains=data) | Q(national_code=data) | Q(first_name__icontains=data) | Q(last_name__icontains=data) | Q(email__icontains=data) | Q(address__icontains=data) | Q(sel_number=data) | Q(home_number=data))
        return User.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchForm"] = searchForm
        return context


class UserDetail(LoginRequiredMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/users/user_detail.html"
    def get_object(self):
        id = self.kwargs.get('pk')
        if id != self.request.user.id:
            user = get_object_or_404(User, id=id)
        else:
            raise Http404
        return user


class UserCreate(LoginRequiredMixin, SuperuserAccessMixin, CreateView):
    model = User
    template_name = "account/users/user_create_update.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("account:users")

class UserUpdate(LoginRequiredMixin, SuperuserAccessMixin, UpdateView):
    model = User
    template_name = "account/users/user_create_update.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("account:users")
    def get_object(self):
        return User.objects.get(id=self.kwargs.get("pk"))
    def get_form_kwargs(self):
        kwargs = super(UserUpdate, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class UserDelete(LoginRequiredMixin, SuperuserAccessMixin, DeleteView):
    model = User
    template_name = "account/users/user_comfirm_delete.html"
    success_url = reverse_lazy("account:users")


#---------------------------------Profile------------------------------------------

class Profile(LoginRequiredMixin, DetailView):
    template_name = "account/profile.html"
    def get_object(self):
        id = self.request.user.id
        return get_object_or_404(User, id=id)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "account/profile_update.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("account:profile")
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    def get_form_kwargs(self):
        kwargs = super(ProfileUpdate, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs
    

class BookmarkList(LoginRequiredMixin, ListView):
    template_name = "account/bookmarks_list.html"
    def get_queryset(self):
        return Books.objects.filter(bookmarks__in=[self.request.user.id])