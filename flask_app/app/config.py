import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_HOSTNAME = os.getenv('MONGODB_HOSTNAME', 'mongo_db')
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'db_admin')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'Password')
    MONGODB_DATABASE = os.getenv('MONGODB_DATABASE', 'user_resource')
