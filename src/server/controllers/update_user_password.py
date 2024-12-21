from flask_restful_swagger_2 import Resource
from helpers import ResponseHandler
from http import HTTPStatus

class UpdatePassword(Resource):

    def put(self):
        try:
            ...
        except Exception as e:
            return ResponseHandler.send_response(
                HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e)
            )