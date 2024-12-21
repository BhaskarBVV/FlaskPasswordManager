from pymongo import MongoClient

class MongoHelper():

    def __init__(self, uri):
        self.uri = uri
        self.client = MongoClient(uri)

    @staticmethod
    def get_collection_reference(client, database_name: str, collection_name: str):
        db = client[database_name]
        return db[collection_name]
    
    def get_data(self, database_name: str, collection_name: str, filter: dict):
        collection = MongoHelper.get_collection_reference(self.client, database_name, collection_name)
        return collection.find_one(filter)
    
    def get_all_data(self, database_name: str, collection_name: str, filter: dict):
        collection = MongoHelper.get_collection_reference(self.client, database_name, collection_name)
        return collection.find(filter)
    
    def insert_data(self, database_name: str, collection_name: str, data: dict):
        collection = MongoHelper.get_collection_reference(self.client, database_name, collection_name)
        collection.insert_one(data)
    
    def delete_data(self, database_name: str, collection_name: str, data: dict):
        collection = MongoHelper.get_collection_reference(self.client, database_name, collection_name)
        collection.delete_one(data)
