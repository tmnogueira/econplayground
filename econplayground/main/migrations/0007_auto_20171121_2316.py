# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171117_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='score',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
    ]
