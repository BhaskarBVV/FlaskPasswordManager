from helpers import ResponseHandler
from http import HTTPStatus


class UserBusiness:

    def add_user(request):
        return ResponseHandler.send_response(
            HTTPStatus.CREATED, message="Created a new user"
        )
