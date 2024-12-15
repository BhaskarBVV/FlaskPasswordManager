from flask_restful_swagger_2 import Resource
from helpers import ResponseHandler
from http import HTTPStatus

class Health(Resource):
    
    def get(self):
        return ResponseHandler.send_response(HTTPStatus.OK, message="Healthy")