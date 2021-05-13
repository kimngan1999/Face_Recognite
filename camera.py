# camera.py
import cv2
import os
import time
from flask import Response
from pathlib import Path
import uuid
from contextlib import contextmanager
from typing import Callable
from random import seed
from random import random
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
face_cascade = cv2.CascadeClassifier("C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/haarcascade_frontalface_default.xml")
ds_factor = 0.6
datasets = 'datasets'


class VideoCamera:

    def __new__(cls, *args, **kwargs):
        if getattr(cls, '_instance', False):
            return cls._instance

        cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'video'):
            self.video = cv2.VideoCapture(0)
            # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    def get_frame(self) -> bytes:
        success, image = self.video.read()

        if not success:
            return b''

        image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


            break
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def save_to_dataset(self, mssv) -> str:
        path = "C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/img/" + str(mssv)
        os.mkdir(path)
        (width, height) = (200, 200)

        count= 0
        size = 4
        while (count < 100):
                success, image = self.video.read()

                mini = cv2.resize(image, (image.shape[1] // size, image.shape[0] // size))

                faces = face_cascade.detectMultiScale(mini)
                # label = "Mask" if face_rects is () else "No Mask"
                count += 1;
                if faces is ():
                    count += 1
                    isSusses = 100
                    pass
                else:

                    for f in faces:
                        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
                        cv2.rectangle(image, (x, y), (x + w + 10, y + h + 20), (0, 255, 0), thickness=4)
                        sub_face = image[y:y + h, x:x + w]
                        face_resize = cv2.resize(sub_face, (width, height))
                        FaceFileName = "C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/img/" + str(mssv)+"/"+ str(count) + ".jpg"
                        cv2.imwrite(FaceFileName, face_resize)
                key = cv2.waitKey(10)

                # if Esc key is press then break out of the loop
                if key == 27 or count == 100:  # The Esc key
                    isSusses = 100
                    break

        return f'{isSusses} đang được lưu vào hệ thống'
