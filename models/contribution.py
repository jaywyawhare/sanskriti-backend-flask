from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.base_class import Base

class Contribution(Base):
    __tablename__ = 'contributions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    language = Column(String, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'language': self.language,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at
        }
