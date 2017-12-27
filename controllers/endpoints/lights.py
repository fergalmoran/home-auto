from flask import jsonify
from flask_restplus import Resource, reqparse

from phue import Bridge
import ast
import colorsys

from controllers.restplus import api

ns = api.namespace('lights', description='Operations related to Philips Hue lights')


class HueController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._BRIDGE_IP = "10.1.1.20"
        self._bridge = Bridge(self._BRIDGE_IP)
        self._lights = self._bridge.get_light_objects('name')

    def __hex2rgb(self, hex):
        return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

    def _execute_recipe(self, light, recipe):
        if light in self._lights:
            l = self._lights[light]

            l.on = recipe["on"]
            l.brightness = recipe["brightness"] or l.brightness

            # set colour
            r = recipe['rgb'] if recipe['rgb'] is not None else None
            if r is not None:
                rgb = self.__hex2rgb(r)
                h, s, v = colorsys.rgb_to_hsv(*rgb)
                l.hue = h * 65535
                l.sat = s * 255
                l.bri = v


@ns.route('/')
class ListController(HueController):
    def get(self):
        result = []
        for k, v in self._lights.items():
            result.append(k)

        return jsonify(result)


class RecipeController(Resource):
    def get(self):
        pass

    def post(self):
        pass


@ns.route('/recipe/execute')
class ExecuteRecipeController(HueController):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mode', type=str, location='json')

        args = parser.parse_args()
        mode = ast.literal_eval(args['mode'])

        for k, v in mode.items():
            self._execute_recipe(k, v)


class ModeController(HueController):
    MODES = {
        "morning": {
        },
        "evening": {
            "description": "Evening Time",
            "modes": {
                "Living Room": {
                    "on": True,
                    "brightness": 110,
                    "colour": "red"
                }, "Penny": {
                    "status": "off",
                    "brightness": 110,
                    "colour": "red"
                }, "Hallway": {
                    "status": "off",
                    "brightness": 110,
                    "colour": "red"
                }
            }
        },
        "night": {

        }
    }

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('mode', type=str, location='json')

            args = parser.parse_args()
            mode = args['mode']

            if mode in self.MODES:
                for k, v in self.MODES[mode]['modes'].items():
                    if k in self._lights:
                        light = self._lights[k]
                        light.on = v['on']

            return jsonify({"success": True})

        except Exception as e:
            print(e)

