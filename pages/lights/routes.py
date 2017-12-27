from flask import render_template

from . import lights


@lights.route('/')
def index():
    return render_template('lights/index.html')
