# Generated by Django 3.2.5 on 2021-07-12 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tite',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 12, 22, 3, 44, 647090, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]