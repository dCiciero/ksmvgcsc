from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask_login import (
    current_user, login_user, logout_user, login_required
)
from werkzeug.urls import url_parse
from werkzeug import secure_filename
from vgcsc import db, app
from vgcsc.models import Access, Membership, Profile, Executive, PastExecutive

# bp = Blueprint('routes', __name__)

@app.route('/', methods=("GET", "POST"))
@app.route('/index', methods=("GET", "POST"))
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
            next_page = url_for('index')
        print(user)
        return redirect(next_page)
    
    return render_template('vgcsc/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/membership', methods=["GET", "POST"])
@login_required
def membership():
    if current_user.is_authenticated:
        if request.method == "POST":
            flash("Record saved")
        else:
            id = current_user.id
            member = Membership.query.filter_by(access_id=id).first()
            # print(f'Current user is {current_user.id}')
            # print(f'member is {member}')
            return render_template("vgcsc/members.html", member=member)

    else:
        flash("You have to login in to access this page")
        return redirect(url_for('login'))
    

@app.route('/executives', methods=["GET", "POST"])
def exco():
    excos = Executive.query.all()
    return render_template('vgcsc/executives.html', excos=excos)

# @app.route('/history')
# def history():
#     render_template('vgcsc/history.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/gallery')
def gallery():
    return render_template('vgcsc/gallery.html')

@app.route('/zones')
def zones():
    return render_template('vgcsc/zones.html')

@app.route('/personal')
def personal():
    return render_template('vgcsc/members.html')

@app.route('/directory')
@login_required
def directory():
    if current_user.is_authenticated:
        if request.method == "GET":
            members = Profile.query.all()
            # print(f'Current user is {current_user.id}')
            # print(f'member is {members}')
            return render_template('vgcsc/directory.html')

    else:
        flash("You have to login in to access this page")
        return redirect(url_for('login'))
    