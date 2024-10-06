# Generated by Django 5.1.1 on 2024-10-05 17:08

import account.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام صفحه')),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, verbose_name='آدرس صفحه ویرایش')),
                ('date_edited', models.DateField(auto_now=True, verbose_name='آخرین ویرایش')),
                ('text1', models.TextField(blank=True, verbose_name='متن شماره ۱')),
                ('text2', models.TextField(blank=True, verbose_name='متن شماره ۲')),
                ('text3', models.TextField(blank=True, verbose_name='متن شماره ۳')),
                ('text4', models.TextField(blank=True, verbose_name='متن شماره ۴')),
                ('text5', models.TextField(blank=True, verbose_name='متن شماره ۵')),
                ('text6', models.TextField(blank=True, verbose_name='متن شماره ۶')),
                ('text7', models.TextField(blank=True, verbose_name='متن شماره ۷')),
                ('text8', models.TextField(blank=True, verbose_name='متن شماره ۸')),
                ('text9', models.TextField(blank=True, verbose_name='متن شماره ۹')),
                ('text10', models.TextField(blank=True, verbose_name='متن شماره ۱۰')),
                ('text11', models.TextField(blank=True, verbose_name='متن شماره ۱۱')),
                ('text12', models.TextField(blank=True, verbose_name='متن شماره ۱۲')),
                ('text13', models.TextField(blank=True, verbose_name='متن شماره ۱۳')),
                ('text14', models.TextField(blank=True, verbose_name='متن شماره ۱۴')),
                ('text15', models.TextField(blank=True, verbose_name='متن شماره ۱۵')),
                ('text16', models.TextField(blank=True, verbose_name='متن شماره ۱۶')),
                ('text17', models.TextField(blank=True, verbose_name='متن شماره ۱۷')),
                ('image1', models.ImageField(blank=True, upload_to='upload/page_theme/', verbose_name='تصویر شماره ۱')),
                ('image2', models.ImageField(blank=True, upload_to='upload/page_theme/', verbose_name='تصویر شماره ۲')),
                ('image3', models.ImageField(blank=True, upload_to='upload/page_theme/', verbose_name='تصویر شماره ۳')),
                ('image4', models.ImageField(blank=True, upload_to='upload/page_theme/', verbose_name='تصویر شماره ۴')),
                ('image5', models.ImageField(blank=True, upload_to='upload/page_theme/', verbose_name='تصویر شماره ۵')),
            ],
            options={
                'verbose_name': 'ظاهر صفحه',
                'verbose_name_plural': 'ظاهر صفحات',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('address', models.TextField(blank=True, verbose_name='آدرس منزل')),
                ('birth_number', models.CharField(blank=True, max_length=20, verbose_name='شماره شناسنامه')),
                ('national_code', models.CharField(blank=True, max_length=10, verbose_name='کدملی')),
                ('fathers_name', models.CharField(blank=True, max_length=50, verbose_name='نام پدر')),
                ('sel_number', models.CharField(blank=True, max_length=15, verbose_name='تلفن همراه')),
                ('home_number', models.CharField(blank=True, max_length=11, verbose_name='تلفن ثابت')),
                ('emergency_number', models.CharField(blank=True, max_length=15, verbose_name='شماره اضطراری')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('picture', models.ImageField(default='default.jpg', upload_to='uploads/profile/', verbose_name='تصویر')),
                ('reservation_limit', models.IntegerField(default=5, verbose_name='محدودیت رزرو')),
                ('role', models.CharField(blank=True, choices=[('دانشجو', 'دانشجو'), ('استاد', 'استاد'), ('کارمند', 'کارمند')], max_length=7, verbose_name='نقش')),
                ('st_id', models.CharField(blank=True, max_length=15, verbose_name='کد دانشجویی')),
                ('st_major', models.CharField(blank=True, choices=[('حسابداری', 'حسابداری'), ('کامپیوتر', 'کامپیوتر'), ('صنایع چوب', 'صنایع چوب'), ('عمران', 'عمران'), ('معماری', 'معماری'), ('برق', 'برق')], max_length=15, verbose_name='رشته تحصیلی')),
                ('st_grade', models.CharField(blank=True, choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی')], max_length=15, verbose_name='مقطع تحصیلی')),
                ('emp_id', models.CharField(blank=True, max_length=15, verbose_name='کد پرسنلی')),
                ('emp_unit', models.CharField(blank=True, choices=[('آموزشکده فنی بندر انزلی - شهید خدادادی', 'آموزشکده فنی بندر انزلی - شهید خدادادی'), ('آموزشکده فنی رستم آباد رودبار - سیدالشهداء', 'آموزشکده فنی رستم آباد رودبار - سیدالشهداء'), ('آموزشکده فنی رشت - شهید چمران', 'آموزشکده فنی رشت - شهید چمران'), ('آموزشکده فنی پسران آسانه اشرفیه', 'آموزشکده فنی پسران آسانه اشرفیه'), ('آموزشکده فنی پسران لاهیجان-شهیدرجائی', 'آموزشکده فنی پسران لاهیجان-شهیدرجائی'), ('دانشکده فنی و حرفه ای صومعه سرا', 'دانشکده فنی و حرفه ای صومعه سرا'), ('آموزشکده فنی دختران رشت', 'آموزشکده فنی دختران رشت'), ('دانشگاه فنی و حرفه ای استان گیلان', 'دانشگاه فنی و حرفه ای استان گیلان')], max_length=50, verbose_name='محل کار')),
                ('emp_grade', models.CharField(blank=True, max_length=255, verbose_name='سمت شغلی')),
                ('pro_id', models.CharField(blank=True, max_length=15, verbose_name='کد استادی')),
                ('pro_major', models.CharField(blank=True, choices=[('حسابداری', 'حسابداری'), ('کامپیوتر', 'کامپیوتر'), ('صنایع چوب', 'صنایع چوب'), ('عمران', 'عمران'), ('معماری', 'معماری'), ('برق', 'برق')], max_length=15, verbose_name='رشته آموزشی')),
                ('pro_grade', models.CharField(blank=True, choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی'), ('کاردانی و کارشناسی', 'کاردانی و کارشناسی')], max_length=18, verbose_name='مقطع آموزشی')),
                ('view_books', models.BooleanField(default=False, verbose_name='مشاهده کتاب ها')),
                ('view_authors', models.BooleanField(default=False, verbose_name='مشاهده نویسندگان')),
                ('view_reservations', models.BooleanField(default=False, verbose_name='مشاهده رزرو ها')),
                ('view_users', models.BooleanField(default=False, verbose_name='مشاهده کاربران')),
                ('view_categories', models.BooleanField(default=False, verbose_name='مشاهده دسته بندی ها')),
                ('update_books', models.BooleanField(default=False, verbose_name='ویرایش کتاب ها')),
                ('update_authors', models.BooleanField(default=False, verbose_name='ویرایش نویسندگان')),
                ('update_reservations', models.BooleanField(default=False, verbose_name='ویرایش رزرو ها')),
                ('update_users', models.BooleanField(default=False, verbose_name='ویرایش کاربران')),
                ('update_categories', models.BooleanField(default=False, verbose_name='ویرایش دسته بندی')),
                ('update_theme', models.BooleanField(default=False, verbose_name='ویرایش ظاهر سایت')),
                ('create_books', models.BooleanField(default=False, verbose_name='ایجاد کتاب ها')),
                ('create_authors', models.BooleanField(default=False, verbose_name='ایجاد نویسندگان')),
                ('create_reservations', models.BooleanField(default=False, verbose_name='ایجاد رزرو ها')),
                ('create_users', models.BooleanField(default=False, verbose_name='ایجاد کاربران')),
                ('create_categories', models.BooleanField(default=False, verbose_name='ایجاد دسته بندی ها')),
                ('delete_books', models.BooleanField(default=False, verbose_name='حذف کتاب ها')),
                ('delete_authors', models.BooleanField(default=False, verbose_name='حذف نویسندگان')),
                ('delete_reservations', models.BooleanField(default=False, verbose_name='حذف رزرو ها')),
                ('delete_users', models.BooleanField(default=False, verbose_name='حذف کاربران')),
                ('delete_categories', models.BooleanField(default=False, verbose_name='حذف دسته بندی ها')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', account.models.UserManager2()),
            ],
        ),
    ]
