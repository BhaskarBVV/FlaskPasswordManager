from http import HTTPStatus
from helpers import AppSettings, EncryptionHelper, MongoHelper


class UserBusiness:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    def add_user(request):
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        first_name = request.json.get("first_name")
        last_name = request.json.get("last_name")

        encrypted_password = EncryptionHelper.encrypt_data(password)
        user = {
            "username": username.lower(),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": encrypted_password,
        }
        UserBusiness.get_mongo_client().insert_data(
            AppSettings.database_name, AppSettings.user_collection, user
        )
