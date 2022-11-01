import os
from flask import Flask
from flask_s3 import FlaskS3
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# s3 = FlaskS3(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from vgcsc import routes, models, error
# . import models, routes

# app.register_blueprint(routes.bp)
