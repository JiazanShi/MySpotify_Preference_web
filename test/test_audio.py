from app.playlist import fetch_playlist
from app.audio import fetch_features
import pandas as pd





def test_fetch_features():
    df, playlist_name, owner, num_tracks = fetch_playlist('3QJAP3W7ONDac1qIdTsBRJ')
    result = fetch_features(df)
    assert isinstance(result, pd.DataFrame)
    assert 'danceability' in result.columns
    assert 'speechiness' in result.columns
    assert 'liveness' in result.columns
