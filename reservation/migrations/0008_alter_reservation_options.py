# Generated by Django 5.0.3 on 2024-08-04 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_alter_reservation_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-date_added'], 'verbose_name': 'رزرو', 'verbose_name_plural': 'رزرو\u200cها'},
        ),
    ]
