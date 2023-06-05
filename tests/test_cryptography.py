from lock.cryptography import *


def test_create_password():
    password = create_password(8)
    assert len(password) == 8

def test_check_weak_password_strength():
    password = "12345678"
    assert check_password_strength(password) == False

def test_generate_passphrase():
    passphrase = generate_passphrase(4)
    print(f"Passphrase : {passphrase}")
    assert len(passphrase.split()) == 4
