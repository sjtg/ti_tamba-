# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *

# Create your views here.

#Home page of the website
def home(request):
    home = VideoLibrary.objects.all()
    return render(request, 'shows/home.html', {'home' : home})


#Dashboard page

def dashboard(request):
    dashboard = VideoLibrary.objects.all().order_by("-timestamp")
    return render(request, 'shows/dashboard.html', {'dashboard' : dashboard})

#Video Library page
def video_library(request):
    videos = VideoLibrary.objects.all().order_by("-timestamp")
    return render(request, 'shows/video.html', {'videos' : videos})

#Recent videos / shows watched
def recent_video(request):
    videos = VideoLibrary.objects.all().order_by("-timestamp")
    return render(request, 'shows/video.html', {'videos' : videos})

#History of all videos / shows watched
def history_video(request):
    videos = VideoLibrary.objects.all()
    return render(request, 'shows/video.html', {'videos' : videos})

#New videos / shows
def new_video(request):
    videos = VideoLibrary.objects.all()
    return render(request, 'shows/video.html', {'videos' : videos})
