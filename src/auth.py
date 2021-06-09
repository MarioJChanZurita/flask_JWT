from .extensions import mongo, bcrypt
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import requests as req


token_api = Blueprint('jwt_token', __name__)


@token_api.route('/<username>/token', methods=['POST'])
def create_token(username):
    # receive data
    user_request = fetch_data(username)  # instead of an api, frontend
    # check the database
    user_data = mongo.db['users'].find_one({'username': user_request['username']})
    if not user_data or bcrypt.check_password_hash(user_data['password'], user_request['password']):
        return make_response({'message': 'User Not Found'}, 404)
    # create the token if exits
    access_token = create_access_token(identity=user_request)
    return jsonify(access_token=access_token)


@token_api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


def fetch_data(username):
    response = req.get('http://127.0.0.1:5000/getUser/' + username)
    if response.status_code != 200:
        raise Exception('GET /tasks/ {}'.format(response.status_code))
    return response.json()




