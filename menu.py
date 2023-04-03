from tabulate import tabulate
import orders

"""
    1. The display menu utilizes dictionaries to display the items available in the restaurant and their information
    note: more info in the diagrams at the docs
"""
def display_menu(menu):
    table = [["Item Code", "Item Name", "Price", "Stocks Available"]]

    for items in menu:
        temp_list = [items, menu[items]["Name"], str(menu[items]["Price"]) + " PHP", menu[items]["Stocks"]]
        table.append(temp_list)

    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

"""
    1. Sorts the information in the menu dictionary based on the number of times the item is bought.
    note: more info in the diagrams at the docs
"""
def display_popular_drinks():
    pass
