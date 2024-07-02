from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user import User
from db.session import get_db

def role_required(role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if user.role != role:
                return jsonify({"message": "Unauthorized"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def get_current_user():
    user_id = get_jwt_identity()
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    return user
