# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0003_auto_20161221_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='nome',
            field=models.CharField(default='Sem nome', max_length=50),
        ),
    ]