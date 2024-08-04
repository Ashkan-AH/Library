from django import forms
from django.contrib.auth.forms import UserCreationForm
from books.models import Books, Category
from author.models import Author
from reservation.models import Reservation
from .models import User
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["slug", "bookmarks", "waiting_users"]


class SearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=150, label="جستجو")


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "picture", "description"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["book_id", "user_id", "status", "delivery_date", "extend_sluts"]

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
        fields = [ "first_name", "last_name", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "is_superuser", "is_staff", "is_active", "fathers_name", "birth_number", "emergency_number", "role", "reservation_limit"]

class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields["birth_date"] = JalaliDateField(label="تاریخ تولد", widget=AdminJalaliDateWidget)
    class Meta:
        model = User
        fields = [ "first_name", "last_name", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "fathers_name", "birth_number", "emergency_number", "role"]