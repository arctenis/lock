import secrets


def create_password(length: int) -> str:
    """Create a password of a given length"""
    return secrets.token_urlsafe(length)[:length]


def check_password_strength(password: str) -> bool:
    valid_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)
    return all([valid_length, has_digit, has_upper, has_lower, has_special])



