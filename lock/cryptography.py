import secrets
import string


def create_password(length: int) -> str:
    """Create a password of a given length"""
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
            print(f"Passphrase : {passphrase}")
    except FileNotFoundError:
        raise FileNotFoundError("Words dictionary not found")
    return passphrase




