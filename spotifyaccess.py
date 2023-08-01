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
  seed_genres = 'classical, country', seed_tracks = None,
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
    
