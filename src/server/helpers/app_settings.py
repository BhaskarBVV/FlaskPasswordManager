import os


class AppSettings:
    base_uri = os.getenv("MONGO_URI")
    cluster_uri = f"{base_uri}&retryWrites=true&w=majority"
    database_name = "PasswordManager"
    user_collection = "user"
    session_collection = "session"
    password_collection = "password"