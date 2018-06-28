# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0007_auto_20180628_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='videoCategories',
        ),
        migrations.RemoveField(
            model_name='videolibrary',
            name='actor',
        ),
        migrations.AddField(
            model_name='actors',
            name='videoLibraries',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='videoLibraries_ref', to='ti_tamba_app.VideoLibrary'),
            preserve_default=False,
        ),
    ]
