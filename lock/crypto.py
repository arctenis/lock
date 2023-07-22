import base64
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from password import check_password_strength


def create_key(password:str):
    """Creates a key using the password"""
    check_password_strength(password)
    salt = os.urandom(16)
    kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            )
    bytes_password = bytes(password, "utf-8")
    key = kdf.derive(bytes_password)
    return key


def base64_encode(bytes_data:bytes) -> str:
    """Encodes bytes data to base64 string"""
    return base64.b64encode(bytes_data).decode("utf-8")

def validate_credentials(credentials:dict):
    keys = ["context", "username", "password"]
    for key in keys:
        if key not in credentials:
            raise KeyError(f"Missing key: {key}")
        if not isinstance(credentials[key], str):
            raise ValueError(f"Invalid value for key: {key}")
    return True


def encrypt(credentials:dict, password:str) -> dict:
    """Encrypts the credentials using the key"""

    key = create_key(password)
    print(f"Key: {key}")

    base64_key = base64_encode(key)
    print(f"Base64 key: {base64_key}")

    f = Fernet(base64_key)
    print(f"Fernet: {f}")

    validate_credentials(credentials)

    encrypted_credentials = {
            "context": f.encrypt(credentials["context"].encode()),
            "username": f.encrypt(credentials["username"].encode()),
            "password": f.encrypt(credentials["password"].encode())
            }
    return encrypted_credentials

def decrypt(credentials:dict, password:str) -> dict:
    """Decrypts the credentials using the key"""
    key = create_key(password)
    f = Fernet(key)
    validate_credentials(credentials)

    decrypted_credentials = {
            "context": f.decrypt(credentials["context"].decode()),
            "username": f.decrypt(credentials["username"].decode()),
            "password": f.decrypt(credentials["password"].decode())
            }
    return decrypted_credentials

password = "abcABC123@#$"
credentials = {
        "context": "context",
        "username": "username",
        "password": "password"
        }
encrypted_credentials = encrypt(credentials, password)
print(f"Encrypted credentials : {encrypted_credentials}")

