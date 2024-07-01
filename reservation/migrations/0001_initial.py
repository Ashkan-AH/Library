# Generated by Django 5.0.3 on 2024-07-01 14:03

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0019_books_bookmarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد رزرو')),
                ('status', models.CharField(choices=[('رزرو شده', 'رزرو شده'), ('تحویل داده شده', 'تحویل داده شده'), ('در انتظار بازگشت', 'در انتظار بازگشت'), ('بازگردانده نشده', 'بازگردانده نشده'), ('بازگردانده شده', 'بازگردانده شده')], default='رزرو شده', max_length=25, verbose_name='وضعیت رزرو')),
                ('delivery_date', models.DateField(blank=True, default=datetime.datetime(2024, 7, 1, 14, 3, 22, 347991, tzinfo=datetime.timezone.utc), verbose_name='تاریخ تحویل')),
                ('extend_sluts', models.IntegerField(default=2, verbose_name='تعداد درخواست مهلت اضافه باقی مانده')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservations', to='books.books', verbose_name='کد کتاب')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservations', to=settings.AUTH_USER_MODEL, verbose_name='کد کاربری')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'رزرو\u200cها',
            },
        ),
    ]