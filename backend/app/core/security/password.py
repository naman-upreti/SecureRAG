from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hasher.hash(password)

def verify_password(password:str,hashed_password:str)->bool:
    return password_hasher.verify(password,hashed_password)

"""
Password Security Utilities

This module provides helper functions for:

- Hashing plain-text passwords before storing them.
- Verifying user passwords during login.

Passwords are never stored in plain text.
Only password hashes are saved in the database.
"""
