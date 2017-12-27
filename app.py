from flask import render_template, Blueprint, Flask
import logging.config

from livereload import Server

import settings

from controllers.endpoints.lights import ns as lights_namespace
from controllers.endpoints.camera import ns as camera_namespace
from controllers.endpoints.action import ns as action_namespace
from controllers.restplus import api
from models import db
from pages.home import home
from pages.lights import lights
from pages.camera import camera
from pages.action import action

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
    flask_app.config['EXPLAIN_TEMPLATE_LOADING'] = True



def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api.init_app(blueprint)
    api.add_namespace(lights_namespace)
    api.add_namespace(camera_namespace)
    api.add_namespace(action_namespace)

    flask_app.register_blueprint(blueprint)

    flask_app.register_blueprint(home, url_prefix='/')
    flask_app.register_blueprint(lights, url_prefix='/lights')
    flask_app.register_blueprint(camera, url_prefix='/camera')
    flask_app.register_blueprint(action, url_prefix='/action')

    db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0', port=5000)

    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
