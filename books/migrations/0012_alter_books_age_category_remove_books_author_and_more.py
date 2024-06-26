# Generated by Django 5.0.3 on 2024-04-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_author_description_alter_author_picture'),
        ('books', '0011_alter_books_age_category_alter_books_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='age_category',
            field=models.CharField(blank=True, choices=[('کودک', 'کودک'), ('نوجوان', 'نوجوان'), ('بزرگسال', 'بزرگسال')], default='کودک', max_length=15, verbose_name='گروه سنی'),
        ),
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.AlterField(
            model_name='books',
            name='language',
            field=models.CharField(blank=True, choices=[('خارجی', [('انگلیسی', 'انگلیسی'), ('فرانسوی', 'فرانسوی'), ('آلمانی', 'آلمانی'), ('عربی', 'عربی')]), ('داخلی', [('فارسی', 'فارسی'), ('کردی', 'کردی'), ('ترکی', 'ترکی')])], default='فارسی', max_length=25, verbose_name='زبان'),
        ),
        migrations.AlterField(
            model_name='books',
            name='picture',
            field=models.ImageField(upload_to='uploads/books/', verbose_name='عکس کتاب'),
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='books', to='author.author'),
        ),
    ]
