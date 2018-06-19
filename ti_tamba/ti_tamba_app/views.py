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
    Dashboard = VideoLibrary.objects.all().order_by("-timestamp")
    query = request.GET.get("search")
    if query:
        Dashboard = Dashboard.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(genre__icontains=query)|
            Q(age_restriction__icontains=query)|
            Q(year_of_release__icontains=query)
        ).distinct()
    return render(request, 'shows/dashboard.html', {'Dashboard' : Dashboard})

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


# Upload VideoLibrary
