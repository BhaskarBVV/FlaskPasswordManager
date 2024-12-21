from exceptions import UnauthorizedException
from helpers import MongoHelper, AppSettings, ErrorMessage, RequestValidator


class LogoutBusiness:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    def logout(self, request):
        RequestValidator.validate_request(request)
        cookie = request.headers.get("cookie")
        filter = {"session_id": cookie}
        LogoutBusiness.get_mongo_client().delete_data(
            AppSettings.password_manager_database_name,
            AppSettings.session_collection,
            filter,
        )
