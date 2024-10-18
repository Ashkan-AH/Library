# Generated by Django 5.1.1 on 2024-10-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_pagetheme_image1_alter_pagetheme_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_comments',
            field=models.BooleanField(default=False, verbose_name='ایجاد نظرات'),
        ),
        migrations.AddField(
            model_name='user',
            name='delete_comments',
            field=models.BooleanField(default=False, verbose_name='حذف نظرات'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_comments',
            field=models.BooleanField(default=False, verbose_name='ویرایش نظرات'),
        ),
        migrations.AddField(
            model_name='user',
            name='view_comments',
            field=models.BooleanField(default=False, verbose_name='مشاهده نظرات'),
        ),
    ]
