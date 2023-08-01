from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import io
import base64
from PIL import Image
import cv2
import numpy as np
import imutils
from fer import FER
import os
import logging
from spotifyaccess import get_recomendations

logging.getLogger('engineio').setLevel(logging.WARNING)

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
    face_cascade = cv2.CascadeClassifier(os.path.join(os.path.dirname(os.path.realpath(__file__)), "static", "haarcascade_frontalface_default.xml")
)
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
    
    
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    
    
    # Get the data sent by the client (assuming it's JSON)
    request_data = request.get_data()
    mood = request_data.decode('utf-8').split(' \t ')[0]
    percentage = request_data.decode('utf-8').split(' \t ')[1]
    os.system('cls')
    
    print('\n\n\n\n\n\n\n', mood,'\n\n\n\n\n')
    
    track_ids = get_recomendations(seed_genres="rock,metal,heavy-metal,death-metal,punk-rock", limit=5, target_danceability=0.5, target_energy=0.8, target_loudness=-5.94, target_acousticness=0.06, target_valence=0.5, target_tempo=120.34)


    # Process the data or do whatever you need to do with it
    # For example, echo the received data back to the client
    return ','.join(track_ids)



if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)