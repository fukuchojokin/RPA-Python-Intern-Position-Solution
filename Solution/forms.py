from django import forms

from .models import Video


class VideoInput(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["videoName", "videoFile"]
