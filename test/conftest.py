import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.auth import auth_bp
from api.contributions import contributions_bp
from api.users import users_bp
from models.user import User
from models.contribution import Contribution
from db.base_class import Base
from db.session import get_db, SessionLocal


SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.config["TESTING"] = True

    jwt = JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(contributions_bp, url_prefix="/contributions")
    app.register_blueprint(users_bp, url_prefix="/users")

    Base.metadata.create_all(bind=engine)

    yield app

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(app, db_session):
    return app.test_client()


@pytest.fixture(scope="function")
def init_db(db_session):
    admin = User(email="admin@example.com", password_hash="admin", role="admin")
    manager = User(
        email="manager@example.com",
        password_hash="manager",
        role="manager",
        language="Python",
    )
    contributor = User(
        email="contributor@example.com", password_hash="contributor", role="contributor"
    )

    db_session.add(admin)
    db_session.add(manager)
    db_session.add(contributor)
    db_session.commit()

    return db_session
