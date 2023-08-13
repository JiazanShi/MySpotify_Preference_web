from app.audio import url_to_id, fetch_playlist, fetch_features
import pandas as pd

def test_url_to_id():
    default = "https://open.spotify.com/playlist/3QJAP3W7ONDac1qIdTsBRJ?si=f8e17f22c0304ee2"
    assert url_to_id(default) == '3QJAP3W7ONDac1qIdTsBRJ'
    url2 = "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6?si=bdbd257672964d72"
    assert url_to_id(url2) == "37i9dQZF1DX4WYpdgoIcn6"

def test_fetch_playlist():
    result = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    assert isinstance(result, pd.DataFrame)
    assert 'track_name' in result.columns
    assert 'track_popularity' in result.columns
    assert 'artist_id' in result.columns


def test_fetch_features():
    pl = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    result = fetch_features(pl)
    assert isinstance(result, pd.DataFrame)
    assert 'danceability' in result.columns
    assert 'speechiness' in result.columns
    assert 'liveness' in result.columns
