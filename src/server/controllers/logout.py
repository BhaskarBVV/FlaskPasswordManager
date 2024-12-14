from business import LogoutBusiness
from flask_restful_swagger_2 import Resource, request

business = LogoutBusiness()

class Logout(Resource):

    def post():
        business.logout(request)