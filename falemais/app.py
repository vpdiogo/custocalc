from flask import Flask

from falemais.ext import config


def create_app():
    app = Flask(__name__)

    config.init_app(app)

    return app
