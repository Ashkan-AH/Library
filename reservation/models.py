from django.db import models
from books.models import Books
from account.models import User
# Create your models here.

class Reservation(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="reserves")
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="reserves")
    