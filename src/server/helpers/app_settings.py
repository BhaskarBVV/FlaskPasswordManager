import os


class AppSettings:
    cluster_uri = f"{os.getenv('MONGO_URI')}"
    password_manager_database_name = "PasswordManager"
    user_collection = "user"
    session_collection = "session"
    password_collection = "password"
