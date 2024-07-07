from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.BookList.as_view(), name="books"),
    path("<str:slug>/", views.BookDetail.as_view(), name="book-detail"),
    path("bookmark/<int:id>/", views.bookmark_add, name="bookmark-add"),
    path("reservation/create/<int:book_id>/", views.reservation_add, name="reservation-add"),
    path("category/<str:slug>/", views.CategoryList.as_view(), name="category"),
]