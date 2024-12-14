from http import HTTPStatus
from pymongo import MongoClient, errors
from helpers import ResponseHandler, AppSettings, ErrorMessage, EncryptionHelper

collection_ref = None


class UserBusiness:

    @staticmethod
    def get_collection_reference():
        global collection_ref

        if collection_ref == None:
            uri = AppSettings.cluster_uri
            client = MongoClient(uri)
            db = client[AppSettings.database_name]
            collection = db[AppSettings.user_collection]
            collection_ref = collection
        return collection_ref

    def add_user(request):
        try:
            username = request.json.get("username")
            email = request.json.get("email")
            password = request.json.get("password")
            first_name = request.json.get("first_name")
            last_name = request.json.get("last_name")

            encrypted_password = EncryptionHelper.encrypt_data(password)
            print(f"The hashed pass: {encrypted_password}")
            user = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": encrypted_password,
            }
            collection = UserBusiness.get_collection_reference()
            collection.insert_one(user)
            return ResponseHandler.send_response(
                HTTPStatus.CREATED, message="Successfully created a new user"
            )
        except errors.DuplicateKeyError as de:
            return ResponseHandler.send_response(
                HTTPStatus.BAD_REQUEST, error=ErrorMessage.DuplicateUsername
            )
        except Exception as e:
            return ResponseHandler.send_response(
                HTTPStatus.INTERNAL_SERVER_ERROR, error=str(e)
            )
