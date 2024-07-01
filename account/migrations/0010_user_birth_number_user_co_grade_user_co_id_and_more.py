# Generated by Django 5.0.3 on 2024-06-28 13:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='شماره شناسنامه'),
        ),
        migrations.AddField(
            model_name='user',
            name='co_grade',
            field=models.CharField(blank=True, max_length=15, verbose_name='سمت شغلی'),
        ),
        migrations.AddField(
            model_name='user',
            name='co_id',
            field=models.CharField(blank=True, max_length=15, verbose_name='کد کارمندی'),
        ),
        migrations.AddField(
            model_name='user',
            name='co_unit',
            field=models.CharField(blank=True, choices=[('آموزشکده فنی بندر انزلی - شهید خدادادی', 'آموزشکده فنی بندر انزلی - شهید خدادادی'), ('آموزشکده فنی رستم آباد رودبار - سیدالشهداء', 'آموزشکده فنی رستم آباد رودبار - سیدالشهداء'), ('آموزشکده فنی رشت - شهید چمران', 'آموزشکده فنی رشت - شهید چمران'), ('آموزشکده فنی پسران آستانه اشرفیه', 'آموزشکده فنی پسران آستانه اشرفیه'), ('آموزشکده فنی پسران لاهیجان - شهیدرجائی', 'آموزشکده فنی پسران لاهیجان - شهیدرجائی'), ('دانشکده فنی و حرفه\u200cای صومعه سرا', 'دانشکده فنی و حرفه\u200cای صومعه سرا'), ('آموزشکده فنی دختران رشت', 'آموزشکده فنی دختران رشت'), ('دانشگاه فنی و حرفه\u200cای استان گیلان', 'دانشگاه فنی و حرفه\u200cای استان گیلان')], max_length=50, verbose_name='محل کار'),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='شماره اضطراری'),
        ),
        migrations.AddField(
            model_name='user',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='نام پدر'),
        ),
        migrations.AddField(
            model_name='user',
            name='pro_grade',
            field=models.CharField(blank=True, choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی')], max_length=15, verbose_name='مقطع درسی'),
        ),
        migrations.AddField(
            model_name='user',
            name='pro_id',
            field=models.CharField(blank=True, max_length=15, verbose_name='کد استادی'),
        ),
        migrations.AddField(
            model_name='user',
            name='pro_major',
            field=models.CharField(blank=True, choices=[('حسابداری', 'حسابداری'), ('کامپیوتر', 'کامپیوتر'), ('صنایع چوب', 'صنایع چوب'), ('عمران', 'عمران'), ('معماری', 'معماری'), ('برق', 'برق')], max_length=15, verbose_name='رشته درسی'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('دانشجو', 'دانشجو'), ('استاد', 'استاد'), ('کامند', 'کامند')], max_length=7),
        ),
        migrations.AddField(
            model_name='user',
            name='st_grade',
            field=models.CharField(blank=True, choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی')], max_length=15, verbose_name='مقطع تحصیلی'),
        ),
        migrations.AddField(
            model_name='user',
            name='st_id',
            field=models.CharField(blank=True, max_length=15, verbose_name='کد دانشجویی'),
        ),
        migrations.AddField(
            model_name='user',
            name='st_major',
            field=models.CharField(blank=True, choices=[('حسابداری', 'حسابداری'), ('کامپیوتر', 'کامپیوتر'), ('صنایع چوب', 'صنایع چوب'), ('عمران', 'عمران'), ('معماری', 'معماری'), ('برق', 'برق')], max_length=15, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, verbose_name='آدرس منزل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, upload_to='uploads/profile/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sel_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='تلفن همراه'),
        ),
    ]