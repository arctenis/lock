import pytest
from typer.testing import CliRunner
from lock.cli import app


def test_check_strong_password_strength():
    password = "azerAZER1234@"
    assert check_password_strength(password) == True

def test_create_command():
    runner = CliRunner()
    default_password_length = 16
    result = runner.invoke(app, ["create"])
    # \n is added to the end of the password
    assert len(result.stdout) == default_password_length + 1

def test_create_command_with_length():
    runner = CliRunner()
    result = runner.invoke(app, ["create", "--length", "8"])
    assert len(result.stdout) == 9

def test_store_password():
    runner = CliRunner()
    result = runner.invoke(app, ["store", "login", "password"])
    assert result.stdout == "login password\n"
    
