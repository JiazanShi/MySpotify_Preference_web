import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from IPython.display import Image, display
from itertools import chain
import plotly.express as px

#import api keys from api.py
from app.api import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

#connect to spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def url_to_id(url):
    ## https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2
    ## playlist_id is between the 'playlist/' and '?'

    playlist_id = url.split('/')[-1].split('?')[0]
    return playlist_id

def fetch_playlist(playlist_id):
    ## fetch playlist, extract data about tracks and artists
    ## and store in a dataframe

    try:
        pl = sp.playlist(playlist_id)
        playlist_name = pl['name']
        owner = pl['owner']['display_name']
        num_tracks = len(pl['tracks']['items'])

        track_name = []
        track_id = []
        track_popularity = []
        album_cover = []
        artist_name = []
        artist_id = []

        for track in pl['tracks']['items']:
            track_name.append(track['track']['name'])
            track_id.append(track['track']['id'])
            track_popularity.append(track['track']['popularity'])
            album_cover.append(track['track']['album']['images'][2]['url'])
            artist_name.append(track['track']['artists'][0]['name'])
            artist_id.append(track['track']['artists'][0]['id'])
        
        playlist_df = pd.DataFrame(list(zip(track_name,track_id,track_popularity, album_cover, artist_name,artist_id)),
                           columns=['track_name','track_id','track_popularity','album_cover','artist_name','artist_id'])
        
        return playlist_df, playlist_name, owner, num_tracks
    
    except:
        print("Please input a valid playlist id")


default = "https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2"
if __name__ == "__main__":
    
    input_url = input("Please input a playlist url") or default
    
    id = url_to_id(input_url)

    playlist_df, playlist_name, owner, num_tracks = fetch_playlist(id)

    for i in range(len(playlist_df)):
        print(playlist_df['track_name'].iloc[i], playlist_df['artist_name'].iloc[i])