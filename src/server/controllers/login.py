from flask_restful_swagger_2 import Resource, request
from business import LoginBusiness


class Login(Resource):

    def post(self):
        data = request.get_json()
        # add validation on login request
        return LoginBusiness.login(data)

