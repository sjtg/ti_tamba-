# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
# from django.template import RequestContext
# from django.http import JsonResponse
from .models import *
from .forms import *
from django.utils import timezone

import time

# Create your views here.

#Home page of the website
def Home(request):
    home = VideoLibrary.objects.all()
    return render(request, 'shows/home.html', {'home' : home})


#Dashboard page
@login_required
def Dashboards(request):
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
    return render(request, 'shows/dashboard.html', {'new_video' : Dashboard,})


#Video Library page
@login_required
def VideoLibraries(request):
    videos = VideoLibrary.objects.all().order_by("-timestamp")
    return render(request, 'shows/video.html', {'videos' : videos})

#Recent videos / shows watched
# def recent_video(request):
#     videos = VideoLibrary.objects.all().order_by("-timestamp")
#     return render(request, 'shows/video.html', {'videos' : videos})

#History of all videos / shows watched
# def history_video(request):
#     videos = VideoLibrary.objects.all()
#     return render(request, 'shows/video.html', {'videos' : videos})

#New videos / shows
# def new_video(request):
#     videos = VideoLibrary.objects.all()
#     return render(request, 'shows/video.html', {'videos' : videos})

#media player
def mediaPlayer(request):
    medias = VideoLibra.objects.all()
    return render(request, 'shows/video.html', {'new_video' : medias})

#video detail function
def video_detail(request, pk):
    posts = get_object_or_404(VideoLibrary, pk=pk)
    return render(request, 'shows/video_detail.html', {'new_video': posts})


# Upload VideoLibrary
@login_required
def UploadVideo(request):
    # if request.user.is_staff or request.user.is_superuser
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save() #commit=False
            new_video.user = request.user
            new_video.save()
            return redirect('home')
    else:
        form = VideoForm()

    return render(request, 'shows/upload.html', { 'form' : form})





# Edit function
@login_required
def EditVideos(request, pk):
    # if request.user.is_staff or request.user.is_superuser
    new_photo = get_object_or_404(VideoLibrary, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=new_video)
        if form.is_valid():
            new_video = form.save() #commit=False
            new_video.user = request.user
            new_video.uploaded_at = timezone.now()
            new_video.save()
            return redirect('video_detail', pk=new_video.pk)
    else:
        form = PhotoForm(instance=new_video)

    return render(request, 'album/edit.html', { 'form' : form})
