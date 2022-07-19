# Create your models here.
from django.db import models


class Videos(models.Model):
    name = models.CharField(max_length=64)
    videoFile = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + " : " + self.videoFile
