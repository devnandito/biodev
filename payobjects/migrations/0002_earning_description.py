# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-30 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payobjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]