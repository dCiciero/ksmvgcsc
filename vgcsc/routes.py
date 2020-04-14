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
from vgcsc.forms import ExecutiveSetupForm, OfficeSetupForm, NewsForm, MemberForm

def getMetro():
    mc = MetroCouncil.query.all()
    return mc

# bp = Blueprint('routes', __name__)
def save_record(data):
    db.session.add(data)
    db.session.commit()
    return 1
def getGalleryOptions():
    gallery_options = GalleryOptions.query.all()
    return gallery_options
@app.route('/', methods=("GET", "POST"))
@app.route('/index', methods=("GET", "POST"))
def index():
    news_feed = News.query.order_by(News.date_created.desc()).limit(3)
    carousel = PhotoGallery.query.filter_by(display_type = 1) 
    history = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                Suspendisse sed sem ut diam accumsan maximus sit amet eget risus.\
                Nulla maximus mollis venenatis. Maecenas sem leo, placerat id nisl placerat, pellentesque semper ante.\
                Pellentesque tincidunt finibus congue. Proin at odio vitae tortor consectetur fringilla id nec lacus.\
                Nunc pulvinar magna euismod lorem bibendum gravida. Ut pellentesque cursus nulla at varius.\
                Etiam fermentum enim egestas mi venenatis imperdiet. Nunc sed mi ac tortor condimentum porttitor in ut dolor.\
                Duis neque magna, tincidunt a elit nec, iaculis rhoncus nisi. Duis ac purus non diam lobortis rhoncus in eu urna.\
                Nulla sollicitudin metus non dapibus mollis. Etiam interdum ut augue sit amet tincidunt.\
                Vivamus ex metus, convallis vestibulum odio in, pharetra mattis ligula.\
                Proin mollis, est a consequat molestie, elit purus interdum est, sed luctus mauris lectus a tellus.\
                Morbi semper justo id mauris pretium elementum. Nunc venenatis convallis blandit.\
                Maecenas suscipit tortor eros, eget fringilla erat rutrum nec. Fusce viverra pretium eros,\
                ac vulputate ex convallis placerat. Donec non velit volutpat, pulvinar justo vel, ullamcorper orci.\
                Praesent malesuada dictum tellus, id imperdiet neque pulvinar non.\
                Fusce auctor, sapien vel pharetra iaculis, justo dui auctor felis,\
                nec pharetra tellus sapien at turpis. Nam sem mi, luctus sit amet ipsum vel, malesuada eleifend metus.\
                Cras vel tincidunt elit. Maecenas convallis faucibus nulla sed convallis. Cras vel est libero.\
                In laoreet mi posuere, rutrum lacus vitae, laoreet ante. Sed gravida lorem eu tellus laoreet volutpat.\
                Cras sed lorem sed enim bibendum iaculis a vel augue. Nullam finibus turpis justo,\
                eget euismod leo efficitur dictum. Curabitur egestas, mauris sed interdum scelerisque,\
                tortor odio convallis risus, sit amet ornare massa est eget lectus.\
                Phasellus convallis quam quis ligula efficitur euismod. Duis venenatis sed sapien ut blandit.\
                Nam sed felis ultrices, venenatis lorem ut, sollicitudin tortor. Curabitur pretium tristique lobortis."
    return render_template('vgcsc/index.html', news_feed=news_feed, 
                            gallery_options=getGalleryOptions(), carousel=carousel, history=history)

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
            user_email = current_user.email
            # print(current_user.email)
            memberlisting = Member.query.all()
            for member in memberlisting:
                member.email = member.email.strip().lower()
                if member.email == user_email:
                    memba = member
            # print(f'Current user is {current_user.id}')
            # print(f'member is {member}')
            return render_template("vgcsc/members.html", member=memba)

    else:
        flash("You have to login in to access this page")
        return redirect(url_for('login'))
    

