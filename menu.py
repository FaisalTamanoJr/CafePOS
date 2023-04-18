from tabulate import tabulate

"""
    1. The display menu utilizes dictionaries to display the items available in the restaurant and their information
    note: more info in the diagrams at the docs
"""


def display_menu(menu):
    available = [["Item Code", "Item Name", "Price", "Stocks"]]
    unavailable = [["Item Code", "Item Name", "Price", "Stocks"]]

    for items in menu:
        temp_list = [items, menu[items]["Name"], "{0:.2f}".format(menu[items]["Price"]) + " PHP", menu[items]["Stocks"]]
        if menu[items]["Stocks"] > 0:
            available.append(temp_list)
        else:
            unavailable.append(temp_list)

    print("Available Items")
    print(tabulate(available, headers="firstrow", tablefmt="fancy_grid"))
    print("Unavailable Items")
    print(tabulate(unavailable, headers="firstrow", tablefmt="fancy_grid"))


"""
    1. Sorts the information in the menu dictionary based on the number of times the item is bought.
    note: more info in the diagrams at the docs
"""


def display_popular_drinks(menu):
    # sort the items based on the stocks
    sorted_menu = sorted(menu.items(), key=lambda x: x[1]['Stocks'])

    table = [["Popularity Rank", "Item Name"]]
    for i, j in zip(sorted_menu, range(1, len(sorted_menu))):
        items_info = i[1]
        temp_list = [j, items_info["Name"]]
        table.append(temp_list)
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
