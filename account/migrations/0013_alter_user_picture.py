# Generated by Django 5.0.3 on 2024-07-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='uploads/profile/', verbose_name='تصویر'),
        ),
    ]