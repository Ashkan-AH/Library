# Generated by Django 5.0.3 on 2024-03-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام نویسنده')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('slug', models.SlugField(verbose_name='لینک')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
    ]
