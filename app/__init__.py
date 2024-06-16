from flask import Flask
from config inport Config

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)

    from . inport routes

    app.register_blueprint(routes.bp)


    return app
