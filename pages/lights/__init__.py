from flask import Blueprint

lights = Blueprint('lights', __name__, template_folder='templates', static_folder='static')

from . import routes
