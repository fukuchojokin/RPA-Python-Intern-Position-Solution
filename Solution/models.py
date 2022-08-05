# Create your models here.
from django.db import models
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    path = os.path.join("videos/", filename)
    print(path)
    return path


class Video(models.Model):
    videoID = models.AutoField(primary_key=True)
    videoName = models.CharField(max_length=64)
    videoFile = models.FileField(
        upload_to=get_file_path,
        null="True",
    )

    def __str__(self):
        return str(self.videoID) + " : " + self.videoName + " : " + str(self.videoFile)
