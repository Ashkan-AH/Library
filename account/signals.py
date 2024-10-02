from django.db.models.signals import pre_save, post_delete , post_save
from django.http import Http404
from django.dispatch import receiver
from books.models import Books, Category
from .models import User
from reservation.models import Reservation
from author.models import Author
from django.utils.text import slugify

@receiver(pre_save, sender=User)
def role(sender, instance, *args, **kwargs):
    if instance.role == "دانشجو":
        instance.pro_id = ""
        instance.emp_id = ""
        instance.pro_grade = ""
        instance.emp_grade = ""
        instance.pro_major = ""
        instance.emp_unit = ""
    elif instance.role == "استاد":
        instance.st_id = ""
        instance.emp_id = ""
        instance.st_grade = ""
        instance.emp_grade = ""
        instance.st_major = ""
        instance.emp_unit = ""
    elif instance.role == "کارمند":
        instance.pro_id = ""
        instance.st_id = ""
        instance.pro_grade = ""
        instance.st_grade = ""
        instance.pro_major = ""
        instance.st_major = ""


@receiver(pre_save, sender=Books)
def create_book(sender, instance, *args, **kwargs):
    if instance.id is None:
        if not instance.slug:
            instance.slug = create_unique_slug(instance)
    else:
        Books.in_stock_email(instance)
        

@receiver(pre_save, sender=Author)
def create_author(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

@receiver(pre_save, sender=Category)
def create_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


@receiver(post_delete, sender=Reservation)
def book_delete_increase(sender, instance, *args, **kwargs):
    book = Books.objects.get(id=instance.book_id.id)
    user = User.objects.get(id=instance.user_id.id)
    
    if instance.status == "رزرو شده":
        book.in_stock_user += 1
        book.save()
        user.reservation_limit += 1
        user.save()
    elif instance.status == "تحویل داده شده" or instance.status == "بازگردانده نشده":
        book.in_stock_user += 1
        book.in_stock += 1
        book.save()
        user.reservation_limit += 1
        user.save()
    
    


@receiver(pre_save, sender=Reservation)
def book_create_reservation_reduce(sender, instance, *args, **kwargs):
    user = User.objects.get(id=instance.user_id.id)
    book = Books.objects.get(id=instance.book_id.id)
    if instance.reservation_id is None:
        if user.reservation_limit > 0:
            if instance.status == "رزرو شده":
                if book.in_stock_user > 0:
                    user.reservation_limit -= 1
                    user.save()
                    book.in_stock_user -= 1
                    book.save()
                else:
                    raise Http404("ظرفیت رزرو این کتاب کاملا پر است.")
            elif instance.status == "لغو رزرو":
                user.reservation_limit += 1
                user.save()
                book.in_stock_user += 1
                book.save()
            elif instance.status == "تحویل داده شده" or instance.status == "بازگردانده نشده":
                if book.in_stock_user > 0 and book.in_stock > 0:
                    user.reservation_limit -= 1
                    user.is_active = False
                    user.save()
                    book.in_stock_user -= 1
                    book.in_stock -= 1
                    book.save()
                else:
                    raise Http404("این کتاب در انبار موجود نیست یا ظرفیت رزرو تکمیل است.")
            elif instance.status == "بازگردانده شده":
                user.reservation_limit += 1
                user.save()
                book.in_stock_user += 1
                book.in_stock += 1
                book.save()
        else:
            raise Http404("این کاربر به حد تعداد رزرو خود رسیده است.")

            
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