# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_barber_barber_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='work_sample',
            field=models.ImageField(default='wati.jpeg', upload_to='sample/'),
        ),
    ]
