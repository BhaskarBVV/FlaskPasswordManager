import os


class AppSettings:
    cluster_uri = f"{os.getenv('MONGO_URI')}&retryWrites=true&w=majority"
    database_name = "PasswordManager"
    user_collection = "user"
    session_collection = "session"
    password_collection = "password"