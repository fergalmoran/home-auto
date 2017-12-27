from flask import jsonify
from flask_restplus import Resource, reqparse

from phue import Bridge
import ast
import colorsys

from controllers.restplus import api

ns = api.namespace('action', description='Operations related to Philips Hue lights')


class ActionController(Resource):

    def get(self):
        return 'Hello Sailor'