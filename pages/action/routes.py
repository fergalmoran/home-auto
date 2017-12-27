from flask import render_template

from . import action


@action.route('/')
def index():
    return render_template('action/index.html')
