# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db import models

# Create your models here.

#vide types
class VideoCategory(models.Model):
    videoCategory = models.CharField(max_length=50)

    def __unicode__(self):
        videoCategory = str(self.videoCategory)
        return videoCategory


# video library
class VideoLibrary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=550, blank=True)
    genre = models.ForeignKey(VideoCategory, blank=True,null=True, related_name="videoCategory_genre")
    # actor = models.ForeignKey(Actors, related_name="actor_ref")
    age_restriction = models.IntegerField(default=0)
    year_of_release = models.DateTimeField(u'Day of Release', help_text=u'Day of the Release')
    image_poster = models.ImageField(upload_to='posters/', blank=False, null=True)
    files = models.FileField(upload_to='videos/', blank=False, null=True)
    uploaded_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        title = str(self.title)
        return title

#Actor models
class Actors(models.Model):
    actors = models.CharField(max_length=50)
    actor_profile = models.CharField(max_length=550)
    image_actor = models.ImageField(upload_to='Actor_Images/', blank=False, null=True)
    videoLibraries = models.ForeignKey(VideoLibrary,blank=True, null=True, related_name='videoLibraries_ref')

    def __unicode__(self):
        actors = str(self.actors)
        return actors
