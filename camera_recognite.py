# camera.py
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
face_cascade = cv2.CascadeClassifier("C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/haarcascade_frontalface_default.xml")
ds_factor = 0.6
datasets = 'datasets'


class VideoCameraRecognite:

    def __new__(cls, *args, **kwargs):
        if getattr(cls, '_instance', False):
            return cls._instance

        cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'video'):
            self.video = cv2.VideoCapture(0)


    def video_recognite1(self) -> bytes:
        (width, height) = (200, 200)
        count = 0
        size = 4

        success, imgs = self.video.read()
            # image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        mini = cv2.resize(imgs, (imgs.shape[1] // size, imgs.shape[0] // size))

        faces = face_cascade.detectMultiScale(mini)
        # label = "Mask" if face_rects is () else "No Mask"
        count += 1;

        for f in faces:
            (x, y, w, h) = [v * size for v in f]
            cv2.rectangle(imgs, (x, y), (x + w + 10, y + h + 20), (0, 255, 0), thickness=4)
            sub_face = imgs[y:y + h, x:x + w]
            face_resize = cv2.resize(sub_face, (width, height))
            FaceFileName = "C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/image_predic/" + str(
                count) + ".jpg"
            cv2.imwrite(FaceFileName, face_resize)
            # img = image.load_img(FaceFileName)
            x1 = image.img_to_array(face_resize)
            x1 = np.expand_dims(x1, axis=0)
            # os.remove(FaceFileName)
            model = load_model(
                    'C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/Train_model_Face.hdf5')
            model.compile(loss='categorical_crossentropy',
                              optimizer=tf.keras.optimizers.Adam(lr=0.0005),
                              metrics=['accuracy'])
            # predicting images
            images = np.vstack([x1])
            # classes = model.predict(images)
            val = model.predict(images)
            index = 0;
            i = 0;
            for x in val[0]:
                i = i + 1;
                if (x > 0):
                    index = i - 1;
            if (index == 0):
                prediction = "Pham Phong Hao"
            elif (index == 1):
                prediction = "Do Thi Yen Linh"
            elif (index == 2):
                prediction = "Le Trung Long"
            elif (index == 3):
                prediction = "Chu Thi Luot"
            elif (index == 4):
                prediction = "To Thi Kim Ngan"
            elif (index == 5):
                prediction = "Nguyen Dat Phi"
            elif (index == 6):
                prediction = "Le Thi Kim Phung"
            elif (index == 7):
                prediction = "Bui Lam Quy"
            elif (index == 8):
                prediction = "Dinh Thi Quynh"
            elif (index == 9):
                prediction = "hoang tien phuc"


            print(val)
                # ret, jpeg = cv2.imencode('.jpg', image)
                #     return jpeg.tobytes()

            cv2.putText(imgs, prediction, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
        ret, jpeg = cv2.imencode('.jpg', imgs)

        return jpeg.tobytes()

