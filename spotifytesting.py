from dotenv import load_dotenv
from requests import post, get
import os
import base64
import json

load_dotenv()

#getting client_id and secret from environment variables file
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_token():
    
    #Visit https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow for more information
    
    #base64 encoding
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
    
    url = 'https://accounts.spotify.com/api/token'
    
    headers = {'Authorization': 'Basic ' + auth_base64, 'Content-Type': 'application/x-www-form-urlencoded'}
    
    data = {'grant_type': 'client_credentials'}
    
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}


def search_track(search_query, limit, offset = 0, token = get_token()):
    
    headers = get_auth_header(token)
    url = 'https://api.spotify.com/v1/search'
    query = f'?q={search_query}&type=track&limit={limit}&offset={offset}&market=IN'
    
    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    track_info = json_result['tracks']['items']
    
    for i in range(len(track_info)):
        link = track_info[i]['external_urls']['spotify']

        print(str(i+1) + ' . '+ str(track_info[i]['name']) +'\t' + str(link))
    

def get_recomendations(limit = 20, market = 'IN', seed_artists = None,
  seed_genres = 'classical, country', seed_tracks = None, max_acousticness = None,
  max_danceability = None, max_energy = None,
  max_instrumentalness = None, max_key = None, max_liveness = None,
  max_loudness = None, max_mode = None, max_popularity = None,
  max_speechiness = None, max_tempo = None,
  max_time_signature = None, max_valence = None,
  min_acousticness = None, min_danceability = None,
   min_energy = None,
  min_instrumentalness = None, min_key = None, min_liveness = None,
  min_loudness = None, min_mode = None, min_popularity = None,
  min_speechiness = None, min_tempo = None,
   min_valence = None,
  target_acousticness = None, target_danceability = None,
  target_energy = None, target_loudness = None,
  target_instrumentalness = None, target_key = None,
  target_liveness = None, target_mode = None,
  target_popularity = None, target_speechiness = None,
  target_tempo = None,
  target_valence = None, token = get_token()):
    
    headers = get_auth_header(token)
    
    url = 'https://api.spotify.com/v1/recommendations' 
    
      
    query = f'?limit={limit}&market=IN'\
    f'{f"&target_valence={target_valence}" if target_valence else ""}'\
    f'{f"&target_loudness={target_loudness}" if target_loudness else ""}'\
    f'{f"&target_instrumentalness={target_instrumentalness}" if target_instrumentalness else ""}'\
    f'{f"&target_speechiness={target_speechiness}" if target_speechiness else ""}'\
    f'{f"&target_acousticness={target_acousticness}" if target_acousticness else ""}'\
    f'{f"&target_tempo={target_tempo}" if target_tempo else ""}'\
    f'{f"&target_liveness={target_liveness}" if target_liveness else ""}'\
    f'{f"&target_energy={target_energy}" if target_energy else ""}'\
    f'{f"&target_popularity={target_popularity}" if target_popularity else ""}'\
    f'{f"&target_danceability={target_danceability}" if target_danceability else ""}'\
    f'{f"&target_mode={target_mode}" if target_mode else ""}'\
    f'{f"&target_key={target_key}" if target_key else ""}'\
    f'{f"&seed_artists={seed_artists}" if seed_artists else ""}'\
    f'{f"&seed_genres={seed_genres}" if seed_genres else ""}'\
    f'{f"&seed_tracks={seed_tracks}" if seed_tracks else ""}'



    #query ="?limit=10&market=ES&seed_artists=4YRxDV8wJFPHPTeXepOstw&seed_genres=indian%2C+k-pop"
    
    print(query)
    
    track_ids = []
    
    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print (result)
    track_info = json_result['tracks']

    for i in range(len(track_info)):
        print("\n", i+1, " . ", track_info[i]['name'], " | ", end=" ")
        print(track_info[i]['artists'][0]['name'], end=" ")
        print(track_info[i]['external_urls']['spotify'])
        track_ids.append(track_info[i]['id'])
    
    return track_ids
    
    
    





#Angry
get_recomendations(seed_genres="rock,metal,heavy-metal,death-metal,punk-rock", limit=15, target_popularity=100, target_danceability=0.5, target_energy=0.8, target_loudness=-5.94, target_acousticness=0.06, target_valence=0.5, target_tempo=120.34)

#happy_tracks
print("\n\n Happy tracks")
get_recomendations(seed_genres="indian", limit=10, target_popularity=100, target_danceability=0.62, target_acousticness=0.12, target_energy=0.75 ,target_valence=0.57, target_loudness=-7.27 , target_tempo=124.2)
    
#sad_tracks
print("\n\n Sad tracks")
get_recomendations(seed_genres="indian", limit=10, target_popularity=100, target_danceability=0.49, target_acousticness=0.57, target_energy=0.38 ,target_valence=0.19, target_loudness=-10.56, target_tempo=115.5)