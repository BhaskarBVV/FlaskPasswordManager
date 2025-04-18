from exceptions import UnauthorizedException
from helpers import (
    ErrorMessage,
    MongoHelper,
    AppSettings,
    EncryptionHelper,
    RequestValidator,
)


class PasswordBusiness:

    @staticmethod
    def get_mongo_client():
        return MongoHelper(AppSettings.cluster_uri)

    def get_password(self, request):
        session_info = RequestValidator.validate_request(request)
        filter = {"userid": session_info.userid}
        response = PasswordBusiness.get_mongo_client().get_all_data(
            AppSettings.password_manager_database_name,
            AppSettings.password_collection,
            filter,
        )
        passwords = PasswordBusiness.fill_passwords(response)
        return passwords

    def add_password(self, request):
        session_info = RequestValidator.validate_request(request)
        password_info = PasswordBusiness.create_new_encrypted_password(
            request, session_info.userid
        )
        PasswordBusiness.get_mongo_client().insert_data(
            AppSettings.password_manager_database_name,
            AppSettings.password_collection,
            password_info,
        )

    @staticmethod
    def add_field(key: str, value: str, dict: dict):
        if value and value.strip() != "":
            dict[key] = value

    @staticmethod
    def create_new_encrypted_password(request, user_id):
        body = request.get_json()
        website = body.get("website")
        password = body.get("password")
        username: str = body.get("username")
        email: str = body.get("email")
        info: str = body.get("info")
        encrypted_password = EncryptionHelper.encrypt_data(password)
        
        password_info = {}
        PasswordBusiness.add_field("username", username, password_info)
        PasswordBusiness.add_field("email", email, password_info)
        PasswordBusiness.add_field("website", website, password_info)
        PasswordBusiness.add_field("info", info, password_info)
        PasswordBusiness.add_field("userid", user_id, password_info)
        PasswordBusiness.add_field("password", encrypted_password, password_info)
        return password_info

    @staticmethod
    def fill_passwords(encrypted_passwords):
        passwords = []
        for _ in encrypted_passwords:
            password = {}
            PasswordBusiness.add_field("_id", str(_.get("_id")), password)
            PasswordBusiness.add_field("website", _.get("website"), password)
            PasswordBusiness.add_field("username", _.get("username"), password)
            PasswordBusiness.add_field("email", _.get("email"), password)
            PasswordBusiness.add_field("info", _.get("info"), password)
            encoded_password = _.get("password")
            decoded_password = EncryptionHelper.decrypt_data(encoded_password)
            PasswordBusiness.add_field("password", decoded_password, password)
            passwords.append(password)
        return passwords
