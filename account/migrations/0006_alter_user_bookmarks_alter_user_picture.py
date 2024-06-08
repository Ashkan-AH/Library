# Generated by Django 5.0.3 on 2024-06-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_picture_alter_user_address_and_more'),
        ('books', '0017_alter_books_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, to='books.books', verbose_name='ذخیره شده ها'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(upload_to='uploads/profile/', verbose_name='تصویر'),
        ),
    ]
