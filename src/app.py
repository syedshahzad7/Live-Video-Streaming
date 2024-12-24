from flask import Flask, render_template, Response
import cv2
from src.utils import generate_frames

app = Flask(__name__)
camera = cv2.VideoCapture(0)            #camera is an object of OpenCV. VideoCapture(0) indicates we use this object to capture(read) the video or images from the webcam of our computer(thats why 0, otherwise ip address of some other video recording device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(camera), mimetype = 'multipart/x-mixed-replace; boundary = frame')






if __name__ == '__main__':
    app.run(debug=True)