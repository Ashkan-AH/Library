import pandas as pd
from books.models import Books, Category
from author.models import Author

def import_books(file):
    if file.name.endswith(".xlsx"):
        data = pd.read_excel(file)
    elif file.name.endswith(".csv"):
        data = pd.read_csv(file)
    elif file.name.endswith(".json"):
        data = pd.read_json(file)
    else:
        raise ValueError("این نوع فایل پشتیبانی نمیشود.")
    data = data.fillna(value="")
    for _, row in data.iterrows():
        title = row["title"]
        cover_title = row["cover_title"]
        volume = row["volume"]
        author_objects = []
        if row["author"]:
            authors = row["author"].split("-")  
            for author_name in authors:
                author, created = Author.objects.get_or_create(name=author_name)
                author_objects.append(author)
        publisher = row["publisher"]
        translator = row["translator"]
        nli = row["nli"]
        ddc = row["ddc"]
        location = row["location"]
        isbn = row["isbn"]
        pub_year = row["pub_year"]
        edition = row["edition"]
        in_stock = row["in_stock"]
        llc = row["llc"]
        category = [row["llc"].split(" ")[0]] if row["llc"] else []

        book, created = Books.objects.get_or_create(title=title, cover_title=cover_title, volume=volume, publisher=publisher, translator=translator, nli=nli, ddc=ddc, location=location, isbn=isbn, pub_year=pub_year, edition=edition, llc=llc)
        book.title = title
        book.cover_title = cover_title
        book.volume = volume
        book.author_objects = author_objects
        book.publisher = publisher
        book.translator = translator
        book.nli = nli
        book.ddc = ddc
        book.location = location
        book.isbn = isbn
        book.pub_year = pub_year
        book.edition = edition
        book.in_stock = in_stock
        book.in_stock_user = in_stock
        book.llc = llc
        book.category = category
        book.save()


def import_categories(file):
    if file.name.endswith(".xlsx"):
        data = pd.read_excel(file)
    elif file.name.endswith(".csv"):
        data = pd.read_csv(file)
    elif file.name.endswith(".json"):
        data = pd.read_json(file)
    else:
        raise ValueError("این نوع فایل پشتیبانی نمیشود.")
    for ـ, row in data.iterrows():
        name = row["name"]
        llc = row["llc"]
        category, created = Category.objects.get_or_create(name=name, llc=llc)
        category.name = name
        category.llc = llc
        category.save()


def import_authors(file):
    if file.name.endswith(".xlsx"):
        data = pd.read_excel(file)
    elif file.name.endswith(".csv"):
        data = pd.read_csv(file)
    elif file.name.endswith(".json"):
        data = pd.read_json(file)
    else:
        raise ValueError("این نوع فایل پشتیبانی نمیشود.")
    for ـ, row in data.iterrows():
        name = row["name"]
        author, created = Author.objects.get_or_create(name=name)
        author.name = name
        author.save()


# # utils.py
# import pandas as pd
# from .models import Book, Author, Category

# def import_books(file):
#     data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)

#     for index, row in data.iterrows():
#         title = row['Title']
#         isbn = row['ISBN']
#         published_date = row['Published Date']
        
#         # پردازش و اضافه کردن دسته‌بندی‌ها
#         categories = row['Categories'].split(',')
#         category_objects = []
#         for cat_name in categories:
#             category, created = Category.objects.get_or_create(name=cat_name.strip())
#             category_objects.append(category)
        
#         # پردازش و اضافه کردن نویسنده‌ها
#         authors = row['Author'].split(',')
#         author_objects = []
#         for author_name in authors:
#             author, created = Author.objects.get_or_create(name=author_name.strip())
#             author_objects.append(author)
        
#         # ایجاد یا به‌روزرسانی کتاب
#         book, created = Book.objects.get_or_create(title=title, isbn=isbn)
#         book.published_date = published_date
#         book.categories.set(category_objects)  # افزودن دسته‌بندی‌ها
#         book.authors.set(author_objects)       # افزودن نویسنده‌ها
#         book.save()

# views.py
# from django.shortcuts import render, redirect
# from .forms import UploadFileForm
# from .utils import import_books

# def import_books_view(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             import_books(request.FILES['file'])
#             return redirect('success_page')  # صفحه‌ای برای نمایش موفقیت آمیز بودن وارد کردن داده‌ها
#     else:
#         form = UploadFileForm()
#     return render(request, 'import_books.html', {'form': form})


# urls.py
# from django.urls import path
# from .views import import_books_view

# urlpatterns = [
#     path('import-books/', import_books_view, name='import_books'),
# ]


# <!-- import_books.html -->
# <form method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Upload</button>
# </form>



# utils.py
# import json
# import pandas as pd
# from .models import Book, Author, Category

# def import_books(file):
#     # بررسی نوع فایل
#     if file.name.endswith('.xlsx'):
#         data = pd.read_excel(file)
#     elif file.name.endswith('.csv'):
#         data = pd.read_csv(file)
#     elif file.name.endswith('.json'):
#         # خواندن و تبدیل JSON به قالب DataFrame
#         data = pd.DataFrame(json.load(file))
#     else:
#         raise ValueError("Unsupported file format")

#     for index, row in data.iterrows():
#         title = row['Title']
#         isbn = row['ISBN']
#         published_date = row['Published Date']
        
#         # پردازش و اضافه کردن دسته‌بندی‌ها
#         categories = row['Categories'] if isinstance(row['Categories'], list) else row['Categories'].split(',')
#         category_objects = []
#         for cat_name in categories:
#             category, created = Category.objects.get_or_create(name=cat_name.strip())
#             category_objects.append(category)
        
#         # پردازش و اضافه کردن نویسنده‌ها
#         authors = row['Author'] if isinstance(row['Author'], list) else row['Author'].split(',')
#         author_objects = []
#         for author_name in authors:
#             author, created = Author.objects.get_or_create(name=author_name.strip())
#             author_objects.append(author)
        
#         # ایجاد یا به‌روزرسانی کتاب
#         book, created = Book.objects.get_or_create(title=title, isbn=isbn)
#         book.published_date = published_date
#         book.categories.set(category_objects)  # افزودن دسته‌بندی‌ها
#         book.authors.set(author_objects)       # افزودن نویسنده‌ها
#         book.save()


