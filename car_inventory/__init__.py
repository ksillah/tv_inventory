from flask import Flask 
from config import Config
from .site.routes import site
from .authentication.routes import auth

app = Flask(__name__)#name = drone_inventory

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)