@app.route("/executives/<string:option>")
def exco(option):
    # print(f"{option}")
    # return f"{option}"
    excos = Executive.query.filter_by(where=f"{option}")
    return render_template('vgcsc/executives1.html', excos=excos, gallery_options=getGalleryOptions())

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
        print(request.files)
        # check if the post request has the file part
        if 'file' not in request.files:
        # if 'file' not in request.form.get('file'):
            flash('No file (photo) selected', 'danger')
            return redirect(request.url)
        imglist = request.files.getlist('file') #['file']
        fototype = request.form.get('photoType') #request.form['photoType']
        caption = request.form.get('filecaption') #request.form['filecaption']
        galleryType = request.form.get('galleryOptions') #request.form['galleryOptions']
        if galleryType == 0 or galleryType == '0':
            if fototype == "2":
                flash('Select an option', 'warning')
                return redirect(request.url)
            galleryType = None
        print(f" Photo Type: {fototype}")
        print(galleryType)
        print(f"caption {caption}")
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
        
        fototype = request.form.get('fototype') #request.form['photoType']
        caption = request.form.get('caption') #request.form['filecaption']
        galleryType = request.form.get('galleryType') #request.form['galleryOptions']
        if galleryType == 0 or galleryType == '0':
            if fototype == "2":
                flash('Select an option', 'warning')
                return jsonify({"success": False, "message": "Select an option"})
            galleryType = None
        myupload = request.form.get('file')
        print(type(myupload))
        print(len(myupload))
        print(myupload)
        
        
        # if user does not select file, browser also
        # submit an empty part without filename
        # check if the post request has the file part
        if 'file' not in request.files:
        # if 'file' not in request.form.get('file'):
            flash('No file (photo) selected', 'danger')
            return jsonify(code=1002, result="File name can't be empty") #{"success": False, "message": "No file (photo) selected "}
        imglist = request.files.getlist('file') #['file']
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
    gallery_options = getGalleryOptions()
    name = gallery_options[id -1].name #[name for name in gallery_options if name == gallery_options.name ]
    return render_template('vgcsc/gallery.html', photos=pixOptions, gallery_options=getGalleryOptions(), name=name)

@app.route('/zones')
def zones():
    return render_template('vgcsc/zones.html', gallery_options=getGalleryOptions())

@app.route('/personal')
def personal():
    return render_template('vgcsc/members.html')

@app.route('/directory')
@login_required
def directory():
    if current_user.is_authenticated:
        if request.method == "GET":
            members = Member.query.order_by(Member.id).all()
            # print(f'Current user is {current_user.id}')
            # print(f'member is {members}')
            return render_template('vgcsc/directory.html', members=members)

    else:
        flash("You have to login in to access this page")
        return redirect(url_for('login'))

@app.route('/directoryedit/<int:opt>', methods=["POST", "GET"])
@login_required
def editDirectory(opt):
    print(opt)
    # mc = getMetro()
    form = MemberForm()
    # form.initiated_sc.choices = [(sc.id, sc.descr.upper()) for sc in mc[6].subcouncils]
    # form.current_sc.choices = [(sc.id, sc.descr.upper()) for sc in mc[6].subcouncils]
    if current_user.is_authenticated:
        member_details = Member.query.get(opt)
        # member_details = Member.query.get_or_404(opt)
        if request.method == "POST":
            name = form.firstname.data
            member_details.first_name = form.firstname.data # request.form.get('txt_fname')
            member_details.last_name = form.lastname.data # request.form.get('txt_lname')
            member_details.other_names = form.midname.data  # request.form.get('txt_oname')
            member_details.ksmno = form.ksmno.data   # request.form.get('txt_ksmno')
            member_details.phone = form.phone1.data  #  request.form.get('txt_phone1')
            member_details.phone2 = form.phone2.data  # request.form.get('txt_phone2')
            member_details.email = form.email.data  # request.form.get('txt_email')
            member_details.nationality = form.nationality.data  # request.form.get('txt_country')
            member_details.state_of_origin = form.state_of_origin.data  # request.form.get('cmb_state')
            member_details.home_town = form.home_town.data  # request.form.get('cmb_state')
            member_details.occupation = form.occupation.data  # request.form.get('cmb_state')
            member_details.address = form.address.data  # request.form.get('address')
            member_details.degree = form.degree_in_order.data  # request.form.get('txt_degree')
            member_details.initiated_sc = form.initiated_sc.data  # request.form.get('txt_initiated_sc')
            member_details.current_sc = form.current_sc.data  # request.form.get('txt_initiated_sc')
            member_details.status = form.membership_status.data  # request.form.get('txt_initiated_sc')
            db.session.commit()
            flash(f'Update successful.....{name}','success')
        
        return render_template('vgcsc/editdirectory.html', details = member_details, form=form)
