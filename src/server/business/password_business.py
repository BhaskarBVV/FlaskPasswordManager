from exceptions import UnauthorizedException
from helpers import ErrorMessage, MongoHelper, AppSettings, EncryptionHelper

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
        session_info = PasswordBusiness.validate_request(request)
        filter = {
            "userid": session_info.get("userid")
        }
        print(filter)
        response = PasswordBusiness.get_mongo_client().get_all_data(AppSettings.database_name, AppSettings.password_collection, filter)
        passwords = []
        for _ in response:
            password = {}
            password["website"] = _.get("website")
            encoded_password = _.get("password")            
            decoded_password = EncryptionHelper.decrypt_data(encoded_password)
            password["password"] = decoded_password
            passwords.append(password)
        return passwords
            
        

    def add_password(self, request):
        session_info = PasswordBusiness.validate_request(request)
        body = request.get_json()
        website = body.get('website')
        password = body.get('password')
        encrypted_passwoed = EncryptionHelper.encrypt_data(password)
        password_info = {
            "website": website,
            "password": encrypted_passwoed,
            "userid": session_info.get("userid")
        }
        PasswordBusiness.get_mongo_client().insert_data(AppSettings.database_name, AppSettings.password_collection, password_info)