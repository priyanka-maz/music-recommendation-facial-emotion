# Music Recommendation by Facial Emotion Detection using FER, SpotifyAPI, Flask, OpenCV2

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="static\inside_out.png" alt="Logo" width="200">
    <h3 align="center">Inside-Out</h3>

</div>

Inside-Out is a web application that uses FER library, OpenCv's Haarcascades to detect faces and their emotion. Music is recommended using Spotify API. The website uses Python, Flask, SocketIO, HTML, CSS &amp; JS.

Inside-Out detects 7 emotions - 
<b>
- Neutral
- Happy
- Sad
- Disgust
- Fear
- Angry
- Surprise
</b>

## Screenshots


![Neutral](screenshots/Emotion&#32;Neutral.png)

![Happy](screenshots/Emotion&#32;Happy.png)

![Sad](screenshots/Emotion&#32;Sad.png)

![Disgust](screenshots/Emotion&#32;Disgust.png)

![Angry](screenshots/Emotion&#32;Angry.png)

![Fear](screenshots/Emotion&#32;Fear.png)

![Surprise](screenshots/Emotion&#32;Surprise.png)



## Setup & Use

- Clone the repository
```sh
git clone https://github.com/priyanka-maz/music-recommendation-facial-emotion.git
```

- Install requirements


> cd music-recommendation-facial-emotion
> pip install -r requirements.txt


- Go to https://developer.spotify.com/dashboard > Create app(fill the details and submit) > Settings

- Copy ClientID and ClientSecret, paste it in **.env**

- Run app.py


## Spotify API

Once the emotion is detected, the Spotify API <b>```/recommendations```</b> endpoint is used to obtain the tracks.
