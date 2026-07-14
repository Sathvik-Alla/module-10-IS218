import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import os

from app.database import Base
from app.models import User
from app.security import hash_password, verify_password

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/module10_test_db",
)


@pytest.fixture(scope="module")
def engine():
    return create_engine(TEST_DATABASE_URL)


@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine, tables):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.query(User).delete()
    session.commit()
    session.close()


def test_create_user(db_session):
    user = User(
        username="alice",
        email="alice@example.com",
        password_hash=hash_password("alicepass123"),
    )
    db_session.add(user)
    db_session.commit()

    fetched = db_session.query(User).filter_by(username="alice").first()
    assert fetched is not None
    assert fetched.email == "alice@example.com"
    assert verify_password("alicepass123", fetched.password_hash)


def test_duplicate_username_rejected(db_session):
    user1 = User(username="bob", email="bob1@example.com", password_hash=hash_password("pass1234"))
    db_session.add(user1)
    db_session.commit()

    user2 = User(username="bob", email="bob2@example.com", password_hash=hash_password("pass5678"))
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_duplicate_email_rejected(db_session):
    user1 = User(username="carol1", email="carol@example.com", password_hash=hash_password("pass1234"))
    db_session.add(user1)
    db_session.commit()

    user2 = User(username="carol2", email="carol@example.com", password_hash=hash_password("pass5678"))
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()