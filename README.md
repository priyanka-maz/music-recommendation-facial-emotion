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
#####<center>Neutral</center>
###
![Happy](screenshots/Emotion&#32;Happy.png)
#####<center>Happy</center>
###
![Sad](screenshots/Emotion&#32;Sad.png)
#####<center>Sad</center>
###
![Disgust](screenshots/Emotion&#32;Disgust.png)
#####<center>Disgust</center>
###
![Angry](screenshots/Emotion&#32;Angry.png)
#####<center>Angry</center>
###
![Fear](screenshots/Emotion&#32;Fear.png)
#####<center>Fear</center>
###
![Surprise](screenshots/Emotion&#32;Surprise.png)
#####<center>Surprise</center>



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
