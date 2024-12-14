from helpers import AppSettings, EncryptionHelper, ResponseHandler
from pymongo import MongoClient
from http import HTTPStatus

collection_ref = None


class LoginBusiness:

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

    def login(data):
        entered_username = data.get("username")
        entered_password = data.get("password")
        collection_ref = LoginBusiness.get_collection_reference()
        userinfo = collection_ref.find_one({"username": entered_username})
        actual_password = userinfo.get("password")
        stored_vector = EncryptionHelper.get_vector_from_password(actual_password)
        if actual_password == EncryptionHelper.encrypt_data(entered_password, stored_vector):
            return ResponseHandler.send_response(HTTPStatus.OK, message="Login success")
        else:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error="Invalid creds")

        
