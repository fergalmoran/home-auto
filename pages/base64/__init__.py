from flask import Blueprint

base64 = Blueprint('base64', __name__, template_folder='templates', static_folder='static')

from . import routes
