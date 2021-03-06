# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('senha', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'Usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('categoria', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'db_table': 'Video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Categoria',
                'managed': True,
            },
        ),
    ]
