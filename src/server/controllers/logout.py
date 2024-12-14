from http import HTTPStatus
from exceptions import UnauthorizedException
from business import LogoutBusiness
from helpers import ResponseHandler, Messages
from flask_restful_swagger_2 import Resource, request

business = LogoutBusiness()

class Logout(Resource):

    def post(self):
        try:            
            business.logout(request)
            return ResponseHandler.send_response(http_status_code=HTTPStatus.OK, message=Messages.LOGGED_OUT)
            
        except KeyError as e:
            return ResponseHandler.send_response(HTTPStatus.BAD_REQUEST, error=str(e))
        except UnauthorizedException as e:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error=str(e))
        except Exception as e:
            return ResponseHandler.send_response(HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e))