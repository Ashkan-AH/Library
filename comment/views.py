from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect 
from .forms import CommentCreateForm, ReplyCreateForm
from .models import Comment, Reply
from books.models import Books

# Create your views here.

class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentCreateForm
    def form_valid(self, form):
        slug = self.kwargs.get("slug")
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.parent_book = Books.objects.get(slug=slug)
        comment.save()
        return redirect("books:books", slug)


class ReplyCreate(LoginRequiredMixin, CreateView):
    form_class = ReplyCreateForm
    def form_valid(self, form):
        comment_id = self.kwargs.get("id")
        reply = form.save(commit=False)
        reply.author = self.request.user
        reply.parent_comment = Comment.objects.get(id=comment_id)
        reply.save()
        return redirect("books:books", reply.parent_comment.parent_book.slug)
    

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "main/comments/comment_comfirm_delete.html"
    

class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = "main/comments/reply_comfirm_delete.html"