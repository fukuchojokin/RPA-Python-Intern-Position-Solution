from django.forms import forms

from RPA.Solution.models import Videos


class VideoInput(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['name', 'videoFile']