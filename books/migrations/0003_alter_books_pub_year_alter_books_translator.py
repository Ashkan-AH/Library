# Generated by Django 5.0.3 on 2024-03-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_options_remove_books_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pub_year',
            field=models.IntegerField(blank=True, verbose_name='سال انتشار'),
        ),
        migrations.AlterField(
            model_name='books',
            name='translator',
            field=models.CharField(max_length=150, verbose_name='مترجم'),
        ),
    ]
