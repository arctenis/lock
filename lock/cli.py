import secrets
import typer
from typing_extensions import Annotated


app = typer.Typer()

def create_password(length: int) -> str:
    """Create a password of a given length"""
    return secrets.token_urlsafe(length)[:length]

@app.command()
def create(length: Annotated[int, typer.Option(help="Give password length")] = 16):
    # typer.echo(f"Creating a new password of length {length}")
    password = create_password(length)
    typer.echo(password)


if __name__ == "__main__":
    app()
