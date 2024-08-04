from django.db import models
from books.models import Books
from account.models import User
# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments", verbose_name="کاربر", null=True)
    parent_book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments", verbose_name="کتاب")
    text = models.CharField(max_length=150)
    date_created = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)

    def __str__(self) -> str:
        if self.author:
            return f"{self.author.username} : {self.text[:30]}"
        else:
            return f"No Author : {self.text[:30]}"
        
    class Meta:
        ordering = ["-date_created"]
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'



class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="replies", verbose_name="کاربر", null=True)
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies", verbose_name="کامنت اصلی")
    text = models.CharField(max_length=150)
    date_created = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)

    def __str__(self) -> str:
        if self.author:
            return f"{self.author.username} : {self.text[:30]}"
        else:
            return f"No Author : {self.text[:30]}"
        
    class Meta:
        ordering = ["date_created"]
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'