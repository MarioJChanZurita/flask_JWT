import os
from flask import Flask
from .user import user_api
from .auth import token_api
from .extensions import mongo, bcrypt, jwt, NewJsonEncoder


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET')
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json"]
app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
app.json_encoder = NewJsonEncoder
app.register_blueprint(user_api)
app.register_blueprint(token_api)

mongo.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)



