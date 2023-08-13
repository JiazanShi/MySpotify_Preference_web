# MySpotify_Preference_web

## Setup

create vitual environment:

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

## Usage

setup api:

```sh
python -m app.api
```

get current user top tracks:

```sh
python -m app.audio
```

## Web

```sh
FLASK_APP=web_app flask run
```

