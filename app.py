import authentication as auth
import menu
import orders

"""
The app.py utilizes the other modules for different functions.
The features are seperated to different modules so that the code is easier to manage
and so that it can be more modular.

app.py is also the main code. Therefore this is the python file we will run to start our program.
"""

# Dictionary of users and their passwords
users = {"username":"password"}

# Menu Items
wake_menu = {
    # E = Espresso, IB = Ice Blended, T = Tea, NC = Non-Coffee
    #'Drink Code': ("Name", "Price", Stocks)
    'E01': {"Name":"Mocha", "Price":3.00, "Stocks":20},
    'E02': {"Name":"Latte", "Price":4.00, "Stocks":20},
    'E03': {"Name":"Cappuccino", "Price":3.50, "Stocks":20},
    'E04': {"Name":"Americano", "Price":4.50, "Stocks":20},
    'E05': {"Name":"Espresso", "Price":4.25, "Stocks":20},
    'E06': {"Name":"Macchiato", "Price":4.00, "Stocks":20},
    'E07': {"Name":"Vanilla", "Price":3.75, "Stocks":20},

    'IB01': {"Name":"Caramel", "Price":4.25, "Stocks":20},
    'IB02': {"Name":"Coffee Latte", "Price":3.50, "Stocks":20},
    'IB03': {"Name":"Frappe", "Price":3.75, "Stocks":20},
    'IB04': {"Name":"Mocha", "Price":4.00, "Stocks":20},
    'IB05': {"Name":"Mint", "Price":5.00, "Stocks":20},
    'IB06': {"Name":"Matcha Cream", "Price":4.50, "Stocks":20},

    'T01': {"Name":"Jasmine", "Price":3.75, "Stocks":20},
    'T02': {"Name":"Green", "Price":4.50, "Stocks":20},
    'T03': {"Name":"Earl Grey", "Price":4.00, "Stocks":20},
    'T04': {"Name":"English", "Price":3.75, "Stocks":20},

    'NC01': {"Name":"Chocolate Frappe", "Price":4.75, "Stocks":20},
    'NC02': {"Name":"Milk Brown Sugar", "Price":4.00, "Stocks":20},
    'NC03': {"Name":"Thai Milktea", "Price":3.75, "Stocks":20},
}

def main():
    users_encrypted = {}

    # Encrypt the passwords in the dictionary
    for user in users:
        users_encrypted[user] = auth.cryptography(users[user], "encrypt")

    menu.display_menu(wake_menu)


if __name__ == "__main__":
    main()
