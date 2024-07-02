from models.contribution import Contribution
from db.session import get_db
from datetime import datetime

def create_contribution_service(user, data):
    db = next(get_db())
    contribution = Contribution(
        user_id=user.id,
        language=data['language'],
        question=data['question'],
        answer=data['answer'],
        created_at=datetime.utcnow()
    )
    db.add(contribution)
    db.commit()
    return contribution

def update_contribution_service(user, contribution_id, data):
    db = next(get_db())
    contribution = db.query(Contribution).filter_by(id=contribution_id).first()
    if not contribution or (user.role == 'contributor' and contribution.user_id != user.id):
        raise Exception("Contribution not found or unauthorized")
    contribution.language = data['language']
    contribution.question = data['question']
    contribution.answer = data['answer']
    db.commit()
    return contribution

def delete_contribution_service(user, contribution_id):
    db = next(get_db())
    contribution = db.query(Contribution).filter_by(id=contribution_id).first()
    if not contribution or (user.role == 'contributor' and contribution.user_id != user.id):
        raise Exception("Contribution not found or unauthorized")
    db.delete(contribution)
    db.commit()
