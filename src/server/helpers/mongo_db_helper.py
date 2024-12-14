from pymongo import MongoClient

class MongoHelper():

    def __init__(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)
    
    def get_data(self, database_name: str, collection_name: str, filter: dict):
        db = self.client[database_name]
        collection = db[collection_name]
        return collection.find_one(filter)
    
    def insert_data(self, database_name: str, collection_name: str, data: dict):
        db = self.client[database_name]
        collection = db[collection_name]
        collection.insert_one(data)
