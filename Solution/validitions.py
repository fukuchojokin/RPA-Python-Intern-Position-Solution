import os, cv2
import datetime


class VideoInfo:
    def __init__(self, videoFile):
        self.charge = 0
        self.videoFile = videoFile
        self.temp_path = videoFile.temporary_file_path()

    def get_extension(self):
        return os.path.splitext(self.temp_path)[1]

    def get_duration(self):
        data = cv2.VideoCapture(self.temp_path)
        frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = int(data.get(cv2.CAP_PROP_FPS))
        return int(frames / fps)

    def get_size(self):
        return int(self.videoFile.size)

    def get_charge(self):
        if self.get_size() < 524288:
            self.charge += 5
        elif 524288 < self.get_size() <= 1024**3:
            self.charge += 12.5

        if self.get_duration() < 378:
            self.charge += 12.5
        elif 378 < self.get_duration() <= 600:
            self.charge += 20

        return self.charge


def json_response(status, status_message):
    if status:
        status = "success"
    else:
        status = "error"
    return [
        {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status,
            str(status) + "_message": status_message,
        },
    ]
