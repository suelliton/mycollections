# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0008_auto_20161223_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.CharField(choices=[('Forró', 'Forró'), ('Rock', 'Rock'), ('Pop', 'Pop'), ('Swingueira', 'Swingueira'), ('Eletrohits', 'Eletrohits'), ('Romântica', 'Romântica'), ('Asmr', 'Asmr'), ('Palestras', 'Palestras')], default='Rock', max_length=30),
        ),
    ]