from flask import Blueprint, jsonify, request
from .extensions import guard

api = Blueprint('api', __name__)

@api.route('/login')
def login():
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']

    user = guard.authenticate(username, password)

    return jsonify({'access_token': guard.encode_jwt_token(user)})

@api.route('/protected')
def protected():
    return None

@api.route('/open')
def open():
    return jsonify({'result': 'hello'})