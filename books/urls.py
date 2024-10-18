from django.urls import path, include
from . import views

app_name = "books"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("books/<str:slug>/", views.BookList.as_view(), name="books"),
    path("books/", views.BookList.as_view(), name="books"),
    path("book/<str:slug>/", views.BookDetail.as_view(), name="book-detail"),

    path("book/comment/create/<str:slug>/", views.CommentCreate.as_view(), name="comment-create"),

    path("search-result/", views.search_result, name="search-result"),
    path("search/", views.search_item, name="search-item"),

    path("bookmark/add/<int:id>/", views.bookmark_add, name="bookmark-add"),

    path("waiting/add/<int:id>/", views.waiting_add, name="waiting-add"),

    path("reservation/create/<int:book>/", views.reservation_add, name="reservation-add"),

    path("extend-request/<int:id>/", views.extend_request, name="extend-request"),

    path("categories/", views.CategoryList.as_view(), name="categories"),
    path("category/<str:slug>/", views.CategoryBookList.as_view(), name="category"),
]