from sqlalchemy import Column, Integer, String
from db.base_class import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default='contributor', nullable=False)
    language = Column(String, nullable=True)  # Only for managers

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'role': self.role,
            'language': self.language
        }
