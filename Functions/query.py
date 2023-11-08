from data import stock, personnel
from datetime import datetime
from collections import defaultdict


# Get/Return the user name.
def get_user_name():
    username = input("Please enter the username: ")
    return username.capitalize()


# Greet the user
def greet_user(username):
    print(f"Hello {username}, Welcome to the Re_conNect website")


# Show the menu and ask to pick a choice
def select_operation():
    # print()
    print("What would you like to do?")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Browse by category")
    print("4. Quit")
    print("-" * 120)
    menu_option = input("Please pick a choice using the numeric values (1/2/3/4): ")

    # If user pick option 1
    if menu_option == "1":
        item_list_by_wearhouse()
    # If user pick option 2
    elif menu_option == "2":
        search_and_order_item()

    # If user pick option  3
    elif menu_option == "3":
        browse_by_category()

    # If user pick option  4
    elif menu_option == "4":
        pass

    else:
        print("*" * 100)
        print("Invalid input, please enter a number between 1 and 4 for a valid option")
        print("*" * 100)


# List of items by warehouse.
def item_list_by_wearhouse():
    d = defaultdict(list)
    for i in stock:
        item_name = i["state"] + " " + i["category"]
        d[i["warehouse"]].append(item_name)
    for i in dict(d).keys():
        print(f"Items in warehouse {i}: \n{dict(d)[i]} \n")
        print(f"Total items in Warehouse {i} are {len(dict(d)[i])}")
        print("." * 120)
    items_sum = 0
    for value in dict(d).values():
        items_sum += len(value)
    other_warehouse = len(dict(d).keys())
    actions.append(f"listed {items_sum} items from {other_warehouse} Warehouses")
    # actions.append("Hi")
    continue_session = input(
        f"Do you want to continue with another operation? (yes/no)"
    )
    if continue_session == "yes":
        select_operation()
