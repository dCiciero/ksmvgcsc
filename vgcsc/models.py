from datetime import datetime
from vgcsc import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# lead@devpro.org/goo123

class Access(UserMixin, db.Model):
    __tablename__="access"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User {}, Email {}>'.format(self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return Access.query.get(int(id))

class Profile(db.Model):
    __tablename__ = "profiles"
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
    __tablename__ = "memberships"
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


class Carousel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    caption = db.Column(db.String(120), nullable=True)

class Executive(db.Model):
    __tablename__ = "executives"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    post = db.Column(db.String(50), nullable=False)
    elected_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    where = db.Column(db.String(5), nullable=False)
    alias = db.Column(db.String(10), nullable=False, default="")
    display_order = db.Column(db.Integer)
    

class PastExecutive(db.Model):
    __tablename__ = "pastexecutives"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    post = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    end_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    where = db.Column(db.String(5))

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.Date, index=True, default=datetime.utcnow)
    posted_by = db.Column(db.Integer, db.ForeignKey('access.id'), nullable=False)