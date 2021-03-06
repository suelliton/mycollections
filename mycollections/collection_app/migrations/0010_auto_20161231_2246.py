# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0009_auto_20161223_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_temp',
            fields=[
                ('nome', models.CharField(default='', max_length=30)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('senha', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'managed': True,
                'db_table': 'Usuario_temp',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.CharField(choices=[('Forró', 'Forró'), ('Rock', 'Rock'), ('Pop', 'Pop'), ('Swingueira', 'Swingueira'), ('Sertanejo', 'Sertanejo'), ('Eletrohits', 'Eletrohits'), ('Romântica', 'Romântica'), ('Palestras', 'Palestras'), ('Outros', 'Outros')], default='Rock', max_length=30),
        ),
        migrations.AlterField(
            model_name='video',
            name='id_usuario',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='video',
            table='Video',
        ),
    ]
