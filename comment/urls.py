from django.urls import path
from . import views

app_name = "author"
urlpatterns = [
    path("comment-create/<str:slug>/", views.CommentCreate.as_view(), name="comment-create"),
    path("comment-delete/<int:pk>/", views.CommentDelete.as_view(), name="comment-delete"),
    path("reply-create/<int:pk>/", views.ReplyCreate.as_view(), name="reply-create"),
    path("reply-delete/<int:pk>/", views.ReplyDelete.as_view(), name="reply-delete"),
]