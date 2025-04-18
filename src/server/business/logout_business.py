from exceptions import UnauthorizedException
from helpers import MongoHelper, AppSettings, ErrorMessage, RequestValidator


class LogoutBusiness:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    def logout(self, request):
        RequestValidator.validate_request(request)
        session_id = request.cookies.get('session_id')
        if session_id is None:
            raise ValueError(ErrorMessage.SESSION_INFO_ABSENT)
        filter = {"session_id": session_id}
        LogoutBusiness.get_mongo_client().delete_data(
            AppSettings.password_manager_database_name,
            AppSettings.session_collection,
            filter,
        )
