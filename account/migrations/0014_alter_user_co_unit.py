# Generated by Django 5.0.3 on 2024-07-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='co_unit',
            field=models.CharField(blank=True, choices=[('آموزشکده فنی بندر انزلی - شهید خدادادی', 'آموزشکده فنی بندر انزلی - شهید خدادادی'), ('آموزشکده فنی رستم آباد رودبار - سیدالشهداء', 'آموزشکده فنی رستم آباد رودبار - سیدالشهداء'), ('آموزشکده فنی رشت - شهید چمران', 'آموزشکده فنی رشت - شهید چمران')], max_length=50, verbose_name='محل کار'),
        ),
    ]