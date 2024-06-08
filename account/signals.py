from django.db.models.signals import pre_save
from django.dispatch import receiver
from books.models import Books, Category
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