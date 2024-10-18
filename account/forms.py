from django import forms
from django.contrib.auth.forms import UserCreationForm
from books.models import Books, Category, Comment
from author.models import Author
from reservation.models import Reservation
from .models import User, PageTheme
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from ckeditor.widgets import CKEditorWidget

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = CKEditorWidget(attrs={'id': "id_book_description"})
    class Meta:
        model = Books
        exclude = ["slug", "bookmarks", "waiting_users"]


class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=150, label="جستجو")


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "picture"]

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "rating", "user", "book", "status"]

        
class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = CKEditorWidget(attrs={'id': "id_author_description"})

    class Meta:
        model = Author
        fields = ["name", "picture", "description"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["book", "user", "extend_sluts"]

    def __init__(self, *args, **kwargs):
        signal = 0
        if "update" in kwargs:
            signal = kwargs.pop("update")
        
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['delivery_date'] = JalaliDateField(required=False, label=('تاریخ تحویل کتاب'),
            widget=AdminJalaliDateWidget
        )
        if signal:
            self.fields["status"].disabled = True

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # fields = ["username", "first_name", "last_name", "email", "address", "national_code", "sel_number", "home_number", "birth_date", "fathers_name", "birth_number", "emergency_number", "role", "st_id", "st_major", "st_grade", "co_id", "co_unit", "co_grade", "pro_id", "pro_major", "pro_grade", "picture"]
    



class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields["birth_date"] = JalaliDateField(label="تاریخ تولد", widget=AdminJalaliDateWidget)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "address", "birth_number", "national_code", "fathers_name", "sel_number", "home_number", "emergency_number", "birth_date", "picture", "reservation_limit", "is_active", "is_staff", "is_superuser", "role", "st_id", "st_major", "st_grade", "emp_id", "emp_unit", "emp_grade", "pro_id", "pro_major", "pro_grade", "view_books", "view_authors", "view_reservations", "view_users", "view_categories", "update_books", "update_authors", "update_reservations", "update_users", "update_categories", "create_books", "create_authors", "create_reservations", "create_users", "create_categories", "delete_books", "delete_authors", "delete_reservations", "delete_users", "delete_categories",]

class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields["birth_date"] = JalaliDateField(label="تاریخ تولد", widget=AdminJalaliDateWidget)
    class Meta:
        model = User
        fields = [ "first_name", "last_name", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "fathers_name", "birth_number", "emergency_number", "role", "st_id", "st_major", "st_grade", "emp_id", "emp_unit", "emp_grade", "pro_id", "pro_major", "pro_grade"]


class UpdateThemeForm(forms.ModelForm):
    class Meta:
        model = PageTheme
        exclude = ["name", "slug", "thumbnail"]