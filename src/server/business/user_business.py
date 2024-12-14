from http import HTTPStatus
from pymongo import MongoClient
from helpers import AppSettings, EncryptionHelper

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
        collection = UserBusiness.get_collection_reference()
        collection.insert_one(user)
