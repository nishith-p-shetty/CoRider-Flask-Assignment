import os
from pymongo import MongoClient

def get_db():
    client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                        port=int(os.environ['MONGODB_PORT']),
                        username=os.environ['MONGODB_USERNAME'],
                        password=os.environ['MONGODB_PASSWORD'],
                        authSource="admin")
    db = client[os.environ['MONGODB_DATABASE']]
    return db
