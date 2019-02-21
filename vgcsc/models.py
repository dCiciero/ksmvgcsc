from datetime import datetime
from vgcsc import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    other_names=db.Column(db.String(75), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone1 = db.Column(db.String(20), nullable=False)
    phone2 = db.Column(db.String(20), nullable=True)
    occupation = db.Column(db.String(150), nullable=True)
    work_place = db.Column(db.String(150), nullable=True)
    work_address = db.Column(db.String(200), nullable=True)

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    other_names=db.Column(db.String(75), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    initiation_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    investiture_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    home_town = db.Column(db.String(120), nullable=True)


