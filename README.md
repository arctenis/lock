# Lock

**Lock** is a CLI password manager written in Python. It uses the
[Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption scheme
to encrypt passwords and store them in a local SQLite database.

## Features

- Create, read, update, and delete passwords with context (URLs for example)
- Generate random passwords and passphrases
- Copy passwords to the clipboard
- Check password strength

## Dependencies

- [Typer](https://typer.tiangolo.com/)
- cryptography (for Fernet encryption)
- pyperclip (for copying passwords to the clipboard)
- 
