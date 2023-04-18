import menu

    # check the diagrams in the docs for an explanation on how this function works.

def action_on_orders():
    print("action on orders function")
    pass
    order = {}  # initialize an empty order dictionary
    menu.display_menu(menu.wake_menu)
    while True:
        item_code = input("Enter item code (or 'done' to finish): ")
        if item_code == "done":
            break
        elif item_code not in menu.wake_menu:
            print("Invalid item code. Please try again.")
            continue
        item = menu.wake_menu[item_code]
        quantity = int(input(f"Enter quantity for '{item['Name']}': "))
        if quantity > item['Stocks']:
            print(f"Insufficient stocks for '{item['Name']}'")
            continue
        order[item_code] = {"Name": item['Name'], "Price": item['Price'], "Quantity": quantity}
        item['Stocks'] -= quantity
        print(f"Added '{item['Name']}' x {quantity} to order.")
    return order


    # check the diagrams in the docs for an explanation on how this function works.
def receipt():


def receipt(order):
    total_cost = 0
    print("\n*************** RECEIPT ***************\n")
    print("\n*************** from Wake Cup! ***************\n")
    for item_code, quantity in order.items():
        item = menu.items[item_code]
        item_cost = quantity * item['Price']
        total_cost += item_cost
        print(f"{item['Name']} x {quantity}: Php{item_cost:.2f}")
    print(f"\nTotal cost: ${total_cost:.2f}")
    print("\nThank you for your order. Come again!\n")
    pass

