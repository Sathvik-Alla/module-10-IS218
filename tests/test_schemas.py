import pytest
from pydantic import ValidationError
from app.schemas import UserCreate


def test_user_create_valid():
    user = UserCreate(username="sathvik", email="sathvik@example.com", password="password123")
    assert user.username == "sathvik"
    assert user.email == "sathvik@example.com"


def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="sathvik", email="not-an-email", password="password123")


def test_user_create_password_too_short():
    with pytest.raises(ValidationError):
        UserCreate(username="sathvik", email="sathvik@example.com", password="short")


def test_user_create_username_too_short():
    with pytest.raises(ValidationError):
        UserCreate(username="ab", email="sathvik@example.com", password="password123")