from flask import Blueprint

camera = Blueprint('camera', __name__, template_folder='templates', static_folder='static')

from . import routes
