# Generated by Django 5.1.1 on 2024-10-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_extend'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='extend_request',
            field=models.BooleanField(default=False, verbose_name='درخواست تمدید'),
        ),
        migrations.DeleteModel(
            name='Extend',
        ),
    ]