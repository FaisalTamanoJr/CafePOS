import authentication as auth
import menu
import orders
import maskpass
import sys
from os import system

"""
The app.py utilizes the other modules for different functions.
The features are separated to different modules so that the code is easier to manage
and so that it can be more modular.

app.py is also the main code. Therefore this is the python file we will run to start our program.
"""

# Dictionary of users and their passwords
users = {"Timothy": "Tiu",
         "Bienne": "Yu",
         "Faisal": "Tamano"
         }

# Menu Items
wake_menu = {
    # E = Espresso, IB = Ice Blended, T = Tea, NC = Non-Coffee
    'E01': {"Name": "Mocha", "Price": 3.00, "Stocks": 20},
    'E02': {"Name": "Latte", "Price": 4.00, "Stocks": 20},
    'E03': {"Name": "Cappuccino", "Price": 3.50, "Stocks": 20},
    'E04': {"Name": "Americano", "Price": 4.50, "Stocks": 20},
    'E05': {"Name": "Espresso", "Price": 4.25, "Stocks": 20},
    'E06': {"Name": "Macchiato", "Price": 4.00, "Stocks": 19},
    'E07': {"Name": "Vanilla", "Price": 3.75, "Stocks": 18},

    'IB01': {"Name": "Caramel", "Price": 4.25, "Stocks": 17},
    'IB02': {"Name": "Coffee Latte", "Price": 3.50, "Stocks": 20},
    'IB03': {"Name": "Frappe", "Price": 3.75, "Stocks": 20},
    'IB04': {"Name": "Mocha", "Price": 4.00, "Stocks": 20},
    'IB05': {"Name": "Mint", "Price": 5.00, "Stocks": 20},
    'IB06': {"Name": "Matcha Cream", "Price": 4.50, "Stocks": 20},

    'T01': {"Name": "Jasmine", "Price": 3.75, "Stocks": 20},
    'T02': {"Name": "Green", "Price": 4.50, "Stocks": 20},
    'T03': {"Name": "Earl Grey", "Price": 4.00, "Stocks": 20},
    'T04': {"Name": "English", "Price": 3.75, "Stocks": 20},

    'NC01': {"Name": "Chocolate Frappe", "Price": 4.75, "Stocks": 20},
    'NC02': {"Name": "Milk Brown Sugar", "Price": 4.00, "Stocks": 20},
    'NC03': {"Name": "Thai Milktea", "Price": 3.75, "Stocks": 20},
}

welcomeMessage = "Welcome to Wake Cup POS system! Please enter your customer login credentials."


def main():
    # Do not terminate the program unless requested by the user
    while True:
        system('clear')
        users_encrypted = {}

        # Encrypt the passwords in the dictionary
        for user in users:
            users_encrypted[user] = auth.cryptography(users[user], "encrypt")

        # Login system
        print(welcomeMessage)
        allowAccess = False
        while not allowAccess:
            system('clear')
            username = input("Username: ")
            password = maskpass.askpass(mask="*")
            allowAccess = auth.login(users_encrypted, username, password)

        while allowAccess:
            # Display the menu and the other options
            menu.display_menu(wake_menu)

            # Ask the users on what to do
            choices = [0, 1, 2]
            print("[0] Order an item, [1] Rank drinks, [2] Exit the program")
            choice = 3
            while choice not in choices:
                choice = input(f"choose an option:\n{choices}\n")
                if choice.isdecimal():
                    choice = int(choice)
            if choice == 0:
                system('clear')
                orders.action_on_orders()
            elif choice == 1:
                menu.display_popular_drinks(wake_menu)

                # Ask the users on what to do
                choices = [0, 1, 2]
                print("[0] Order an item, [1] Go back to Original Menu, [2] Exit the program")
                choice = 3
                while choice not in choices:
                    choice = input(f"choose an option:\n{choices}\n")
                    if choice.isdecimal():
                        choice = int(choice)
                if choice == 0:
                    system('clear')
                    orders.action_on_orders(wake_menu)
                elif choice == 1:
                    pass
                else:
                    sys.exit()
            else:
                sys.exit()


if __name__ == "__main__":
    main()
