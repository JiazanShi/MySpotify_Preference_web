# MySpotify_Preference_web

This is a platform used to analyze user's Spotify playlist data, including user's favorite artists, genres, and audio features. It helps us know better about user's music preference and taste so that software developer could develop state-of-art music recommendation algorithms.

## Setup

To get access to Spotify API, you need to apply a developer account, and get your client_id and client_secret. Please pass your client_id and client_secret in the .env file.

```sh
# this is the ".env" file (in the root directory of the repo)

SPOTIFY_CLIENT_ID="____________"
SPOTIFY_CLIENT_SECRET="____________"
```

create vitual environment for the app:

```sh
conda create -n spotipy-env python=3.10
```

Activate environment:
```sh
conda activate spotipy-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## CLI Usage

run playlist.py (return tracks in the playlist, and tracks popularity details):
```sh
python -m app.playlist
```

run artist.py that tells you what are the high-frequent artists and genres in this playlist:
```sh
python -m app.artist
```

run audio.py and get audio features:
```sh
python -m app.audio
```
## Test

To test the app, run pytest in the terminal with virtual environment:

```sh
pytest
```

## Web

This platform has 3 pages: Playlist Details, Artists, Audio Features. Just simply input the playlist URL you want to analyze, you will get the information about this playlist.

The 'Playlist Details' page returns a list of songs and artists in the playlist, and also the popularity of those songs.

The 'Artists' page tells you who is the most welcomed artist in the playlist, and the high-frequent genres in this playlist. That reflects favorite artists of the user who created the playlist, and the genres they like most

The 'Audio Features' page gives you the average audio features in this playlist, such as danceability and liveness.

```sh
FLASK_APP=web_app flask run
```

## Deploy

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service". Choose your own repository by specifying its public URL (at the bottom of the page).

Specify start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Under the "Advanced" options, set your client_id and client_secret as environment variables.

Finally, click to "Create" the web service.

