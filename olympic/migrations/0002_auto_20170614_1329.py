# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('code', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic.Games')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коды',
                'db_table': 'dzzzr_codes',
            },
        ),
        migrations.AlterModelOptions(
            name='gameadmins',
            options={'verbose_name': 'Админ ', 'verbose_name_plural': 'Админы '},
        ),
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AddField(
            model_name='codes',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympic.Teams'),
        ),
    ]
