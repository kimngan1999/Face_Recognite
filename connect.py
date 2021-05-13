import sqlite3
conn = sqlite3.connect('C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/database/database_faceR.db')

c = conn.cursor()
def CREATE_TABLE():
    c.execute("CREATE TABLE IF NOT EXISTS ATENDENCE(ID INTEGER, MSSV TEXT, FULLNAME TEXT, MUSTER TEXT, DAY TEXT)")
    c.execute(
        "CREATE TABLE IF NOT EXISTS TOTALLIST (ID INTEGER PRIMARY KEY, MSSV TEXT, FULLNAME TEXT, LEARNING_NUMBER INTEGER,PRESENT INTEGER ,STATUS TEXT)")
    c.execute("INSERT INTO TOTALLIST VALUES(0,'1724801030036','PHAM PHONG HAO',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(1,'1724801030069','DO THI YEN LINH',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(2,'1724801030072','LE TRUNG LONG',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(3,'1724801030074','CHU THI LUOT',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(4,'1724801030083','TO THI KIM NGAN',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(5,'1724801030093','NGUYEN DAT PHI',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(6,'1724801030101','LE THI KIM PHUNG',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(7,'1724801030110','BUI LAM QUY',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(8,'1724801030112','DINH THI QUYNH',60,0,'CHUA')")
    c.execute("INSERT INTO TOTALLIST VALUES(9,'1724801030098','HOANG TIEN PHUC',60,0,'CHUA')")


    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS(ID INTEGER PRIMARY KEY, MSSV TEXT, FULLNAME TEXT)")
    c.execute("INSERT INTO STUDENTS VALUES(0,'1724801030036','PHAM PHONG HAO')")
    c.execute("INSERT INTO STUDENTS VALUES(1,'1724801030069','DO THI YEN LINH')")
    c.execute("INSERT INTO STUDENTS VALUES(2,'1724801030072','LE TRUNG LONG')")
    c.execute("INSERT INTO STUDENTS VALUES(3,'1724801030074','CHU THI LUOT')")
    c.execute("INSERT INTO STUDENTS VALUES(4,'1724801030083','TO THI KIM NGAN')")
    c.execute("INSERT INTO STUDENTS VALUES(5,'1724801030093','NGUYEN DAT PHI')")
    c.execute("INSERT INTO STUDENTS VALUES(6,'1724801030101','LE THI KIM PHUNG')")
    c.execute("INSERT INTO STUDENTS VALUES(7,'1724801030110','BUI LAM QUY')")
    c.execute("INSERT INTO STUDENTS VALUES(8,'1724801030112','DINH THI QUYNH')")
    c.execute("INSERT INTO STUDENTS VALUES(9,'1724801030098','HOANG TIEN PHUC')")
    conn.commit()
    conn.close()


    # def insert(id, mssv, fullname):
    #     query =" SELECT * from Students WHERE id = " + str(id)
    #     cusror = conn.execute(query)
    #     isRecordExist = 0
    #     for row in cusror:
    #         isRecordExist = 1
    #
    #     if(isRecordExist == 0):
    #         query = "INSERT INTO Students(id, mssv, fullname) VALUES (" + str(id)+",'"+str(mssv) +"','"+ str(fullname)+ "')"
    #     else:
    #         query = "UPDATE Students set mssv='"+ str(mssv) + "'," + "fullname = '" + str(fullname) + "' WHERE id = " + str(id)
    #     print(query)
    #     c.execute(query)
    #     conn.commit()
    #     conn.close()
    #
    # insert(1, '17248010300', 'Pham Phong Hao')


    # def recognite_face(self) -> str:
    #
    #     (width, height) = (200, 200)
    #     count = 0
    #     size = 4
    #     while (True):
    #         success, imgs = self.video.read()
    #         # image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    #         mini = cv2.resize(imgs, (imgs.shape[1] // size, imgs.shape[0] // size))
    #
    #         faces = faceDetect.detectMultiScale(mini)
    #         # label = "Mask" if face_rects is () else "No Mask"
    #         count += 1;
    #
    #         for f in faces:
    #             (x, y, w, h) = [v * size for v in f]
    #             cv2.rectangle(imgs, (x, y), (x + w + 10, y + h + 20), (0, 255, 0), thickness=4)
    #             sub_face = imgs[y:y + h, x:x + w]
    #             face_resize = cv2.resize(sub_face, (width, height))
    #             FaceFileName = "C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/image_predic/" + str(count) + ".jpg"
    #             cv2.imwrite(FaceFileName, face_resize)
    #             # img = image.load_img(FaceFileName)
    #             x1 = image.img_to_array(face_resize)
    #             x1 = np.expand_dims(x1, axis=0)
    #             # os.remove(FaceFileName)
    #             model = load_model(
    #                     'C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/static/models/Train_model_Face.hdf5')
    #             model.compile(loss='categorical_crossentropy',
    #                               optimizer=tf.keras.optimizers.Adam(lr=0.0005),
    #                               metrics=['accuracy'])
    #             # predicting images
    #             images = np.vstack([x1])
    #             # classes = model.predict(images)
    #             val = model.predict(images)
    #             index = 0;
    #             i = 0;
    #             for x in val[0]:
    #                 i = i + 1;
    #                 if (x > 0):
    #                     index = i - 1;
    #             if (index == 0):
    #                 prediction ="Pham Phong Hao"
    #             elif (index == 1):
    #                 prediction ="Do Thi Yen Linh"
    #             elif (index == 2):
    #                 prediction ="Le Trung Long"
    #             elif (index == 3):
    #                 prediction ="Chu Thi Luot"
    #             elif (index == 4):
    #                 prediction ="To Thi Kim Ngan"
    #             elif (index == 5):
    #                 prediction ="Nguyen Dat Phi"
    #             elif (index == 6):
    #                 prediction ="Le Thi Kim Phung"
    #             elif (index == 7):
    #                 prediction ="Bui Lam Quy"
    #             elif (index == 8):
    #                 prediction = "Dinh Thi Quynh"
    #             elif (index == 9):
    #                 prediction ="hoang tien phuc"
    #
    #
    #
    #             print(val)
    #             Recognate.EXIST_DATA(index)
    #
    #
    #             # cv2.putText(imgs, prediction, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
    #         # cv2.imshow('UNG DUNG DIEM DANH', imgs)
    #         if cv2.waitKey(1) == ord('q'):
    #              break
    #     return f'{index}'