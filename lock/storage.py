import json


def load_data_from_file(filename: str = "lock_db.json"):
    try:
        with open(filename, "w") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Database not found")
    return data

def store_credentials_to_file(credentials: dict, filename: str = "lock_db.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[credentials["context"]] = {credentials["login"]: credentials["password"]}
    
    try: 
        with open(filename, "w") as f:
            json.dump(data, f)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

def store_password(login: str, 
                   password: str, 
                   context: str = "",
                   filename: str = "lock_db.json"):
    data = load_data_from_file(filename)
    data[context] = {login: password}
    store_credentials_to_file(data)
