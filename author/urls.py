from django.urls import path
from . import views

app_name = "author"
urlpatterns = [
    path("", views.AuthorList.as_view(), name="authors"),
    path("<str:slug>/", views.AuthorDetail.as_view(), name="author-detail"),
]