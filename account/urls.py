from django.urls import path, re_path
from django.contrib.auth import views
from . import views
from django.views.generic import TemplateView

app_name = "account"

urlpatterns = [
    path("books/create/", views.BookCreate.as_view(), name="book-create"),
    path("books/update/<str:slug>/", views.BookUpdate.as_view(), name="book-update"),
    path("books/delete/<str:slug>/", views.BookDelete.as_view(), name="book-delete"),
    path("books/<str:slug>/", views.BookDetail.as_view(), name="book-detail"),
    path("books/", views.BookList.as_view(), name="books"),


    path("categories/create/", views.CategoryCreate.as_view(), name="category-create"),
    path("categories/update/<str:slug>/", views.CategoryUpdate.as_view(), name="category-update"),
    path("categories/delete/<str:slug>/", views.CategoryDelete.as_view(), name="category-delete"),
    path("categories/", views.CategoryList.as_view(), name="categories"),


    path("authors/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("authors/update/<str:slug>/", views.AuthorUpdate.as_view(), name="author-update"),
    path("authors/delete/<str:slug>/", views.AuthorDelete.as_view(), name="author-delete"),
    path("authors/<str:slug>/", views.AuthorDetail.as_view(), name="author-detail"),
    path("authors/", views.AuthorList.as_view(), name="authors"),


    path("reservations/create/", views.ReservationCreate.as_view(), name="reservation-create"),
    path("reservations/delete/<int:pk>/", views.ReservationDelete.as_view(), name="reservation-delete"),
    path("reservations/<int:pk>/", views.ReservationDetail.as_view(), name="reservation-detail"),
    path("reservations/", views.ReservationList.as_view(), name="reservations"),
    path("delivered/<int:pk>/", views.delivered_action, name="delivered-action"),
    path("cancel/<int:pk>/", views.cancel_action, name="cancel-action"),
    path("reserve/<int:pk>/", views.reserve_action, name="reserve-action"),
    path("returned/<int:pk>/", views.returned_action, name="returned-action"),


    path("users/update/<int:pk>/", views.UserUpdate.as_view(), name="user-update"),
    path("users/delete/<int:pk>/", views.UserDelete.as_view(), name="user-delete"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("users/", views.UserList.as_view(), name="users"),
    

    path("black-list/", views.BlackList.as_view(), name="black-list"),
    path("bookmarks/", views.BookmarkList.as_view(), name="bookmarks"),
    path("waiting-list/", views.WaitingList.as_view(), name="waiting-list"),
    path("profile-update/", views.ProfileUpdate.as_view(), name="profile-update"),

    
    path('signup/', views.Registration.as_view(), name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('policy/', TemplateView.as_view(template_name="registration/policy.html"), name="policy"),


    path("", views.Profile.as_view(), name="profile"), 
]