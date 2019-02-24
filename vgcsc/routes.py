from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask_login import (
    current_user, login_user, logout_user, login_required
)
# from werkzeug.urls import url_parse
from vgcsc import db, app
from vgcsc.models import Access, Membership, Profile

# bp = Blueprint('routes', __name__)

@app.route('/', methods=("GET", "POST"))
def index():
    return render_template('vgcsc/index.html')

@app.route('/login', methods=("GET","POST"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('membership'))
    if request.method == "POST":
        email = request.form['email']
        user = Access.query.filter_by(email=email).first()
        # if user is None or user
    
    return render_template('vgcsc/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_required
@app.route('/membership', methods=["GET", "POST"])
def membership():
    if current_user.is_authenticated:
        if request.method == "POST":
            flash("Record saved")
        else:
            return render_template("vgcsc/members.html")

    else:
        flash("You have to login in to access this page")
        return redirect(url_for('login'))
    
