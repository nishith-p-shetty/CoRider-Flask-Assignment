from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from app.models import get_db

user_blueprint = Blueprint('user_blueprint', __name__)

# Server Status
@user_blueprint.route('/ping', methods=['GET'])
def ping_server():
    return jsonify({"status": "pong"})

# Returns a list of all users.
@user_blueprint.route('/', methods=['GET'])
def get_users():
    db = get_db()
    users = list(db.users.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 200

# Returns the user with the specified ID.
@user_blueprint.route('/<id>', methods=['GET'])
def get_user_id(id):
    db = get_db()
    user = db.users.find_one({"_id": ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Creates a new user with the specified data.
@user_blueprint.route('/', methods=['POST'])
def create_user():
    db = get_db()
    data = request.json
    result = db.users.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201

# Updates the user with the specified ID with the new data.
@user_blueprint.route('/<id>', methods=['PUT'])
def update_user(id):
    db = get_db()
    data = request.json
    result = db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found"}), 404

# Deletes the user with the specified ID.
@user_blueprint.route('/<id>', methods=['DELETE'])
def delete_user(id):
    db = get_db()
    result = db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
