import json
import pytest
from lock.storage import load_data_from_file, store_data_to_file

@pytest.fixture
def load_json_db():
    data = {"website": {"login": "password"},}
    with open("data.json", "w") as f:
        json.dump(data, f)
    return data

def test_load_data_from_file(load_json_db):
    assert load_data_from_file("data.json") == load_json_db

def test_store_data_to_file():
    data = {"login": "password"}
    store_data_to_file(data, "data.json")
    with open("data.json") as f:
        assert json.load(f) == data
