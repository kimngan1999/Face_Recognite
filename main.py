
from flask import Flask, render_template, request, url_for,redirect
import pickle
import subprocess
app = Flask(__name__)
#----------------
import sqlite3
import time
import datetime
import csv

from flask import Flask, render_template, Response
from camera import VideoCamera
from detect_face import Recognate
from camera_recognite import VideoCameraRecognite


#----------------------------
@app.route('/')
def index():
    return render_template('homepage.html')





@app.route('/ghidanh', methods= ["GET","POST"])
def ghidanh():
        req = request.form
        mssv = req.get("mssv")

        response_data_collection = VideoCamera().save_to_dataset(mssv)
        response_data_collection = "Done with Collecting Data" if response_data_collection else "Do nothing"


        return render_template('register.html', alert=response_data_collection)

@app.route('/finish', methods= ["GET","POST"])
def finish():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    con = sqlite3.connect('C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/database/database_faceR.db',
                          check_same_thread=False)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ATENDENCE")
    with open('list.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # csv_writer.writerow([""])
        #
        # csv_writer.writerow([""])
        # csv_writer.writerow(["ID", "MSSV", "HỌ VÀ TÊN","ĐIỂM DANH", "NGÀY"])
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    cursor .close()
    return redirect("/")

def gen(camera):
    while True:
        frame: bytes = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/attendance')
def attendance():
    # VideoCameraRecognite().video_recognite()
    return render_template('attendance.html')






def gen1(detect_face):
    while True:
        recog: bytes = detect_face.recognite_face()
        yield (b'--recog\r\n'
               b'Content-Type: imgs/jpeg\r\n\r\n' + recog + b'\r\n\r\n')

@app.route('/video_recognite')
def video_recognite():
    return Response(gen1(Recognate()),
                    mimetype='multipart/x-mixed-replace; boundary=recog')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/statistic')
def statistics():
    con = sqlite3.connect('C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/database/database_faceR.db',
                          check_same_thread=False)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from TOTALLIST")

    rows = cur.fetchall();
    return render_template("statistic.html", rows=rows)



@app.route('/complete')
def diemdanh():
    con = sqlite3.connect('C:/Users/KIMNGAN/PycharmProjects/Face_Recognite/database/database_faceR.db', check_same_thread=False)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from ATENDENCE order by DAY ")

    rows = cur.fetchall();
    return render_template("ketqua.html", rows=rows)




if __name__ == '__main__':
    app.run()
