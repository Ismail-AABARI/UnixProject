# dal.py
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['AnalyticsDatabase']
users_collection = db['users']

def create_user(user):
    return users_collection.insert_one(user).inserted_id

def get_user_by_email(email):
    return users_collection.find_one({'email': email})

def update_user(user_id, data):
    return users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})