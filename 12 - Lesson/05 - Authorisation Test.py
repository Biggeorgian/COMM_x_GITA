import pytest

users_database = {
    "giorgi": "pass123",
    "mariam": "secretWord!",
    "sandro": "qwerty"
}

def validate_login(username: str, password: str,
                   user_database: dict) -> bool:
    if username in user_database:
        if user_database[username] == password:
            return True
        else:
            return False
    else:
        raise ValueError(f"მომხმარებელი '{username}' არ მოიძებნა.")

def test_authorisation():
    assert validate_login("giorgi", "pass123", users_database) is True

def test_authorisation_error():
    assert validate_login("mariam", "pass123", users_database) is False

def test_unknown_user():
    with pytest.raises(ValueError) as excinfo:
        validate_login("luiza", "any_password", users_database)
    assert "მომხმარებელი 'luiza' არ მოიძებნა" in str(excinfo.value)