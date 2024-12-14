from helpers import ResponseHandler
from http import HTTPStatus


class PasswordBusiness:

    def get_password(request):
        return ResponseHandler.send_response(HTTPStatus.OK, message="Here is your data")

    def add_password(request):
        return ResponseHandler.send_response(
            HTTPStatus.CREATED, message="Created new password"
        )
