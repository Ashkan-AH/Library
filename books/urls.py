from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "books"
urlpatterns = [
    path("", views.BookList.as_view(), name="home"),
    path("<str:slug>/", views.BookDetail.as_view(), name="about"),
    path("bookmark/<int:id>/", views.bookmark_add, name="bookmark-add"),
    path("category/<str:slug>/", views.CategoryList.as_view(), name="category"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)