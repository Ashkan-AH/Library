from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("books/<str:slug>/", views.BookList.as_view(), name="books"),
    path("books/", views.BookList.as_view(), name="books"),
    # path("author-books/<str:slug>/", views.AuthorBookList.as_view(), name="author-books"),
    path("search-result/", views.search_result, name="search-result"),
    path("search/", views.search_item, name="search-item"),

    path("book/<str:slug>/", views.BookDetail.as_view(), name="book-detail"),
    path("bookmark/add/<int:id>/", views.bookmark_add, name="bookmark-add"),
    path("waiting/add/<int:id>/", views.waiting_add, name="waiting-add"),
    path("reservation/create/<int:book_id>/", views.reservation_add, name="reservation-add"),
    path("categories/", views.CategoryList.as_view(), name="categories"),
    path("category/<str:slug>/", views.CategoryBookList.as_view(), name="category"),
]