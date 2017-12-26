from flask import render_template

from . import base64


@base64.route('/')
def index():
    return render_template('base64/index.html')
