# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0005_auto_20180628_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='image_actor',
        ),
    ]
