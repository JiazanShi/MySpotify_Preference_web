from app.playlist import url_to_id, fetch_playlist
import pandas as pd

def test_url_to_id():
    default = "https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2"
    assert url_to_id(default) == '3QJAP3W7ONDac1qIdTsBRJ'
    url2 = "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6?si=bdbd257672964d72"
    assert url_to_id(url2) == "37i9dQZF1DX4WYpdgoIcn6"

def test_fetch_playlist():
    df, playlist_name, owner, num_tracks = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    assert isinstance(df, pd.DataFrame)
    assert owner == 'Jiazan'
    assert 'track_name' in df.columns
    assert 'track_popularity' in df.columns
    assert 'artist_id' in df.columns