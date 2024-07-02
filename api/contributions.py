from flask import Blueprint, request, jsonify
from models.contribution import Contribution
from db.session import get_db
from core.security import role_required, get_current_user
from services.contribution_services import (
    create_contribution_service,
    update_contribution_service,
    delete_contribution_service
)
from flask_jwt_extended import jwt_required

contributions_bp = Blueprint('contributions', __name__)

@contributions_bp.route('/', methods=['GET'])
@jwt_required()
@role_required(['admin', 'manager', 'contributor'])
def get_contributions():
    user = get_current_user()
    db = next(get_db())
    if user.role == 'admin':
        contributions = db.query(Contribution).all()
    elif user.role == 'manager':
        contributions = db.query(Contribution).filter_by(language=user.language).all()
    else:  
        contributions = db.query(Contribution).filter_by(user_id=user.id).all()
    return jsonify([contribution.to_dict() for contribution in contributions])

@contributions_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
@role_required(['admin', 'manager', 'contributor'])
def get_contribution(id):
    user = get_current_user()
    db = next(get_db())
    contribution = db.query(Contribution).filter_by(id=id).first()
    if not contribution:
        return jsonify({"message": "Contribution not found"}), 404

    if user.role == 'admin' or (user.role == 'manager' and contribution.language == user.language) or (user.role == 'contributor' and contribution.user_id == user.id):
        return jsonify(contribution.to_dict())
    else:
        return jsonify({"message": "Unauthorized"}), 403

@contributions_bp.route('/language/<string:language>', methods=['GET'])
@jwt_required()
@role_required(['admin', 'manager'])
def get_contributions_by_language(language):
    db = next(get_db())
    contributions = db.query(Contribution).filter_by(language=language).all()
    return jsonify([contribution.to_dict() for contribution in contributions])

@contributions_bp.route('/', methods=['POST'])
@jwt_required()
@role_required(['admin', 'manager', 'contributor'])
def create_contribution():
    data = request.get_json()
    user = get_current_user()
    try:
        new_contribution = create_contribution_service(user, data)
        return jsonify(new_contribution.to_dict()), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@contributions_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@role_required(['admin', 'manager', 'contributor'])
def update_contribution(id):
    data = request.get_json()
    user = get_current_user()
    try:
        updated_contribution = update_contribution_service(user, id, data)
        return jsonify(updated_contribution.to_dict())
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@contributions_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required(['admin', 'manager', 'contributor'])
def delete_contribution(id):
    user = get_current_user()
    try:
        delete_contribution_service(user, id)
        return jsonify({"message": "Contribution deleted"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400
