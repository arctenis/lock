from cryptography.fernet import Fernet


def encrypt(credentials:dict, key:str):
    """Encrypts the credentials using the key"""
    f = Fernet(key)
    encrypted_credentials = {
            "context": f.encrypt(credentials["context"]),
            "username": f.encrypt(credentials["username"]),
            "password": f.encrypt(credentials["password"])
            }
    return encrypted_credentials

def decrypt(credentials:dict, key:str):
    """Decrypts the credentials using the key"""
    f = Fernet(key)
    decrypted_credentials = {
            "context": f.decrypt(credentials["context"]),
            "username": f.decrypt(credentials["username"]),
            "password": f.decrypt(credentials["password"])
            }
    return decrypted_credentials

