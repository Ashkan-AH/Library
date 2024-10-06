# Generated by Django 5.1.1 on 2024-10-05 16:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_remove_books_test'),
        ('reservation', '0008_alter_reservation_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservations', to='books.books', verbose_name='کتاب'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservations', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
