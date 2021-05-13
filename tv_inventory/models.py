from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid #unique user identifier. Will be used for primary keys
#adding Flask security for password protection
from werkzeug.security import generate_password_hash, check_password_hash
#import secrets module provided by python. gives us a hex value as a token
import secrets
#import flask login classes
from flask_login import UserMixin, LoginManager
#install our marshaller\
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader#looks for user id in the table
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):#gives us the table structure
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=False, default = '')
    token = db.Column(db.String, default='', unique = True)
    review = db.relationship('Review', backref = 'owner', lazy = True)

    def __init__(self, email, id='', password='', token=''):
        self.id = self.set_id()
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User:{self.email} has been created and added to the database!"

class Review(db.Model):
    id = db.Column(db.String, primary_key = True)
    show = db.Column(db.String(200), nullable = True)
    season = db.Column(db.Integer(), nullable = False)
    episode = db.Column(db.String(), nullable = False)
    rating = db.Column(db.Integer(), nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, show, season, episode, rating, user_token, id=''):
        self.id = self.set_id()
        self.show = show
        self.season = season
        self.episode = episode
        self.rating= rating
        self.user_token = user_token


    def __repr__(self):
        return f'The following show been rated: {self.show}'

    def set_id(self):
        return str(uuid.uuid4())
    
#api schema via marshmallow
class TvSchema(ma.Schema):
    class Meta:
        fields = ['id','show','season', 'episode', 'rating']
#singualar data point return
tv_schema = TvSchema()

#list of multiple objects returned
tv_schemas = TvSchema(many = True)