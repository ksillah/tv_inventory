from flask import Blueprint, render_template

site = Blueprint('site',__name__, template_folder='site_templates')

# ###IN the abvoe code, some arguements are specified when creating the Bluepring object
# This first arguement 'site', is the Blueprint's name,
# this will be used by flasks routing mechanism.
# The second parameter --name__, is the BP's import name,
# which flask uses to locate resources

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')

def profile(): 
    return render_template('profile.html')
