# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-13 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200413_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
