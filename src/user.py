from .extensions import mongo, bcrypt
from flask import Blueprint, request, make_response, jsonify


user_api = Blueprint('user', __name__)


@user_api.route('/createUser', methods=['POST'])
def create_user():
    user = request.get_json()
    plain_text_password = user['password']
    user['password'] = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    mongo.db["users"].insert_one(user)
    return make_response({"message": "success"}, 200)


@user_api.route('/getUsers', methods=['GET'])
def get_users():
    return jsonify(list(mongo.db["users"].find()))


@user_api.route('/getUser/<username>', methods=['GET'])
def get_user(username):
    return jsonify(mongo.db["users"].find_one({'username': username}))
