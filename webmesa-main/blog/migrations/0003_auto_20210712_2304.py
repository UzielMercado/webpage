# Generated by Django 3.2.5 on 2021-07-12 23:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210712_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 12, 23, 4, 49, 581705, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
