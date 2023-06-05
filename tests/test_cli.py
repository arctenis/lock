from typer.testing import CliRunner
from lock.cli import app


def test_create_password():
    runner = CliRunner()
    default_password_length = 16
    result = runner.invoke(app, [])
    # \n is added to the end of the password
    assert len(result.stdout) == default_password_length + 1

def test_create_password_with_length():
    runner = CliRunner()
    result = runner.invoke(app, ["--length", "8"])
    assert len(result.stdout) == 9
    
