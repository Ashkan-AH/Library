# Generated by Django 5.0.3 on 2024-07-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_remove_user_co_grade_remove_user_co_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, verbose_name='آدرس منزل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('دانشجو', 'دانشجو'), ('استاد', 'استاد'), ('کامند', 'کامند')], max_length=7, verbose_name='نقش'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sel_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='تلفن همراه'),
        ),
    ]
