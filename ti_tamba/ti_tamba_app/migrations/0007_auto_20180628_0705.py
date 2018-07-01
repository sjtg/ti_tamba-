# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0006_remove_actors_image_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='actor_profile',
            field=models.CharField(default=django.utils.timezone.now, max_length=550),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actors',
            name='image_actor',
            field=models.ImageField(null=True, upload_to='Actor_Images/'),
        ),
    ]