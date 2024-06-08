from django import forms
from django.contrib.auth.forms import UserCreationForm
from books.models import Books, Category
from author.models import Author
from .models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["slug"]


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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2", "email", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "is_superuser", "is_staff", "is_active"]


class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].help_text = True
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['national_code'].disabled = True
            self.fields['is_superuser'].disabled = True
            self.fields['is_staff'].disabled = True
            self.fields['is_active'].disabled = True
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "address", "national_code", "sel_number", "home_number", "picture", "birth_date", "is_superuser", "is_staff", "is_active"]