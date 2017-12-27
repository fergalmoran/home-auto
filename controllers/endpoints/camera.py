from flask import jsonify
from flask_restplus import Resource, reqparse

from phue import Bridge
import ast
import colorsys

from controllers.restplus import api

ns = api.namespace('camera', description='Operations related to Philips Hue lights')


class CameraController(Resource):

    def get(self):
        return 'Hello Sailor'