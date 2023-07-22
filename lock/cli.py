import typer
from typing_extensions import Annotated

from password import create_password, create_passphrase
from storage import store_password


app = typer.Typer()


@app.command()
def create(length: Annotated[int, typer.Option(help="Give password or passphrase length")]=16,
           passphrase: Annotated[bool, typer.Option(help="Generate a passphrase")]=False):
    """
    Create a secure password with a given length (16 by default).
    If passphrase is set, generate a passphrase instead of a password.
    """
    if passphrase:
        result = create_passphrase(length)
    else:
        result = create_password(length)
    typer.echo(result)


@app.command()
def store(login: Annotated[str, typer.Argument(..., help="Login name")],
          password: Annotated[str, typer.Argument(..., help="Password")],
          context: Annotated[str, typer.Option(help="Context name")] = ""):
    """
    Store a password for a given context. Context is empty by default.
    Login and password are required arguments.
    """
    typer.echo(f"Login: {login}\nPassword: {password}")
    try:
        store_password(login, password)
    except Exception as e:
        typer.echo(f"Error storing password : {e}")


if __name__ == "__main__":
    app()
