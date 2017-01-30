# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-30 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Linea',
                'verbose_name_plural': 'Lineas',
            },
        ),
    ]