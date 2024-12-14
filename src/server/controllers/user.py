from flask_restful_swagger_2 import Resource, request
from business import UserBusiness
from pymongo import errors
from helpers import ResponseHandler, ErrorMessage, Messages
from http import HTTPStatus

class User(Resource):

    def post(self):
        try:
            data = request.get_json()
            # Add validation to data
            UserBusiness.add_user(request)
            return ResponseHandler.send_response(
                HTTPStatus.CREATED, message=Messages.CREATED_USER
            )
        except errors.DuplicateKeyError as de:
            return ResponseHandler.send_response(
                HTTPStatus.BAD_REQUEST, error=ErrorMessage.DUPLICATE_USERNAME
            )
        except Exception as e:
            return ResponseHandler.send_response(
                HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e)
            )
