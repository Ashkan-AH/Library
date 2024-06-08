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
    path("books/create/", v.BookCreate.as_view() , name="book-create"),
    path("books/update/<str:slug>/", v.BookUpdate.as_view() , name="book-update"),
    path("books/delete/<str:slug>/", v.BookDelete.as_view() , name="book-delete"),
    path("books/preview/<str:slug>/", v.BookPreview.as_view() , name="book-preview"),
    path("books/<str:slug>/", v.BookDetail.as_view() , name="book-detail"),
    path("books/", v.BookList.as_view() , name="books"),


    path("categories/create/", v.CategoryCreate.as_view() , name="category-create"),
    path("categories/update/<str:slug>/", v.CategoryUpdate.as_view() , name="category-update"),
    path("categories/delete/<str:slug>/", v.CategoryDelete.as_view() , name="category-delete"),
    path("categories/", v.CategoryList.as_view() , name="categories"),


    path("authors/create/", v.AuthorCreate.as_view() , name="author-create"),
    path("authors/update/<str:slug>/", v.AuthorUpdate.as_view() , name="author-update"),
    path("authors/delete/<str:slug>/", v.AuthorDelete.as_view() , name="author-delete"),
    path("authors/<str:slug>/", v.AuthorDetail.as_view() , name="author-detail"),
    path("authors/", v.AuthorList.as_view() , name="authors"),


    path("users/create/", v.UserCreate.as_view() , name="user-create"),
    path("users/update/<int:pk>/", v.UserUpdate.as_view() , name="user-update"),
    path("users/delete/<int:pk>/", v.UserDelete.as_view() , name="user-delete"),
    path("users/<int:pk>/", v.UserDetail.as_view() , name="user-detail"),
    path("users/", v.UserList.as_view() , name="users"),


    path("profile-update/", v.ProfileUpdate.as_view() , name="profile-update"),
    path("", v.Profile.as_view() , name="profile"), 
]