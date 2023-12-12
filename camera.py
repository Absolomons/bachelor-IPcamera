import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import time
from datetime import datetime
import numpy as np

class VideoCamera(object):
    def __init__(self, file_type  = ".jpg", photo_string= "stream_photo"):
        self.vs = PiVideoStream().start()
        self.file_type = file_type
        self.photo_string = photo_string
        time.sleep(0.5)

    def __del__(self):
        self.vs.stop()


    def get_frame(self):
        frame = self.vs.read()
        ret, jpeg = cv.imencode(self.file_type, frame)
        self.previous_frame = jpeg
        return jpeg.tobytes()
