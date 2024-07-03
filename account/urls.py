from django.urls import path
from django.contrib.auth import views
from . import views

app_name = "account"

urlpatterns = [
    path("books/create/", views.BookCreate.as_view() , name="book-create"),
    path("books/update/<str:slug>/", views.BookUpdate.as_view() , name="book-update"),
    path("books/delete/<str:slug>/", views.BookDelete.as_view() , name="book-delete"),
    path("books/<str:slug>/", views.BookDetail.as_view() , name="book-detail"),
    path("books/", views.BookList.as_view() , name="books"),


    path("categories/create/", views.CategoryCreate.as_view() , name="category-create"),
    path("categories/update/<str:slug>/", views.CategoryUpdate.as_view() , name="category-update"),
    path("categories/delete/<str:slug>/", views.CategoryDelete.as_view() , name="category-delete"),
    path("categories/", views.CategoryList.as_view() , name="categories"),


    path("authors/create/", views.AuthorCreate.as_view() , name="author-create"),
    path("authors/update/<str:slug>/", views.AuthorUpdate.as_view() , name="author-update"),
    path("authors/delete/<str:slug>/", views.AuthorDelete.as_view() , name="author-delete"),
    path("authors/<str:slug>/", views.AuthorDetail.as_view() , name="author-detail"),
    path("authors/", views.AuthorList.as_view() , name="authors"),


    path("reservations/create/", views.ReservationCreate.as_view() , name="reservation-create"),
    path("reservations/update/<int:pk>/", views.ReservationUpdate.as_view() , name="reservation-update"),
    path("reservations/delete/<int:pk>/", views.ReservationDelete.as_view() , name="reservation-delete"),
    path("reservations/<int:pk>/", views.ReservationDetail.as_view() , name="reservation-detail"),
    path("reservations/", views.ReservationList.as_view() , name="reservations"),


    path("users/create/", views.UserCreate.as_view() , name="user-create"),
    path("users/update/<int:pk>/", views.UserUpdate.as_view() , name="user-update"),
    path("users/delete/<int:pk>/", views.UserDelete.as_view() , name="user-delete"),
    path("users/<int:pk>/", views.UserDetail.as_view() , name="user-detail"),
    path("users/", views.UserList.as_view() , name="users"),


    path("bookmarks/", views.BookmarkList.as_view() , name="bookmarks"),
    path("profile-update/", views.ProfileUpdate.as_view() , name="profile-update"),
    path("", views.Profile.as_view() , name="profile"), 
]