import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from IPython.display import Image, display
from itertools import chain
import plotly.express as px

#import api keys from api.py
from app.playlist import url_to_id, fetch_playlist
from app.api import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

#connect to spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


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

    playlist_df, playlist_name, owner, num_tracks = fetch_playlist(id)

    pl_audio = fetch_features(playlist_df)

    avg_features = pl_audio[music_feature].mean().reset_index().rename(columns={'index':'feature',0:'value'})
    
    print(avg_features)
    #[pl_audio[i].mean() for i in music_feature]

    #fig = px.line_polar(r=avg_features, theta=music_feature, line_close=True)
    #fig.update_traces(line_color='green')
    #fig.show()