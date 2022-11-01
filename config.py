import os
basedir = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(basedir, 'vgcsc/static/images/uploads')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'vgcsc.db') 
        #os.environ.get('DATABASE_URL') #or \
        #'sqlite:///' + os.path.join(basedir, 'vgcsc.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = upload_folder
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    APP_SETTINGS = os.environ.get('APP_SETTINGS')
    # FLASKS3_BUCKET_NAME = 'awsogcicerobucket'