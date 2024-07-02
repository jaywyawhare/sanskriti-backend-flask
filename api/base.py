from flask import Blueprint, request, jsonify, redirect
from models.user import User
from db.session import get_db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

base_bp = Blueprint('base', __name__)

@base_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, World!"})

@base_bp.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())

@base_bp.route('/admin', methods=['GET'])
def admin():   
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
