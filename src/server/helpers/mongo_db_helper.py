from pymongo import MongoClient
import threading


class MongoHelper:
    # For following the singleton design pattern, with multiple URI configuration.
    _instances = {}
    _lock = threading.Lock()  # To make this singleton class as thread safe.

    def __new__(cls, uri):
        with cls._lock:
            if uri not in cls._instances:
                # Create and store the instance for the given URI
                cls._instances[uri] = super().__new__(cls)
                cls._instances[uri].init(uri)
            return cls._instances[uri]

    def init(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)

    @staticmethod
    def get_collection_reference(client, database_name: str, collection_name: str):
        if not client or not database_name or not collection_name:
            raise ValueError("Invalid parameters for getting collection reference")
        db = client[database_name]
        return db[collection_name]

    def get_data(self, database_name: str, collection_name: str, filter: dict):
        collection = MongoHelper.get_collection_reference(
            self.client, database_name, collection_name
        )
        return collection.find_one(filter)

    def get_all_data(self, database_name: str, collection_name: str, filter: dict):
        collection = MongoHelper.get_collection_reference(
            self.client, database_name, collection_name
        )
        return collection.find(filter)

    def insert_data(self, database_name: str, collection_name: str, data: dict):
        collection = MongoHelper.get_collection_reference(
            self.client, database_name, collection_name
        )
        collection.insert_one(data)

    def delete_data(self, database_name: str, collection_name: str, data: dict):
        collection = MongoHelper.get_collection_reference(
            self.client, database_name, collection_name
        )
        collection.delete_one(data)
