from lock.cryptography import *
import pytest
import string



def test_create_password():
    password = create_password(8)
    lowercase = string.ascii_lowercase
    assert len(password) == 8
    assert any(char in lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)

@pytest.mark.parametrize("password", ["12345678", "abcdefgh", "ABCDEFGH", "abc12345", "ABC12345", "abcABC12"])
def test_check_weak_password_strength(password):
    assert check_password_strength(password) == False

def test_check_strong_password_strength():
    password = "abcABC12!"
    assert check_password_strength(password) == True

def test_generate_passphrase():
    passphrase = generate_passphrase(4)
    assert len(passphrase.split()) == 4
    for word in passphrase.split():
        assert len(word) >= 4


@pytest.mark.parametrize("passphrase", 
                         ["a b c d",
                          "abcde fghij klmno",
                          "a b cdefg hijklm",
                          ])
def test_check_weak_passphrase_strength(passphrase):
    assert check_passphrase_strength(passphrase) == False

def test_check_strong_passphrase_strength():
    passphrase = "horse battery staple correct"
    assert check_passphrase_strength(passphrase) == True
