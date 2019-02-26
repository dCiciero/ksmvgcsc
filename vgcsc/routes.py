from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask_login import (
    current_user, login_user, logout_user, login_required
)
from werkzeug.urls import url_parse
from vgcsc import db, app
from vgcsc.models import Access#, Membership, Profile

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
        password = request.form['password']
        user = Access.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('membership')
        return redirect(next_page)
    
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
    

# @app.route('/executives', methods=["GET", "POST"])
# def exco():
#     excos = None
#     return render_template('vgcsc/executives.html', excos=excos)