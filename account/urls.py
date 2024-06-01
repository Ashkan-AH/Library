from django.urls import path
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

app_name = "account"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path("books/", v.BookList.as_view() , name="books"),
    path("books/<str:slug>/", v.BookDetail.as_view() , name="book-detail"),
    path("create/", v.BookCreate.as_view() , name="create-book"),
    path("update/<str:slug>/", v.BookUpdate.as_view() , name="update-book"),
    path("delete/<str:slug>/", v.BookDelete.as_view() , name="delete-book"),
    path("preview/<str:slug>/", v.BookPreview.as_view() , name="preview-book"),
    path("", v.home , name="home"), 
]