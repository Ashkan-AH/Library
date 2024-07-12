# Generated by Django 5.0.3 on 2024-07-09 22:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_remove_books_keep_duration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='waiting_users',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='لیست انتظار'),
        ),
    ]
