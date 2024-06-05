from .forms import BookForm, UpdateUserForm, CreateUserForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Books
from .models import User
from .mixins import StaffAccessMixin, SuperuserAccessMixin

def home(request):
    return render(request, "account/home.html")

class BookDetail(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/book_detail.html"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Books, slug=slug)


class BookList(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  ListView):
    template_name = "account/books_list.html"
    queryset = Books.objects.all()

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

class BookCreate(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  CreateView):
    model = Books
    form_class = BookForm
    success_url = reverse_lazy("account:books")
    template_name = "account/book-create-update.html"


class BookUpdate(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin,  UpdateView):
    model = Books
    form_class = BookForm
    template_name = "account/book-create-update.html"
    success_url = reverse_lazy("account:book-detail")


class BookDelete(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DeleteView):
    model = Books
    template_name = "account/books_comfirm_delete.html"
    success_url = reverse_lazy("account:books")


class BookPreview(LoginRequiredMixin, StaffAccessMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/book_preview.html"
    def get_object(self):
        return get_object_or_404(Books, slug=self.kwargs.get("slug"))
    

class UserList(LoginRequiredMixin, SuperuserAccessMixin, ListView):
    model = User
    template_name = "account/users_list.html"


class UserDetail(LoginRequiredMixin, SuperuserAccessMixin, DetailView):
    template_name = "account/user_detail.html"
    def get_object(self):
        id = self.kwargs.get('pk')
        if id != self.request.user.id:
            user = get_object_or_404(User, id=id)
        else:
            raise Http404
        return user


class UserCreate(LoginRequiredMixin, SuperuserAccessMixin, CreateView):
    model = User
    template_name = "account/create-update-user.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("account:users")

class UserUpdate(LoginRequiredMixin, SuperuserAccessMixin, UpdateView):
    model = User
    template_name = "account/create-update-user.html"
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
    template_name = "account/users_comfirm_delete.html"
    success_url = reverse_lazy("account:users")


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "account/profile_update.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("account:home")
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    def get_form_kwargs(self):
        kwargs = super(ProfileUpdate, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs