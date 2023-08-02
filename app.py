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
    
    track_ids = ""
    if (mood == 'Angry'):
        track_ids = get_recomendations(seed_genres="rock,metal,heavy-metal,death-metal,punk-rock", limit=5, target_popularity=90, target_danceability=0.73, target_energy=0.9, target_loudness=-5.39, target_acousticness=0.06, target_valence=0.47, target_tempo=150.34)
    elif (mood == 'Happy'):
        track_ids = get_recomendations(seed_genres="happy,dance,funk", limit=5, target_popularity=90, target_danceability=0.75, target_energy=0.76, target_loudness=-4.24, target_acousticness=0.32, target_valence=0.49, target_tempo=116.4)
    elif (mood == 'Sad'):
        track_ids = get_recomendations(seed_genres="emo,blues", limit=5, target_popularity=90, target_danceability=0.48, target_energy=0.32, target_loudness=-10.49, target_acousticness=0.76, target_valence=0.11, target_tempo=115)
    elif (mood == 'Fear'):
        track_ids = get_recomendations(seed_artists="5TvFfw1MgSntdU9A7yncyA,7qrYuWFTRINeUML3ptoSEk", seed_genres='', limit=5, target_popularity=85, target_danceability=0.61, target_energy=0.74, target_loudness=-5.101, target_acousticness=0.113, target_valence=0.49, target_tempo=121.1)
    elif (mood == 'Disgust'):
        track_ids = get_recomendations(seed_artists="5KKpBU5eC2tJDzf0wmlRp2,2W8yFh0Ga6Yf3jiayVxwkE,26VFTg2z8YR0cCuwLzESi2", seed_genres='', limit=5, target_danceability=0.64, target_energy=0.58, target_loudness=-6.538, target_acousticness=0.05, target_valence=0.48, target_tempo=90, target_instrumentalness=0.0014)
        #get_recomendations(seed_artists="5KKpBU5eC2tJDzf0wmlRp2,2W8yFh0Ga6Yf3jiayVxwkE,26VFTg2z8YR0cCuwLzESi2", seed_genres='', limit=15, target_danceability=0.538, target_energy=0.74, target_loudness=-5.35, target_acousticness=0.13, target_valence=0.25, target_tempo=97, target_instrumentalness=0.00467)#get_recomendations(seed_artists="5KKpBU5eC2tJDzf0wmlRp2,2W8yFh0Ga6Yf3jiayVxwkE,26VFTg2z8YR0cCuwLzESi2", seed_genres='', limit=15, target_danceability=0.64, target_energy=0.66, target_loudness=-5.538, target_acousticness=0.124, target_valence=0.51, target_tempo=124.3, target_instrumentalness=0.0014)
    elif (mood == 'Surprise'):
        track_ids = get_recomendations(seed_genres="pop", seed_artists="06HL4z0CvFAxyc27GXpf02", limit=5, target_popularity=100)
    else:
        track_ids = get_recomendations(seed_genres="classical,sleep,study", seed_artists="0Nrx6TQe5XBFEuRBhZTGpC", limit=5, target_danceability=0.56, target_energy=0.54, target_loudness=-7.85, target_acousticness=0.43, target_valence=0.40, target_tempo=123.1, target_instrumentalness=0.03)

    # Process the data or do whatever you need to do with it
    # For example, echo the received data back to the client
    return ','.join(track_ids)



if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)