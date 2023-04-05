import cv2
from deepface import DeepFace

# Load the pre-trained model
# model = DeepFace.loadModel('Emotion')

# Access the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier('d:/Teachable/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Perform emotion recognition on the detected faces
    for (x,y,w,h) in faces:
        detected_face = frame[int(y):int(y+h), int(x):int(x+w)]
        result = DeepFace.analyze(detected_face, actions=['emotion'], enforce_detection=False)

        # Display the results
        emotion = result[0]['dominant_emotion']
        print(result[0]['dominant_emotion'])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
