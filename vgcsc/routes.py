import os
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify, json
)
from flask_login import (
    current_user, login_user, logout_user, login_required
)
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from vgcsc import db, app
from vgcsc.models import * #Access, Membership, Profile, Executive, PastExecutive, PhotoGallery, DisplayPix,News

# bp = Blueprint('routes', __name__)
gallery_options = GalleryOptions.query.all()
@app.route('/', methods=("GET", "POST"))
@app.route('/index', methods=("GET", "POST"))
def index():
    news_feed = News.query.order_by(News.date_created.desc()).limit(3)
    
    return render_template('vgcsc/index.html', news_feed=news_feed, gallery_options=gallery_options)

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
    

@app.route("/executives/<string:option>")
def exco(option):
    # print(f"{option}")
    # return f"{option}"
    excos = Executive.query.filter_by(where=f"{option}")
    return render_template('vgcsc/executives1.html', excos=excos, gallery_options=gallery_options)

# @app.route('/history')
# def history():
#     render_template('vgcsc/history.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['GET', 'POST'])
# @login_required@app.route('/upload', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':    
        # check if the post request has the file part
        if 'file' not in request.files:
        # if 'file' not in request.form.get('file'):
            flash('No file (photo) selected', 'danger')
            return redirect(request.url)
        imglist = request.files.getlist('file') #['file']
        
        fototype = request.form.get('fototype') #request.form['photoType']
        caption = request.form.get('caption') #request.form['filecaption']
        galleryType = request.form.get('galleryType') #request.form['galleryOptions']
        if galleryType == 0 or galleryType == '0':
            if fototype == "2":
                flash('Select an option', 'warning')
                return redirect(request.url)
            galleryType = None
        print(fototype)
        print(galleryType)
        print(f"caption {caption}")
        return redirect(url_for('uploads'))
        # if user does not select file, browser also
        # submit an empty part without filename
        for img in imglist:
            # filename.rsplit('.', 1)[1].lower()
            # if len(img.filename.rsplit('.', 1)[1].lower()) <= 5:
            #     flash('Image name is too short, rename and try again', "warning")
            #     return redirect(request.url)
            if img.filename == '':
                flash('No selected file', "danger")
                return redirect(request.url)
            if img and allowed_file(img.filename):
                filename = secure_filename(img.filename)
                print(filename)
                if not os.path.isdir(os.path.join(app.config['UPLOAD_FOLDER'])):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER']))
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                if os.path.exists(path):
                    flash("File has been uploaded previously", "warning")
                    return redirect(url_for('uploads'))
                img.save(path)
                photo = PhotoGallery(name=filename,caption=caption, path=path, display_type=fototype,
                gallery_options=galleryType)
                db.session.add(photo)
                db.session.commit()
                flash("Upload successful", "success")
                return redirect(url_for('uploads'))
    photoType = DisplayPix.query.all()
    galleryOptions = GalleryOptions.query.all()
    # print(request.form['galleryOptions'])
    
    return render_template('vgcsc/uploads.html', photoType=photoType, galleryOptions=galleryOptions)

@app.route('/uploadAjax', methods=['GET', 'POST'])
def uploads_ajax():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
        # if 'file' not in request.form.get('file'):
            flash('No file (photo) selected', 'danger')
            return jsonify({"success": False, "message": "No file (photo) selected "})
        imglist = request.files.getlist('file') #['file']
        
        fototype = request.form.get('fototype') #request.form['photoType']
        caption = request.form.get('caption') #request.form['filecaption']
        galleryType = request.form.get('galleryType') #request.form['galleryOptions']
        if galleryType == 0 or galleryType == '0':
            if fototype == "2":
                flash('Select an option', 'warning')
                return jsonify({"success": False, "message": "Select an option"})
            galleryType = None
        print(fototype)
        print(galleryType)
        print(f"caption {caption}")
        return jsonify({"success": False, "message": "f{fototype}"})
        # return redirect(url_for('uploads'))
        # if user does not select file, browser also
        # submit an empty part without filename
        for img in imglist:
            # filename.rsplit('.', 1)[1].lower()
            # if len(img.filename.rsplit('.', 1)[1].lower()) <= 5:
            #     flash('Image name is too short, rename and try again', "warning")
            #     return redirect(request.url)
            if img.filename == '':
                flash('No selected file', "danger")
                return jsonify({"success": False, "message": "No selected file"})
            if img and allowed_file(img.filename):
                filename = secure_filename(img.filename)
                print(filename)
                if not os.path.isdir(os.path.join(app.config['UPLOAD_FOLDER'])):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER']))
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                if os.path.exists(path):
                    flash("File has been uploaded previously", "warning")
                    return jsonify({"success": False, "message": "File has been uploaded previously"})
                img.save(path)
                photo = PhotoGallery(name=filename,caption=caption, path=path, display_type=fototype,
                gallery_options=galleryType)
                db.session.add(photo)
                db.session.commit()
                flash("Upload successful", "success")
                return jsonify({"success": True, "message": "Upload successful"})
    photoType = DisplayPix.query.all()
    galleryOptions = GalleryOptions.query.all()
    # print(request.form['galleryOptions'])
    
    return render_template('vgcsc/uploads.html', photoType=photoType, galleryOptions=galleryOptions)
@app.route('/gallery/<int:id>')
def gallery(id):
    print(id)
    pixOptions = PhotoGallery.query.filter_by(gallery_options=id)
    name = gallery_options[id -1].name #[name for name in gallery_options if name == gallery_options.name ]
    return render_template('vgcsc/gallery.html', photos=pixOptions, gallery_options=gallery_options, name=name)

@app.route('/zones')
def zones():
    return render_template('vgcsc/zones.html', gallery_options=gallery_options)

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

@app.route('/setups', methods=["GET","POST"])
def setups():

    # if request.method == "POST":
    #     gh
        
    return "setup areas"