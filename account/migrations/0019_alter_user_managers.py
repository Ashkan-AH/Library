# Generated by Django 5.0.3 on 2024-08-04 21:24

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.UserManager2()),
            ],
        ),
    ]
