from http import HTTPStatus
from business import LoginBusiness
from helpers import ResponseHandler
from exceptions import UnauthorizedException
from flask_restful_swagger_2 import Resource, request
from flask import make_response

business = LoginBusiness()


class Login(Resource):

    def post(self):
        try:
            data = request.get_json()
            # add validation on login request
            session_id = business.login(data)
            response_dict = {
            "status": "success",
            "message": "Successfully logged in."
        }
            response = make_response(response_dict, HTTPStatus.OK)
            response.set_cookie(
                key = 'session_id',
                value=session_id,
                httponly=True,
                secure=True,
                samesite='Strict',
                domain='localhost:8080'
            )
            return response
        except UnauthorizedException as e:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error=str(e))
        except Exception as e:
            return ResponseHandler.send_response(
                HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e)
            )
