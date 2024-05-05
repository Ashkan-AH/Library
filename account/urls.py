from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "account"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)