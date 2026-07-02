from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()

print(password_hasher.hash("hello123"))

