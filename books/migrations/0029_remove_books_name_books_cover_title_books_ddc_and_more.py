# Generated by Django 5.1.1 on 2024-12-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0028_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='name',
        ),
        migrations.AddField(
            model_name='books',
            name='cover_title',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='عنوان جلد'),
        ),
        migrations.AddField(
            model_name='books',
            name='ddc',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='رده بندی دهدهی دیوئی'),
        ),
        migrations.AddField(
            model_name='books',
            name='isbn',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='شابک(ISBN)'),
        ),
        migrations.AddField(
            model_name='books',
            name='llc',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='رده بندی کنگره'),
        ),
        migrations.AddField(
            model_name='books',
            name='location',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='جایگاه'),
        ),
        migrations.AddField(
            model_name='books',
            name='nli',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='کتابخانه ملی ایران'),
        ),
        migrations.AddField(
            model_name='books',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='books',
            name='volume',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='شماره جلد'),
        ),
        migrations.AddField(
            model_name='category',
            name='llc',
            field=models.CharField(blank=True, max_length=10, verbose_name='رده بندی کنگره'),
        ),
        migrations.AlterField(
            model_name='books',
            name='edition',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='سری چاپ'),
        ),
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(default='default-book.jpg', upload_to='uploads/books/', verbose_name='عکس کتاب'),
        ),
        migrations.AlterField(
            model_name='books',
            name='pub_year',
            field=models.IntegerField(blank=True, default=0, verbose_name='سال چاپ'),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='default-category.jpg', upload_to='uploads/categories/', verbose_name='عکس دسته بندی'),
        ),
    ]
