# Generated by Django 4.0.6 on 2022-07-23 02:39

import Solution.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoID', models.AutoField(primary_key=True, serialize=False)),
                ('videoName', models.CharField(max_length=64)),
                ('videoFile', models.FileField(null='True', upload_to=Solution.models.get_file_path)),
            ],
        ),
    ]
