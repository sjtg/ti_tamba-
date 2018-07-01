# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ti_tamba_app', '0004_videolibrary_image_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.CharField(max_length=50)),
                ('image_actor', models.ImageField(null=True, upload_to='Actor_Images/')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoCategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='videolibrary',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videoCategory_genre', to='ti_tamba_app.VideoCategory'),
        ),
        migrations.AddField(
            model_name='actors',
            name='videoCategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videoCategory_ref', to='ti_tamba_app.VideoCategory'),
        ),
        migrations.AddField(
            model_name='videolibrary',
            name='actor',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='actor_ref', to='ti_tamba_app.Actors'),
            preserve_default=False,
        ),
    ]