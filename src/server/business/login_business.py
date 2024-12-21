import uuid
from datetime import datetime as DT
from exceptions import UnauthorizedException
from helpers import AppSettings, EncryptionHelper, MongoHelper, ErrorMessage


class LoginBusiness:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    def login(self, data):
        entered_username = data.get("username").lower()
        entered_password = data.get("password")
        filter = {"username": entered_username}
        userinfo = LoginBusiness.get_mongo_client().get_data(
            AppSettings.database_name, AppSettings.user_collection, filter
        )
        if userinfo is None:
            raise UnauthorizedException(ErrorMessage.INVALID_USERNAME_PASSWORD)
        actual_password = userinfo.get("password")
        stored_vector = EncryptionHelper.get_vector_from_password(actual_password)
        if actual_password == EncryptionHelper.encrypt_data(
            entered_password, stored_vector
        ):
            session_id = self.create_session(userinfo)
            return session_id
        else:
            raise UnauthorizedException(ErrorMessage.INVALID_USERNAME_PASSWORD)

    def create_session(slef, userinfo):
        session_id = f"session={str(uuid.uuid4())}"
        session_info = {
            "session_id": session_id,
            "username": userinfo.get("username"),
            "userid": str(userinfo.get("_id")),
            "created_at": DT.utcnow(),
        }
        LoginBusiness.get_mongo_client().insert_data(
            AppSettings.database_name, AppSettings.session_collection, session_info
        )
        return session_id
