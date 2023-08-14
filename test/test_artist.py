from app.artist import fetch_artists, artist_genres
from app.playlist import fetch_playlist
import pandas as pd

def test_fetch_artists():
    df, playlist_name, owner, num_tracks = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    artists = fetch_artists(df)
    assert isinstance(artists, pd.DataFrame)
    assert 'artist_popularity' in artists.columns
    assert 'artist_genres' in artists.columns


def test_artist_genres():
    df, playlist_name, owner, num_tracks = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    artists = fetch_artists(df)
    genre_dict = artist_genres(artists)
    assert isinstance(genre_dict, dict)