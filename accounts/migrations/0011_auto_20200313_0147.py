# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-13 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200310_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
