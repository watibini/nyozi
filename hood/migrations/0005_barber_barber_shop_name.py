# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_remove_location_hood'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='barber_shop_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
