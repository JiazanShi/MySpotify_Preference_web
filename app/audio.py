import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from IPython.display import Image, display
from itertools import chain
import plotly.express as px

#import api keys from api.py
from app.api import client_id, client_secret

#connect to spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
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
        print(f"You're loading {pl['owner']['display_name']}'s playlist: {pl['name']}")
        print(f"{len(pl['tracks']['items'])} songs in the current playlist")
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
        
        return playlist_df
    
    except:
        print("Please input a valid playlist id")

def fetch_features(df):
    ## extract audio features
    danceability = []
    energy = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []

    for id in df['track_id']:
        features = sp.audio_features(id)
        danceability.append(features[0]['danceability'])
        energy.append(features[0]['energy'])
        speechiness.append(features[0]['speechiness'])
        acousticness.append(features[0]['acousticness'])
        instrumentalness.append(features[0]['instrumentalness'])
        liveness.append(features[0]['liveness'])
        valence.append(features[0]['valence'])
    
    df = df.assign(danceability = danceability,
                   energy = energy,
                   speechiness = speechiness,
                   acousticness = acousticness,
                   instrumentalness = instrumentalness,
                   liveness = liveness,
                   valence = valence)
    return df


#target features
music_feature = ['danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']
default = "https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2"

if __name__ == "__main__":
    
    input_url = input("Please input a playlist url") or default
    
    id = url_to_id(input_url)

    playlist_df = fetch_playlist(id)

    pl_audio = fetch_features(playlist_df)

    avg_features = pl_audio[music_feature].mean().reset_index().rename(columns={'index':'feature',0:'value'})
    #[pl_audio[i].mean() for i in music_feature]

    #fig = px.line_polar(r=avg_features, theta=music_feature, line_close=True)
    #fig.update_traces(line_color='green')
    #fig.show()