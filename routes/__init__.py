from flask import Blueprint

# Initialize the Blueprint for the home and room routes
home_bp = Blueprint('home', __name__, template_folder='../templates')
room_bp = Blueprint('room', __name__, template_folder='../templates')

# Import the routes to register them with the blueprints
from .pages.home import *
from .pages.room import *