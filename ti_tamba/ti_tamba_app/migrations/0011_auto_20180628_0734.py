# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0010_auto_20180628_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='videoLibraries',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoLibraries_ref', to='ti_tamba_app.VideoLibrary'),
        ),
    ]
