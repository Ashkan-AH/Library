from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.BookList.as_view(), name="home"),
    path("<str:slug>/", views.BookDetail.as_view(), name="about"),
    path("bookmark/<int:id>/", views.bookmark_add, name="bookmark-add"),
    path("category/<str:slug>/", views.CategoryList.as_view(), name="category"),
]