from django.db.models.signals import pre_save, post_delete
from django.http import Http404
from django.dispatch import receiver
from books.models import Books, Category
from reservation.models import Reservation
from author.models import Author
from django.utils.text import slugify

@receiver(pre_save, sender=Books)
def create_book(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

@receiver(pre_save, sender=Author)
def create_author(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

@receiver(pre_save, sender=Category)
def create_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

@receiver(post_delete, sender=Reservation)
def create_category(sender, instance, *args, **kwargs):
    book = Books.objects.get(id=instance.book_id.id)
    book.in_stock += 1
    book.save()


@receiver(pre_save, sender=Reservation)
def book_reduce(sender, instance, *args, **kwargs):
    book = Books.objects.get(id=instance.book_id.id)
    if book.in_stock > 0:
        book.in_stock -= 1
        book.save()
    else:
        raise Http404("این کتاب موجود نیست.")


def create_unique_slug(instance, newslug=None):
    if newslug is not None:
        slug=newslug
    else:
        slug = slugify(instance.name, allow_unicode=True)
    
    instanceClass = instance.__class__
    qs = instanceClass.objects.filter(slug=slug)

    if qs.exists():
        newslug = f"{slug}-{qs.first().id}"
        return create_unique_slug(instance, newslug)
    return slug