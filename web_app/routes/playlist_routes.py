from flask import Blueprint, request, render_template, redirect, flash
import plotly.express as px

from app.playlist import url_to_id, fetch_playlist, default


playlist_routes = Blueprint("playlist_routes", __name__)


@playlist_routes.route("/playlist")
def playlist_url():
    print("PLAYLIST URL...")
    return render_template("pl_url.html")

@playlist_routes.route("/playlist/info", methods=["GET", "POST"])
def playlist_info():
    print("ABOUT THIS PLAYLIST...")

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
        data = df.to_dict('records')


        #plot bar chart for songs popularity
        fig = px.bar(df, x='track_name', y='track_popularity',title="Popularity of songs in the playlist")
        fig.update_traces(marker_color='green')
        fig.update_layout(xaxis={'categoryorder':'total descending'})
        songs_bar_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("playlist_details.html",
            name=playlist_name,
            owner=owner,
            num_tracks=num_tracks,
            data=data,
            chart_html=songs_bar_html
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/playlist")

#
# API ROUTES
#

#@audio_routes.route("/audio/data")
#def audio():
#    print("AUDIO DATA...")
#
#    # for data supplied via GET request, url params are in request.args:
#    url_params = dict(request.args)
#    print("URL PARAMS:", url_params)
#    url = url_params.get("url") or default
#
#    try:
#        id = url_to_id(url)
#        df, playlist_name, owner, num_tracks = fetch_playlist(id)
#        data = fetch_features(df)
#        avg_data = data[music_feature].mean().reset_index().rename(columns={'index':'feature',0:'value'})
#        avg_data['value'] = avg_data['value'].apply(lambda x: round(x,4))
#        data_dict = avg_data.to_dict('records')
#        return {"name": playlist_name, "data": data_dict }
#    except Exception as err:
#        print('OOPS', err)
#        return {"message":"Data Error. Please try again."}, 404