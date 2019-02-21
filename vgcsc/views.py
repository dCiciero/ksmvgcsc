from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from vgcsc import app, db
# from vgcsc.models import Login, Membership, Profile

#bp = Blueprint('vgcsc', __name__)

@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("vgcsc/index.html")