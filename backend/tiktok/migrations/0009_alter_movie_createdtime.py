# Generated by Django 4.2.1 on 2023-05-16 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0008_alter_movie_createdtime_alter_movie_moviesrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='createdtime',
            field=models.DateTimeField(blank=None, default=datetime.datetime.now, null=None),
        ),
    ]
