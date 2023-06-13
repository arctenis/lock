import secrets
import string


def create_password(length: int) -> str:
    """Create a password with at least 1 digit, 1 uppercase letter, 1 lowercase
    letter, and 1 special character and has a minimum length of 8 characters.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")

    symbols = "!@#$%^&*()_+-=[]{};:,./<>?"
    characters = string.ascii_letters + string.digits + symbols

    while True:
        password = "".join(secrets.choice(characters) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and any(c in symbols for c in password)):
            break

    return password


def check_password_strength(password: str) -> bool:
    """
    Check if a password has a minimum length of 8 characters,
    at least 1 digit, 1 uppercase letter, 1 lowercase letter,
    and 1 special character.
    """
    valid_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)
    return all([valid_length, has_digit, has_upper, has_lower, has_special])

def generate_passphrase(length: int) -> str:
    """Generate a passphrase of a given length"""
    try:
        with open("words.txt") as f:
            words = [word.strip() for word in f]
            passphrase = " ".join(secrets.choice(words) for i in range(length))
    except FileNotFoundError:
        raise FileNotFoundError("Words dictionary not found")
    return passphrase


def check_passphrase_strength(passphrase):
    """
    Check if passphrase has words of 4 letters minimum and has at least 4
    words.
    """
    words = passphrase.split()
    valid_length = all(len(word) >= 4 for word in words)
    valid_words = len(words) >= 4
    return all([valid_length, valid_words])
