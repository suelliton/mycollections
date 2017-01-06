# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0005_auto_20161221_2210'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.CharField(choices=[('fr', 'Forró'), ('rc', 'Rock'), ('pp', 'Pop'), ('sw', 'Swingueira')], default='rc', max_length=30),
        ),
        migrations.AlterField(
            model_name='video',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection_app.Usuario'),
        ),
    ]