import cv2
from fer import FER


# Access the webcam
cap = cv2.VideoCapture(0)

#FER
emotion_detector = FER(mtcnn=True)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)


    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier('d:/Teachable/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Perform emotion recognition on the detected faces
    for (x,y,w,h) in faces:
        dominant_emotion = ' '
        detected_face = frame[int(y):int(y+h), int(x):int(x+w)]
        fer_result = emotion_detector.detect_emotions(detected_face)
        
        if fer_result:
            fer_result = fer_result[0]['emotions']
            dominant_emotion = max(zip(fer_result.values(), fer_result.keys()))[1]


        # Display the results
        
        print(fer_result)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 242), 2)
        cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,242), 2)

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
