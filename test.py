import authentication as auth


username = "abc"
password = "cringe"

username_encrypted = auth.encrypt(username)
password_encrypted = auth.encrypt(username)

print(username_encrypted)

#bienne trial
