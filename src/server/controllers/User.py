from flask_restful_swagger_2 import Resource, request
from business import UserBusiness


class User(Resource):

    def post(self):
        return UserBusiness.add_user(request)
