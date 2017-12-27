from flask import Blueprint

action = Blueprint('action', __name__, template_folder='templates', static_folder='static')

from . import routes
