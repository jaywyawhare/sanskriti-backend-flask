from flask import Blueprint, request, jsonify, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from db.session import get_db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    db = next(get_db())
    if db.query(User).filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(email=email, password_hash=generate_password_hash(password))
    db.add(user)
    db.commit()
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    db = next(get_db())
    user = db.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})

@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    return jsonify({"message": "Successfully logged out"}), 200

