# Generated by Django 5.0.3 on 2024-03-31 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('books', '0008_alter_books_category_alter_books_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='author.author'),
        ),
    ]
