# Generated by Django 5.0.3 on 2024-07-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_reservation_id_reservation_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تحویل'),
        ),
    ]
