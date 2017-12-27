from flask import render_template

from . import camera


@camera.route('/')
def index():
    return render_template('camera/index.html')
