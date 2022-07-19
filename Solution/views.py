from django.http import HttpResponse

from django.shortcuts import render
from .models import Videos
from .forms import VideoInput


# Create your views here.


def home(request):
    return render(request, 'home.html')


def validate(request):
    video = Videos.objects.all()
    video_file = video.videoFile
    form = VideoInput()
