from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "books"
urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>/", views.about, name="about"),
    path("category/<str:slug>/", views.category, name="category"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)