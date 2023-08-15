# Music Recommendation by Facial Emotion Detection using FER, SpotifyAPI, Flask, OpenCV2

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="static\inside_out.png" alt="Logo" width="200">
    <h3 align="center">Inside-Out</h3>

</div>

Inside-Out is a web application that uses FER library, OpenCv's Haarcascades to detect faces and their emotion. Music is recommended using Spotify API. The website uses Python, Flask, SocketIO, HTML, CSS &amp; JS.

## Screenshots

![Neutral]("screenshots/Emotion&#32;Neutral.png)


## Setup & Use

- Clone the repository
```sh
git clone https://github.com/priyanka-maz/music-recommendation-facial-emotion.git
```

- Install requirements

```sh
cd music-recommendation-facial-emotion
pip install -r requirements.txt
```

- Go to https://developer.spotify.com/dashboard > Create app(fill the details and submit) > Settings

- Copy ClientID and ClientSecret, paste it in <b>.env</b>

- Run app.py
