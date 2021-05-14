import os

basedir = os.path.abspath(os.path.dirname(__file__))

#gives us access to the project in any operating system
#allows outside files/folders to be added into the project from the base directory

class Config():
    # Set config variables for the flask app her
    # using env variables where available 
    # otherise create them if not done already
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turns off notificiations from database- can get annoying and take up space in teminal
    