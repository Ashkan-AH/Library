from .forms import BookForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Books
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