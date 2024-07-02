from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from models.user import User
from db.session import get_db
from core.security import role_required, get_current_user
from flask_jwt_extended import jwt_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_users():
    db = next(get_db())
    users = db.query(User).all()
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_user(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user.to_dict())

@users_bp.route('/', methods=['POST'])
@jwt_required()
@role_required('admin')
def create_user():
    data = request.get_json()
    db = next(get_db())
    if db.query(User).filter_by(email=data['email']).first():
        return jsonify({"message": "User already exists"}), 400
    user = User(email=data['email'], password_hash=generate_password_hash(data['password']), role=data.get('role', 'contributor'))
    db.add(user)
    db.commit()
    return jsonify(user.to_dict()), 201

@users_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@role_required('admin')
def update_user(id):
    data = request.get_json()
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.email = data['email']
    user.password_hash = generate_password_hash(data['password'])
    user.role = data.get('role', user.role)
    db.commit()
    return jsonify(user.to_dict())

@users_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_user(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.delete(user)
    db.commit()
    return jsonify({"message": "User deleted"})
