# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-13 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='target_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
