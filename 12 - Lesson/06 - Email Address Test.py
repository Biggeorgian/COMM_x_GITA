import pytest

symbols = ["@", "."]

def check_email_address(text: str, symbols: list) -> bool:
    return all(symbol in text for symbol in symbols)

def test_one():
    email = "someemail@mailserver.ge"
    assert check_email_address(email, symbols) is True

def test_two():
    email = "someemailmailserver.ge"
    assert check_email_address(email, symbols) is False

def test_three():
    email = "someemail@mailserverge"
    assert check_email_address(email, symbols) is False