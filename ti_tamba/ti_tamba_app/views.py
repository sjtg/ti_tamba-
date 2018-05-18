# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import VideoLibrary

# Create your views here.

#Video Library page
def video_library(request):
    videos = VideoLibrary.objects.all()
    return render(request, 'shows/video.html', {'videos' : videos})
