from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import io
import base64
from PIL import Image
import cv2
import numpy as np
import imutils
from fer import FER


#FER
emotion_detector = FER()


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@socketio.on('image')
def image(data_image):
    
 
    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    ## converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Process the image frame


    frame = cv2.flip(frame, 1)
    
    dominant_emotion = '-'
    percentage = '-'
    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier('d:/Teachable/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)

    # Perform emotion recognition on the detected faces
    for (x,y,w,h) in faces:
        
        
        detected_face = frame[int(y):int(y+h), int(x):int(x+w)]
        fer_result = emotion_detector.detect_emotions(detected_face)
        
        if fer_result:
            fer_result = fer_result[0]['emotions']
            dominant_emotion = max(zip(fer_result.values(), fer_result.keys()))[1]
            percentage = max(fer_result.values())


    #     # Display the results
        
    #     print('\n\n\t\t' + dominant_emotion + '\n\n')
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 242), 2)
    #     cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,242), 2)
    

    # imgencode = cv2.imencode('.jpg', frame)[1]

    # # base64 encode
    # stringData = base64.b64encode(imgencode).decode('utf-8')
    # b64_src = 'data:image/jpg;base64,'
    # stringData = b64_src + stringData

    # emit the frame back
    
    emo = {'emotion': dominant_emotion, 'percentage': percentage}
    
    
    emit('response_back', emo)



if __name__ == '__main__':
    socketio.run(app, host='localhost', debug=True)