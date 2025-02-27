# Generated by Django 5.1.1 on 2024-12-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0029_remove_books_name_books_cover_title_books_ddc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='title',
        ),
        migrations.AddField(
            model_name='books',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='عنوان'),
        ),
    ]
