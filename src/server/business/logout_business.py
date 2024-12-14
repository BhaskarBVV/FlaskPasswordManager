from exceptions import UnauthorizedException
from helpers import MongoHelper, AppSettings, ErrorMessage

mongoHelper = None

class LogoutBusiness:

    @staticmethod
    def get_mongo_client():
        global mongoHelper
        if mongoHelper == None:
            mongoHelper = MongoHelper(AppSettings.cluster_uri)
        return mongoHelper
    
    def logout(self, request):
        headers = request.headers
        cookie = headers.get("cookie")
        if cookie == None:
            raise KeyError(ErrorMessage.SESSION_INFO_ABSENT)
        filter = {
            "session_id": cookie
        }
        data = LogoutBusiness.get_mongo_client().get_data(AppSettings.database_name, AppSettings.session_collection, filter)
        if data == None:
            raise UnauthorizedException(ErrorMessage.UNAUTHORIZED_ACCESS)
        LogoutBusiness.get_mongo_client().delete_data(AppSettings.database_name, AppSettings.session_collection, filter)
