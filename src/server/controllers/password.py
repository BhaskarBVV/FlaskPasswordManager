from flask_restful_swagger_2 import Resource, request
from business import PasswordBusiness


class Password(Resource):

    def get(self):
        return PasswordBusiness.get_password(request)

    def post(self):
        return PasswordBusiness.add_password(request)
