from pymongo import MongoClient
from pymongo.database import Database

def get_mongo_db(mongo_uri: str, db_name: str) -> Database:
    client = MongoClient(mongo_uri)
    return client[db_name]