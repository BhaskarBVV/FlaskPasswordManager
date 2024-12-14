from flask_restful_swagger_2 import Resource, request
from business import PasswordBusiness
from helpers import ResponseHandler, Messages
from exceptions import UnauthorizedException
from http import HTTPStatus

business = PasswordBusiness()

class Password(Resource):

    def get(self):
        return business.get_password(request)

    def post(self):
        try:
            business.add_password(request)
            return ResponseHandler.send_response(HTTPStatus.CREATED, message=Messages.PASSWORD_STORED)
        except ValueError as e:
            return ResponseHandler.send_response(HTTPStatus.BAD_REQUEST, error=str(e))
        except UnauthorizedException as e:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error=str(e))
        except Exception as e:
            return ResponseHandler.send_response(HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e))
