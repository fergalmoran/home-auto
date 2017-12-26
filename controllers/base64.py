import base64
from flask import jsonify
from flask_restful import Resource, reqparse


class Base64Controller(Resource):
    def get(self):
        return {"response": "hello base64"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('inputstring', type=str, location='json')
        parser.add_argument('direction', type=str, location='json')

        args = parser.parse_args()

        input_string = args['inputstring']
        direction = args['direction']

        if direction == '0':
            # from plain to base64
            output_string = base64.b64decode(input_string)
        else:
            # from base64 to plain
            output_string = base64.b64encode(input_string.encode('utf-8'))

        return jsonify(outputstring=str(output_string.decode("utf-8")))

