# Generated by Django 5.1.1 on 2024-10-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetheme',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='upload/page_theme/thumbnail/', verbose_name='تصویر پیش نمایش'),
        ),
    ]
