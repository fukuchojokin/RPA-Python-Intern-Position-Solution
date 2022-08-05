from .forms import VideoInput
from django.shortcuts import render
from .models import Video
from .validitions import VideoInfo, json_response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser


# Create your views here.
def home(request):
    return render(request, "home.html")


@api_view(["get"])
@permission_classes((permissions.AllowAny,))
def showVideos(request):
    videos = Video.objects.all().values("videoID", "videoName")
    videos = list(videos)
    return Response(videos)


class FileUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        videoName = request.POST["videoName"]
        videoFile = VideoInfo(request.FILES["videoFile"])
        form = VideoInput(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
        print(videoName, str(videoFile))
        flag = True
        if videoFile.get_extension() not in [".mkv", ".mp4"]:
            return Response(json_response("error", "Only .mkv and .mp4 supported."))
        if videoFile.get_duration() > 600:
            flag = False
            return Response(
                json_response("error", "Video can't be longer than 10 minutes.")
            )
        if videoFile.get_size() > 1024**3:
            flag = False
            return Response(
                json_response("error", "Video size can't be larger than 1 GB.")
            )
        if flag:
            form.save()
            return Response(
                json_response(
                    "success",
                    "Uploading this is going to cost you "
                    + str(videoFile.get_charge())
                    + "$",
                )
            )
        flag = False
        return Response(json_response("error", "Invalid Form"))


@api_view(["post"])
@permission_classes((permissions.AllowAny,))
def validate(request):
    flag = True
    form = VideoInput(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=False)
        video = VideoInfo(request.FILES["videoFile"])
        if video.get_extension() not in [".mkv", ".mp4"]:
            flag = False
            return Response(json_response(flag, "Only .mkv and .mp4 supported."))
        if video.get_duration() > 600:
            flag = False
            return Response(
                json_response(flag, "Video can't be longer than 10 minutes.")
            )
        if video.get_size() > 1024**3:
            flag = False
            return Response(
                json_response(flag, "Video size can't be larger than 1 GB.")
            )
        if flag:
            form.save()
            return Response(
                json_response(
                    flag,
                    "Uploading this is going to cost you "
                    + str(video.get_charge())
                    + "$",
                )
            )
        return Response(json_response(flag, "Invalid Form"))
    return Response(json_response(flag, "Invalid Form"))
