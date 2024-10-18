from django.urls import path
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
    path("categories/<str:slug>/", views.CategoryDetail.as_view(), name="category-detail"),
    path("categories/books/<str:slug>/", views.CategoryBooksList.as_view(), name="category-books"),
    path("categories/", views.CategoryList.as_view(), name="categories"),


    path("authors/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("authors/update/<str:slug>/", views.AuthorUpdate.as_view(), name="author-update"),
    path("authors/delete/<str:slug>/", views.AuthorDelete.as_view(), name="author-delete"),
    path("authors/<str:slug>/", views.AuthorDetail.as_view(), name="author-detail"),
    path("authors/books/<str:slug>/", views.AuthorBooksList.as_view(), name="author-books"),
    path("authors/", views.AuthorList.as_view(), name="authors"),


    path("reservations/create/", views.ReservationCreate.as_view(), name="reservation-create"),
    path("reservations/delete/<int:pk>/", views.ReservationDelete.as_view(), name="reservation-delete"),
    path("reservations/<int:pk>/", views.ReservationDetail.as_view(), name="reservation-detail"),
    path("reservations/", views.ReservationList.as_view(), name="reservations"),
    path("extends/", views.ExtendList.as_view(), name="extends"),
    path("delivered/<int:pk>/", views.delivered_action, name="delivered-action"),
    path("cancel/<int:pk>/", views.cancel_action, name="cancel-action"),
    path("returned/<int:pk>/", views.returned_action, name="returned-action"),
    path("extend/<int:pk>/", views.extend_action, name="extend-action"),


    path("comments/create/", views.CommentCreate.as_view(), name="comment-create"),
    path("comments/delete/<int:pk>/", views.CommentDelete.as_view(), name="comment-delete"),
    path("comments/update/<int:pk>/", views.CommentUpdate.as_view(), name="comment-update"),
    path("comments/<int:id>/", views.CommentDetail.as_view(), name="comment-detail"),
    path("comments/", views.CommentList.as_view(), name="comments"),
    path("confirm/<int:id>/", views.confirm_action, name="confirm-action"),
    path("reject/<int:id>/", views.reject_action, name="reject-action"),


    path("users/create/", views.UserCreate.as_view(), name="user-create"),
    path("users/update/<int:pk>/", views.UserUpdate.as_view(), name="user-update"),
    path("users/delete/<int:pk>/", views.UserDelete.as_view(), name="user-delete"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("users/", views.UserList.as_view(), name="users"),
    

    path("black-list/", views.BlackList.as_view(), name="black-list"),
    path("user-bookmarks/", views.UserBookmarkList.as_view(), name="user-bookmarks"),
    path("admin-bookmarks/", views.AdminBookmarkList.as_view(), name="admin-bookmarks"),
    path("waiting-list/", views.WaitingList.as_view(), name="waiting-list"),
    path("user-profile-update/", views.UserProfileUpdate.as_view(), name="user-profile-update"),
    path("admin-profile-update/", views.AdminProfileUpdate.as_view(), name="admin-profile-update"),
    path("themes/", views.ThemeList.as_view(), name="themes"),
    path("themes/<str:slug>/", views.ThemeUpdate.as_view(), name="theme-update"),
    path('security/', TemplateView.as_view(template_name="account/user/security.html"), name="security"),
    path("search/", views.search_item, name="search-item"),
    path("search-result/", views.search_result, name="search-result"),

    
    path('signup/', views.Registration.as_view(), name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('policy/', TemplateView.as_view(template_name="registration/policy.html"), name="policy"),


    path("create/", views.CreationView.as_view(), name="create"), 
    path("admin-index/", views.AdminIndex.as_view(), name="admin-index"), 
    path("user-index/", views.UserProfile.as_view(), name="user-index"), 
    path("", views.identifier, name="identifier"), 
]