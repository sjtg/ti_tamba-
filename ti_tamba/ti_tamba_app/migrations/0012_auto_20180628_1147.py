# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0011_auto_20180628_0734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videolibrary',
            old_name='files',
            new_name='videos',
        ),
        migrations.AddField(
            model_name='videolibrary',
            name='video_trailer',
            field=models.FileField(null=True, upload_to='video/video_trailers/'),
        ),
    ]
