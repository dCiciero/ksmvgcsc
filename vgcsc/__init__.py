import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    login.login_view = 'login'

    from vgcsc import routes, models

    return app
# . import models, routes

# app.register_blueprint(routes.bp)
