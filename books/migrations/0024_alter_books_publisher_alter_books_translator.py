# Generated by Django 5.1.1 on 2024-09-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='ناشر'),
        ),
        migrations.AlterField(
            model_name='books',
            name='translator',
            field=models.CharField(blank=True, default='-', max_length=150, verbose_name='مترجم'),
        ),
    ]