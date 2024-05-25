# Generated by Django 5.0.3 on 2024-05-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_author_description_alter_author_picture'),
        ('books', '0012_alter_books_age_category_remove_books_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='books', to='author.author', verbose_name='نویسندگان'),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ManyToManyField(related_name='books', to='books.category', verbose_name='دسته\u200cبندی\u200cها'),
        ),
    ]
