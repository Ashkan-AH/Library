from django import forms
from .models import Comment, Reply


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widget = {
            "text": forms.TextInput(attrs={"placeholder": "نظر خود را بنویسید..."})
        }
        labels = {
            "body": ""
        }


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["text"]
        widget = {
            "text": forms.TextInput(attrs={"placeholder": "نظر خود را بنویسید...", "class": "!text-sm"})
        }
        labels = {
            "body": ""
        }