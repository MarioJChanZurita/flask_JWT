from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import json
from bson import ObjectId


mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()


class NewJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return o
