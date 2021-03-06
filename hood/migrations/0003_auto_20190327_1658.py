# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_post_hood_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(blank=True, max_length=30)),
                ('business_email', models.EmailField(blank=True, max_length=70)),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='hood.Location')),
            ],
        ),
        migrations.RemoveField(
            model_name='business',
            name='neighborhood_id',
        ),
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hood_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='neighborhood_id',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='NeighbourHood',
        ),
    ]
