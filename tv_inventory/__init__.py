from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate 
from tv_inventory.models import db as root_db, login_manager, ma 

from flask_cors import CORS
from tv_inventory.helpers import JSONEncoder

app = Flask(__name__)#name = drone_inventory

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)

login_manager.login_view = 'auth.signin' #specifying a route for non authorized users

ma.init_app(app)
CORS(app)

app.json_encoder = JSONEncoder

from tv_inventory import models