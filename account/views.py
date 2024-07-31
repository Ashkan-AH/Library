from .forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from books.models import Books, Category
from author.models import Author
from .models import User
from .mixins import StaffAccessMixin, SuperuserAccessMixin

from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

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
        global id
        id = self.kwargs.get('pk')
        if id != self.request.user.id:
            return get_object_or_404(User, id=id)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.filter(Q(user_id=id)).order_by("status")
        return context

class UserUpdate(LoginRequiredMixin, SuperuserAccessMixin, UpdateView):
    model = User
    template_name = "account/users/user_create_update.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("account:users")
    def get_object(self):
        return User.objects.get(id=self.kwargs.get("pk"))
    


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
    form_class = UpdateProfileForm
    success_url = reverse_lazy("account:profile")
    def get_object(self):
        return User.objects.get(id=self.request.user.id)
    
    

class BookmarkList(LoginRequiredMixin, ListView):
    template_name = "account/bookmarks_list.html"
    def get_queryset(self):
        return Books.objects.filter(bookmarks__in=[self.request.user.id])
    

# ---------------------------------Reservation------------------------------


class ReservationCreate(LoginRequiredMixin, StaffAccessMixin, CreateView):
    model = Reservation
    template_name = "account/reservations/reservation_create_update.html"
    form_class = ReservationForm
    success_url = reverse_lazy("account:reservations")
   



@login_required
def delivered_action(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        book = get_object_or_404(Books, id=reservation.book_id.id)
        if reservation.status == "رزرو شده":
            reservation.status = "تحویل داده شده"
            book.in_stock -= 1
            reservation.delivery_date = timezone.now()
            reservation.save()
            book.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise PermissionDenied("اجازه دیدن این صفحه را ندارید.")
    

@login_required
def cancel_action(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        user = User.objects.get(id=reservation.user_id.id)
        book = get_object_or_404(Books, id=reservation.book_id.id)
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
        raise PermissionDenied("اجازه دیدن این صفحه را ندارید.")
    

@login_required
def reserve_action(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        user = User.objects.get(id=reservation.user_id.id)
        book = get_object_or_404(Books, id=reservation.book_id.id)
        if reservation.status == "لغو رزرو":
            reservation.status = "رزرو شده"
            user.reservation_limit -= 1
            book.in_stock_user -= 1
            user.save()
            reservation.save()
            book.save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        raise PermissionDenied("اجازه دیدن این صفحه را ندارید.")
    

@login_required
def returned_action(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        reservation = get_object_or_404(Reservation, reservation_id=pk)
        book = get_object_or_404(Books, id=reservation.book_id.id)
        user = User.objects.get(id=reservation.user_id.id)
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
        raise PermissionDenied("اجازه دیدن این صفحه را ندارید.")
    

# @login_required
# def reservationCreate(request):
#     if request.user.is_staff or request.user.is_superuser:
#         if request.method == "POST":
#             reservationForm = ReservationForm(request.POST)
#             if reservationForm.is_valid():
#                 book_id = reservationForm.cleaned_data["book_id"]
#                 book = Books.objects.get(id=book_id.id)
#                 if book.in_stock > 0:
#                     book.in_stock -= 1
#                     book.save()
#                     reservationForm.save()
#                     return HttpResponseRedirect(reverse("account:reservations"))
#                 else:
#                     raise Http404("این کتاب موجود نیست.")
#         else:
#             reservationForm = ReservationForm()
#     else:
#         raise PermissionDenied("You can't see this page.")

#     context = {"reservationForm": reservationForm, }
#     return render(request, "account/reservations/reservation_create_update.html", context)

# @login_required
# def reservationUpdate(request, pk):
#     if request.user.is_staff or request.user.is_superuser:
#         reservation = Reservation.objects.get(pk=pk)
#         if request.method == "POST":
#             reservationForm = ReservationForm(request.POST, instance=reservation)
#             if reservationForm.is_valid():
#                 reservationForm.save()
#                 return HttpResponseRedirect(reverse("account:reservations"))
#         else:
#             reservationForm = ReservationForm(instance=reservation)
#     else:
#         raise PermissionDenied("You can't see this page.")

#     context = {"reservationForm": reservationForm, }
#     return render(request, "account/reservations/reservation_create_update.html", context)


class ReservationDelete(LoginRequiredMixin, StaffAccessMixin, DeleteView):
    model = Reservation
    template_name = "account/reservations/reservation_confirm_delete.html"
    success_url = reverse_lazy("account:reservations")


    
class ReservationDetail(LoginRequiredMixin, DetailView):
    template_name = "account/reservations/reservation_detail.html"
    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Reservation, reservation_id=id)


class ReservationList(LoginRequiredMixin, ListView):
    template_name = "account/reservations/reservation_list.html"
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            reservations = Reservation.objects.all()
            for reservation in reservations:
                Reservation.not_returned(reservation)
                Reservation.reservation_expired(reservation)
            return reservations
        else:
            reservations = Reservation.objects.filter(user_id=self.request.user.id)
            for reservation in reservations:
                Reservation.not_returned(reservation)
                Reservation.reservation_expired(reservation)
            return reservations

# ------------------------------Black List------------------------------------

class BlackList(SuperuserAccessMixin, LoginRequiredMixin, ListView):
    template_name = "account/black_list_users_list.html"
    def get_queryset(self):
        return User.objects.filter(is_active=False)
    
# -------------------------------Registration---------------------------------

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

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
    
# --------------------------------waiting-list-------------------------------
class WaitingList(LoginRequiredMixin, ListView):
    template_name = "account/waiting_list.html"
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Books.objects.exclude(waiting_users__isnull=True)
        else:
            return Books.objects.filter(waiting_users__in=[self.request.user.id])
