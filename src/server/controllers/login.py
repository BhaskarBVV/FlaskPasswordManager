from http import HTTPStatus
from business import LoginBusiness
from helpers import ResponseHandler
from exceptions import UnauthorizedException
from flask_restful_swagger_2 import Resource, request

business = LoginBusiness()

class Login(Resource):

    def post(self):
        try:
            data = request.get_json()
            # add validation on login request
            session_id = business.login(data)
            return ResponseHandler.send_response(HTTPStatus.OK, message={
                "session_id": session_id
            })
        except UnauthorizedException as e:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error=str(e))
        except Exception as e:
            return ResponseHandler.send_response(HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e))
        

