import authentication
import menu
import orders

# Dictionary of users
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
