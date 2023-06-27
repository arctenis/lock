import typer
from typing_extensions import Annotated

from cryptography import create_password
from storage import store_password


app = typer.Typer()

@app.command()
def create(length: Annotated[int, typer.Option(help="Give password length")] = 16):
    # typer.echo(f"Creating a new password of length {length}")
    password = create_password(length)
    typer.echo(password)

@app.command()
def store(login: Annotated[str, typer.Argument(..., help="Login name")],
          password: Annotated[str, typer.Argument(..., help="Password")]):
    typer.echo(f"Login: {login}\nPassword: {password}")
    store_password(login, password)


if __name__ == "__main__":
    app()
