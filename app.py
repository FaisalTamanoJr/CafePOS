import authentication
import menu
import orders

"""
The app.py utilizes the other modules for different functions.
The features are seperated to different modules so that the code is easier to manage
and so that it can be more modular.

app.py is also the main code. Therefore this is the python file we will run to start our program.
"""

# Dictionary of users and their passwords
users = {'''username:password'''}

def main():
    users_encrypted = {}

    # Encrypt the usernames and passwords in the dictionary
    for user in users:
        users_encrypted[encrypt(user)] = encrypt(password)

    login()
    display_menu()


if __name__ == "__main__":
    main()
