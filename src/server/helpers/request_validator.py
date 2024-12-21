from models import SessionInfo
from exceptions import UnauthorizedException
from helpers import ErrorMessage, MongoHelper, AppSettings


class RequestValidator:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    @staticmethod
    def validate_request(request) -> SessionInfo:
        headers = request.headers
        cookie = headers.get("cookie")
        if cookie is None:
            raise ValueError(ErrorMessage.SESSION_INFO_ABSENT)
        filter = {"session_id": cookie}
        user_info = RequestValidator.get_mongo_client().get_data(
            AppSettings.password_manager_database_name,
            AppSettings.session_collection,
            filter,
        )
        if user_info is None:
            raise UnauthorizedException(ErrorMessage.UNAUTHORIZED_ACCESS)
        return SessionInfo(user_info.get("username"), user_info.get("userid"))
