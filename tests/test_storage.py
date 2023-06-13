import json
import pytest
from lock.storage import *

@pytest.fixture
def load_json_db():
    data = {"website0": {"login0": "password0"},
            "website1": {"login1": "password1"},
            "website2": {"login2": "password2"},}
    with open("data.json", "w") as f:
        json.dump(data, f)
    return data

def test_load_data_from_file(load_json_db):
    assert load_data_from_file("data.json") == load_json_db

def test_store_data_to_file():
    data = {"website3": {"login3": "password3"}}
    store_credentials_to_file(data, "data.json")
    with open("data.json") as f:
        assert json.load(f) == data
