from flask import Flask, render_template, request, Response, jsonify
from flask_cors import CORS
import json
import cv2
import base64
import numpy
import random

#http://localhost:5000/homepage/

app = Flask(__name__)
CORS(app, supports_credentials=True)
English = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Italian = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


@app.route('/')
def hello_world():
    return Response('hello_world')

@app.route('/homepage/')
def homepage():
    return render_template('homepage.html')

@app.route('/learn_ASL/')
def learnASL():
    return render_template('learnASL.html')

@app.route('/learn_ISL/')
def learnISL():
    return render_template('learnISL.html')

@app.route('/level1/')
def level1():
    E = random.choice(English)
    return render_template('camera.html',jay=E)

@app.route('/level2/')
def level2():
    I = random.choice(Italian)
    return render_template('level2.html',jay=I)

@app.route('/answer_correct/')
def answer_correct():
    return render_template('answer_correct.html')

@app.route('/answer_wrong/')
def answer_wrong():
    return render_template('answer_wrong.html')

@app.route('/receiveImage/', methods=["POST"])
def receive_image():
    if request.method == "POST":
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        str_image = json_data.get("imgData")
        img = base64.b64decode(str_image)
        img_np = numpy.fromstring(img, dtype='uint8')
        new_img_np = cv2.imdecode(img_np, 1)
        cv2.imwrite('./images/rev_image.jpg', new_img_np)
        print('data:{}'.format('success'))

    return Response('upload')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)