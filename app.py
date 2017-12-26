from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from livereload import Server

from controllers.base64 import Base64Controller
from controllers.hue import ExecuteRecipeController, ModeController
from pages.base64 import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

# db setup
db = SQLAlchemy(app)
db.init_app(app)





@app.route('/')
def default_index():
    return render_template('home.html')


# Blueprints setup
app.register_blueprint(base64, url_prefix='/base64')

# API setup
api = Api(app)
api.add_resource(Base64Controller, '/api/base64')
api.add_resource(ExecuteRecipeController, '/api/lights/recipe')
api.add_resource(ModeController, '/api/lights/mode')

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0', port=5000)

    app.run(debug=True, host='0.0.0.0', port=5000)
