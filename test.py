import authentication as auth

# This file is just used for testing functions. It will be deleted after the project is done.

username = "Username"
password = "Password"

username_encrypted = auth.cryptography(username, "decrypt")

print(username_encrypted)
