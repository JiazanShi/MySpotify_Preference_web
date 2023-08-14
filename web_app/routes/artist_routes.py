from flask import Blueprint, request, render_template, redirect, flash
import plotly.express as px

from app.playlist import url_to_id, fetch_playlist, default
from app.artist import fetch_artists, artist_genres


artist_routes = Blueprint("artist_routes", __name__)


@artist_routes.route("/artist/playlist")
def playlist_url():
    print("PLAYLIST URL...")
    return render_template("artist_pl_url.html")

@artist_routes.route("/artist/info", methods=["GET", "POST"])
def artist_info():
    print("ABOUT THE ARTISTS...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    url = request_data.get("url") or default

    try:
        id = url_to_id(url)
        df, playlist_name, owner, num_tracks = fetch_playlist(id)
        artists = fetch_artists(df)
        genres = artist_genres(artists)
        artists_dict = artists.to_dict('records')


        #plot bar chart for artists
        fig = px.bar(artists, x='artist_name', y='preference' ,title=f"My Favorite Artists")
        fig.update_traces(marker_color='green')
        fig.update_layout(xaxis={'categoryorder':'total descending'})
        artist_bar_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        fig2 = px.pie(names=genres.keys(), values=genres.values(),title="Genres")
        genres_html = fig2.to_html(full_html=False, include_plotlyjs='cdn')

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("artists.html",
            artists=artists,
            genres=genres,
            artist_chart=artist_bar_html,
            genre_chart=genres_html
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/artist/playlist")