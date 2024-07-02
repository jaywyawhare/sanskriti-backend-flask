import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from api.auth import auth_bp
from api.base import base_bp
from api.contributions import contributions_bp
from api.users import users_bp
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": os.getenv('CORS_ORIGINS').split(',')}})

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(contributions_bp, url_prefix='/contributions')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(base_bp, url_prefix='/')

logging.basicConfig(level=logging.INFO)  
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

if __name__ == '__main__':
    app.run(debug=False)
