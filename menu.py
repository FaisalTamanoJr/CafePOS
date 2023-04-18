from tabulate import tabulate

"""
    1. The display menu utilizes dictionaries to display the items available in the restaurant and their information
    note: more info in the diagrams at the docs
"""


def display_menu(menu):
    table = [["Item Code", "Item Name", "Price", "Stocks"]]

    for items in menu:
        temp_list = [items, menu[items]["Name"], "{0:.2f}".format(menu[items]["Price"]) + " PHP", menu[items]["Stocks"]]
        table.append(temp_list)

    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


"""
    1. Sorts the information in the menu dictionary based on the number of times the item is bought.
    note: more info in the diagrams at the docs
"""


def display_popular_drinks(menu):
    # sort the items based on the stocks
    sorted_menu = sorted(menu.items(), key=lambda x: x[1]['Stocks'])

    table = [["Popularity Rank", "Item Code", "Item Name", "Price", "Stocks"]]
    for i, j in zip(sorted_menu, range(1, len(sorted_menu))):
        items = i[0]
        items_info = i[1]
        temp_list = [j, items, items_info["Name"], "{0:.2f}".format(items_info["Price"]) + " PHP", items_info["Stocks"]]
        table.append(temp_list)
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
