# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0005_games_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='divider',
            field=models.IntegerField(default=3),
        ),
    ]
