from http import HTTPStatus
from helpers import ResponseHandler, ErrorMessage, \
    MongoHelper, AppSettings, EncryptionHelper
from exceptions import UnauthorizedException
import uuid

mongoHelper = None

class PasswordBusiness:

    @staticmethod
    def get_mongo_client():
        global mongoHelper
        if mongoHelper == None:
            mongoHelper = MongoHelper(AppSettings.cluster_uri)
        return mongoHelper

    def validate_request(request):
        headers = request.headers
        cookie = headers.get("cookie")
        if cookie is None:
            raise ValueError(ErrorMessage.SESSION_INFO_ABSENT)
        filter = {
            "session_id": cookie
        }
        user_info = PasswordBusiness.get_mongo_client().get_data(AppSettings.database_name, AppSettings.session_collection, filter)
        if user_info is None:
            raise UnauthorizedException(ErrorMessage.UNAUTHORIZED_ACCESS)
        return user_info

    def get_password(self, request):
        return ResponseHandler.send_response(HTTPStatus.OK, message="Here is your data")

    def add_password(self, request):
        user_info = PasswordBusiness.validate_request(request)
        body = request.get_json()
        website = body.get('website')
        password = body.get('password')
        encrypted_passwoed = EncryptionHelper.encrypt_data(password)
        password_info = {
            "website": website,
            "password": encrypted_passwoed,
            "user_id": str(user_info.get("_id"))
        }
        PasswordBusiness.get_mongo_client().insert_data(AppSettings.database_name, AppSettings.password_collection, password_info)