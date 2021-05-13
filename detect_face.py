import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
#-----------------------------------------------------------------------------------------------------------------------
import sqlite3
import time
import datetime
import csv


import pandas as pd
from firebase import firebase



faceDetect = cv2.CascadeClassifier(
    'C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/haarcascade_frontalface_default.xml')

conn = sqlite3.connect('C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/database/database_faceR.db', check_same_thread=False)
a = conn.cursor()
b = conn.cursor()
d = conn.cursor()

class Recognate:
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

    def insert_data(ID, MSSV, FULLNAME):
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        check = "x"
        a.execute("INSERT INTO ATENDENCE (ID, MSSV ,FULLNAME, MUSTER, DAY) VALUES (?, ?,?, ?, ?)",
                  (ID, MSSV, FULLNAME, check, str(date)))
        query = "INSERT INTO ATENDENCE (ID, MSSV ,FULLNAME, MUSTER, DAY) VALUES (?, ?,?, ?, ?)", (ID, MSSV, FULLNAME, check, str(date))
        print(query)
        conn.commit()
    def EXIST_DATA(ID):
        query = "SELECT * FROM STUDENTS WHERE ID=" + str(ID)
        a.execute(query)
        b.execute("SELECT * FROM ATENDENCE WHERE ID=" + str(ID))
        temp = 0
        print(query)
        for bow in b.fetchall():
            temp = 1
        if (temp == 0):
            for row in a.fetchall():
                d.execute("UPDATE TOTALLIST SET PRESENT = PRESENT + 5 WHERE ID =" + str(ID))
                a.execute("UPDATE TOTALLIST SET STATUS = 'DAT' where LEARNING_NUMBER = PRESENT")
                a.execute("UPDATE TOTALLIST SET STATUS = 'KHONG DAT' where LEARNING_NUMBER > PRESENT")
                Recognate.insert_data(row[0], str(row[1]), str(row[2]))

        else:
            pass

    def recognite_face(self) -> bytes:
        (width, height) = (200, 200)
        size = 4
        success, imgs = self.video.read()
        mini = cv2.resize(imgs, (imgs.shape[1] // size, imgs.shape[0] // size))

        faces = faceDetect.detectMultiScale(mini)

        for f in faces:
            (x, y, w, h) = [v * size for v in f]
            cv2.rectangle(imgs, (x, y), (x + w + 10, y + h + 20), (0, 255, 0), thickness=4)
            sub_face = imgs[y:y + h, x:x + w]
            face_resize = cv2.resize(sub_face, (width, height))
            x1 = image.img_to_array(face_resize)
            x1 = np.expand_dims(x1, axis=0)
            model = load_model(
                'C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/Train_model_Face1305.hdf5')
            model.compile(loss='categorical_crossentropy',
                          optimizer=tf.keras.optimizers.Adam(lr=0.0005),
                          metrics=['accuracy'])
            images = np.vstack([x1])
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
            else:
                prediction = "Khong xac dinh"


            Recognate.EXIST_DATA(index)

            cv2.putText(imgs, prediction, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255,255 ), 1)
        ret, jpeg = cv2.imencode('.jpg', imgs)

        return jpeg.tobytes()
