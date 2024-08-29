import os
from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL="/apidoc"
API_URL="/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Flask User Resource App'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

def get_db():
    client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                        port=int(os.environ['MONGODB_PORT']), 
                        username=os.environ['MONGODB_USERNAME'], 
                        password=os.environ['MONGODB_USERNAME'],
                        authSource="admin")
    db = client[os.environ['MONGODB_DATABASE']]

    return db

# server status
@app.route('/ping')
def ping_server():
    return 'pong'

# Returns a list of all users.
@app.route('/users', methods=['Get'])
def get_users():
    return 'List of users'

# Returns the user with the specified ID.
@app.route('/users/<id>', methods=['Get'])
def get_user_id(id):
    return 'User with id: ' + id

# Creates a new user with the specified data.
@app.route('/users', methods=['POST'])
def create_user():
    return 'User created'

# Updates the user with the specified ID with the new data.
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return 'User updated ' + id

# Updates the user with the specified ID with the new data.
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return 'User deleted ' + id

if __name__=='__main__':
    DEBUG_VAR = os.environ.get("APP_DEBUG", True)
    PORT_VAR = os.environ.get("APP_PORT", 8123)
    app.run(host="0.0.0.0", port=PORT_VAR, debug=DEBUG_VAR)