import json

def load_data_from_file(filename: str = "lock_db.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def store_data_to_file(data: dict, filename: str = "lock_db.json"):
    try: 
        with open(filename, "w") as f:
            json.dump(data, f)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