@app.route('/setups/<string:option>', methods=["GET","POST"])
def setups(option):
    office = Offices.query.all()
    success = 0
    excos = None
    news = None
    galleries = None
    form = ExecutiveSetupForm()
    form_office = OfficeSetupForm()
    news_form = NewsForm()
    form.post.choices = [(p.post, p.post) for p in office]
    form.alias.choices = [(p.alias, p.alias) for p in office]
    if request.method == "POST":
        if option.lower() == 'gallery':
            entry = request.form.get('descr')
            print(f"{entry} {option} dd")
            if entry == "":
                flash("Enter the name of the event", "warning")
                return redirect(url_for('setups', option=option))
            event_name = GalleryOptions(name=entry)
            success = save_record(event_name)
            # flash("Record saved successfully", "success")
            # return redirect(url_for('setups', option=option))
        elif option.lower() == 'sub_exco' or option.lower() == 'zonal_exco':
            officer = Executive(name=form.name.data, post=form.post.data, elected_date=form.date_elect.data, 
                            where=form.arm.data, alias=form.alias.data)
            success = save_record(officer)
            # flash(f"Name: {form.name.data} Post: {form.post.data}", "success")
            # flash(f"Record saved successfully", "success")
            # if form.validate_on_submit():
            #     name = form.name.data
        elif option.lower() == 'office':
            post = Offices(post=form_office.post.data, alias=form_office.alias.data, arm=form_office.arm.data)
            success = save_record(post)
            # flash(f"Record saved successfully", "success")
        elif option.lower() == 'news':
            # flash(f"Current user: {current_user.id}", "success")
            news = News(topic=news_form.topic.data, content=news_form.content.data, posted_by=current_user.id)
            success = save_record(news)

        if success == 1:
            flash(f"Record saved successfully", "success")
            return redirect(url_for('setups', option=option))
    # descriptions = ["Gallery","Sub Council Executive", "Zonal Executive","Offices"]
    descriptions_dict = {"Gallery": "generic","Sub Council Executive": form, 
                "Zonal Executive": form,"Office": form_office, "News": news_form }
    for descr, formName in descriptions_dict.items():
        if option[:3].lower() in descr.lower():
            option = descr
            form = formName
            break
    if option.lower() == "Sub Council Executive".lower():
        excos = Executive.query.filter(Executive.where.in_(['KSM','LSM'])).all()
    elif option.lower() == "zonal executive":
        excos = Executive.query.filter(Executive.where.like('%Zone%')).all()
    elif option.lower() == "news":
        news = News.query.all() # News.query.order_by(News.id.desc()).limit(5).all()
    elif option.lower() == "gallery":
        galleries = GalleryOptions.query.all()
    # else:
    #     excos = None
    return render_template('vgcsc/setup.html', setup=option, form = form, office = office, 
                    excos=excos, news=news, galleries = galleries)
        
    # return "setup areas"
@app.route('/contactus', methods=["GET", "POST"])
def contactus():
    return render_template('vgcsc/contact.html')