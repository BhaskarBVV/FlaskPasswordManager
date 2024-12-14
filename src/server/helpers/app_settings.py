import os


class AppSettings:
    password = os.getenv("MONGO_USER_PASSWORD")
    username = os.getenv("MONGO_USER_NAME")
    cluster = os.getenv("MONGO_CLUSTER")
    cluster_uri = f"mongodb+srv://{username}:{password}@{cluster}.bouoc.mongodb.net/?retryWrites=true&w=majority&appName={cluster}"
    database_name = "PasswordManager"
    user_collection = "user"


print(AppSettings.username)
