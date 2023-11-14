import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from IPython.display import Image, display
from itertools import chain
import plotly.express as px

#import api keys from api.py
from app.api import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
#import functions from playlist.py
from app.playlist import url_to_id, fetch_playlist

#connect to spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_artists(playlist_df):
    my_artists = playlist_df.groupby('artist_name').agg({'track_id':'count'}).reset_index().rename(columns = {'track_id':'preference'})
    my_artists = my_artists.merge(playlist_df[['artist_name','artist_id']].drop_duplicates(),
                              left_on='artist_name',right_on='artist_name',how='inner')
    
    artist_popularity = []
    artist_genres = []
    artist_followers = []
    for id in my_artists['artist_id']:
        artist = sp.artist(id)
        artist_popularity.append(artist['popularity'])
        try:
            artist_genres.append(artist['genres'][0])
        except:
            artist_genres.append('')
        artist_followers.append(artist['followers']['total'])

    my_artists = my_artists.assign(artist_popularity=artist_popularity,
                                     artist_genres=artist_genres,
                                     artist_followers=artist_followers)
    
    return my_artists

def artist_genres(my_artists):
    genre_list = list(my_artists['artist_genres'])
    genre_dict = pd.Series(genre_list).value_counts().to_dict()

    return genre_dict

default = "https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2"
if __name__ == "__main__":
    
    input_url = input("Please input a playlist url") or default
    
    id = url_to_id(input_url)

    playlist_df, playlist_name, owner, num_tracks = fetch_playlist(id)

    artists = fetch_artists(playlist_df)

    for artist in artists['artist_name']:
        print(artist)