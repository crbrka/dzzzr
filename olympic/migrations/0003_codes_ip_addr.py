# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0002_auto_20170614_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='ip_addr',
            field=models.CharField(default='127.0.0.1', max_length=16),
        ),
    ]
