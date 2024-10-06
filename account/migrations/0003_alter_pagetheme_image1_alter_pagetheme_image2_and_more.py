# Generated by Django 5.1.1 on 2024-10-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_pagetheme_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetheme',
            name='image1',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/', verbose_name='تصویر شماره ۱'),
        ),
        migrations.AlterField(
            model_name='pagetheme',
            name='image2',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/', verbose_name='تصویر شماره ۲'),
        ),
        migrations.AlterField(
            model_name='pagetheme',
            name='image3',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/', verbose_name='تصویر شماره ۳'),
        ),
        migrations.AlterField(
            model_name='pagetheme',
            name='image4',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/', verbose_name='تصویر شماره ۴'),
        ),
        migrations.AlterField(
            model_name='pagetheme',
            name='image5',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/', verbose_name='تصویر شماره ۵'),
        ),
        migrations.AlterField(
            model_name='pagetheme',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default-thumbnail.jpg', upload_to='upload/page_theme/thumbnail/', verbose_name='تصویر پیش نمایش'),
        ),
    ]
