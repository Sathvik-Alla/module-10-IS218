from app.security import hash_password, verify_password


def test_hash_password_returns_different_string():
    plain = "SuperSecret123"
    hashed = hash_password(plain)

    assert hashed != plain


def test_verify_password_success():
    plain = "SuperSecret123"
    hashed = hash_password(plain)

    assert verify_password(plain, hashed) is True


def test_verify_password_failure():
    hashed = hash_password("SuperSecret123")

    assert verify_password("WrongPassword", hashed) is False


def test_same_password_hashes_differently_each_time():
    first_hash = hash_password("SamePassword1")
    second_hash = hash_password("SamePassword1")

    assert first_hash != second_hash