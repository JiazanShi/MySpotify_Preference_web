from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.audio_routes import audio_routes
from web_app.routes.playlist_routes import playlist_routes
from web_app.routes.artist_routes import artist_routes



def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(playlist_routes)
    app.register_blueprint(artist_routes)
    app.register_blueprint(audio_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)