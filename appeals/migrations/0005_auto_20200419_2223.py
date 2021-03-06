# Generated by Django 3.0.5 on 2020-04-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0004_appeal_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appeal',
            old_name='text',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='appeal',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='appeal',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
    ]
