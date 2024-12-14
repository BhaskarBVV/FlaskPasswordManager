from http import HTTPStatus
from helpers import ResponseHandler, MongoHelper,\
        AppSettings, ErrorMessage, Messages

mongoHelper = None

class LogoutBusiness:

    @staticmethod
    def get_mongo_client():
        global mongoHelper
        if mongoHelper == None:
            mongoHelper = MongoHelper(AppSettings.cluster_uri)
        return mongoHelper
    
    def logout(self, headers):
        cookie = headers.get("cookie")
        filter = {
            "session_id": cookie
        }
        data = LogoutBusiness.get_mongo_client().get_data(AppSettings.database_name, AppSettings.session_collection, filter)
        if data == None:
            return ResponseHandler.send_response(HTTPStatus.UNAUTHORIZED, error=ErrorMessage.UNAUTHORIZED_ACCESS)
        LogoutBusiness.get_mongo_client().delete_data(AppSettings.database_name, AppSettings.session_collection, filter)
        return ResponseHandler.send_response(http_status_code=HTTPStatus.OK, message=Messages.LOGGED_OUT)
        