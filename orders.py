import sys
from os import system


def action_on_orders(username, menu):
    choices = [0, 1, 2]
    print("[0] Go Back, [1] Take an Order, [2] Exit the program")
    choice = None
    while choice not in choices:
        choice = input(f"choose an option:\n{choices}\n")
        if choice.isdecimal():
            choice = int(choice)
    if choice == 0:
        pass
    elif choice == 1:
        system('clear')
        order = take_an_order(menu)
        if order is None:
            pass
        else:
            receipt_code = receipt(username, menu, order)
            if receipt_code == 1:
                return 1
            elif receipt_code == 0:
                return 0
    else:
        sys.exit()


def take_an_order(menu):

    order = {}

    while True:
        item_code = input("Enter item code: ")
        if item_code not in menu:
            print("Invalid item code. Please try again.")
        else:
            item = menu[item_code]
            quantity = int(input(f"Enter quantity for '{item['Name']}': "))
            if quantity > item['Stocks']:
                print(f"Insufficient stocks for '{item['Name']}'")
            else:
                order[item_code] = {"Name": item['Name'], "Price": item['Price'], "Quantity": quantity}
                item['Stocks'] -= quantity
                print(f"Added '{item['Name']}' x {quantity} to order.")

                choices = [0, 1, 2]
                print("[0] Add More Items, [1] Stop Ordering, [2] Cancel and Remove All Orders")
                choice = None
                while choice not in choices:
                    choice = input(f"choose an option:\n{choices}\n")
                    if choice.isdecimal():
                        choice = int(choice)
                if choice == 0:
                    pass
                elif choice == 1:
                    system('clear')
                    return order
                else:
                    system('clear')

                    # Add back the removed stocks
                    for item_code in order:
                        menu[item_code]["Stocks"] += order[item_code]["Quantity"]

                    order = None
                    return order


def receipt(username, menu, order):
    system('clear')
    total_cost = 0
    print("*************** RECEIPT ***************")
    print("*************** from Wake Cup! ***************")
    for item_code in order:
        item = menu[item_code]
        quantity = order[item_code]["Quantity"]
        item_cost = quantity * item['Price']
        total_cost += item_cost
        print(f"{item['Name']} x {quantity}: Php{item_cost:.2f}")
    print(f"\nTotal cost: ${total_cost:.2f}")

    # Ask for a discount
    choices = [0, 1]
    print("Do you want a 15% discount?\n[0] Yes, [1] No")
    choice = None
    while choice not in choices:
        choice = input(f"choose an option:\n{choices}\n")
        if choice.isdecimal():
            choice = int(choice)
    if choice == 0:
        discounted_cost = total_cost - (0.15 * total_cost)
        print(f"\nDiscounted cost: ${discounted_cost:.2f}")
    else:
        pass

    # Thank and ask the customer if they want to go back to the main menu, logout, or exit the program.
    choices = [0, 1, 2]
    print(f"Thank you for using the Wake Cup POS system, {username}. Would you like to\n"
          f"[0] Go back to the main menu, [1] Log out, [2] Exit the program")
    choice = None
    while choice not in choices:
        choice = input(f"choose an option:\n{choices}\n")
        if choice.isdecimal():
            choice = int(choice)
    if choice == 0:
        return 0
    elif choice == 1:
        return 1
    else:
        sys.exit()
