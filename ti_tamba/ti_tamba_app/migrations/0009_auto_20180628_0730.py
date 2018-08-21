# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0008_auto_20180628_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolibrary',
            name='genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoCategory_genre', to='ti_tamba_app.VideoCategory'),
        ),
    ]
