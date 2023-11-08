"""Command line interface to query the stock."""

from data import stock
from datetime import datetime

# If they pick 1, list all items and count by warehouse


def list_all_items(stock):
    total_warehouse1 = []
    total_warehouse2 = []

    for i in stock:
        item_name = i["state"] + " " + i["category"]
        if i["warehouse"] == 1:
            total_warehouse1.append(item_name)

        elif i["warehouse"] == 2:
            total_warehouse2.append(item_name)

    print(f"Items in warehouse 1: ")

    for id, items in enumerate(total_warehouse1, start=1):
        print(id, ".", items)

    print("*" * 40)
    print(f"Total items in Warehouse 1 is {len(total_warehouse1)}")
    print("*" * 40)
    print(f"Items in warehouse 2: ")
    for id, items in enumerate(total_warehouse2, start=1):
        print(id, ".", items)

    print(f"Total items in Warehouse 2 is {len(total_warehouse2)}")
    print("*" * 40)
    print(f"Thank you for visiting, {user_name}!")


# If they pic 2, search for an item and place an order


def search_and_order():
    item_name = input("Enter the item name you want to search for: ").lower()
    search_item_state = " ".join(item_name.split(" ")[:-1]).capitalize()
    print("state : ", search_item_state)
    search_item_category = item_name.split()[-1].capitalize()
    print("category:", search_item_category)

    location = []
    found_in_warehouse1 = 0
    found_in_warehouse2 = 0
    for item in stock:
        if (
            item["state"] == search_item_state
            and item["category"] == search_item_category
        ):
            date_str = item["date_of_stock"]
            date_format = "%Y-%m-%d %H:%M:%S"
            days = (datetime.now() - datetime.strptime(date_str, date_format)).days
            location.append(
                "Warehouse" + str(item["warehouse"]) + f" (in stock for {days} days)"
            )
            if item["warehouse"] == 1:
                found_in_warehouse1 += 1
            else:
                found_in_warehouse2 += 1

    total_available = found_in_warehouse1 + found_in_warehouse2

    if total_available == 0:
        print(f"{item_name} is Not in stock.")
        return

    print(f"Amount available: {total_available} item(s)")
    print("Location:")
    for loc in location:
        print(f"- {loc}")

    if found_in_warehouse1 and found_in_warehouse2:
        if found_in_warehouse1 > found_in_warehouse2:
            print("Maximum availability: Warehouse 1")
        else:
            print("Maximum availability: Warehouse 2")

    order_choice = input("Would you like to order this item? (yes/no) ").lower()

    if order_choice == "yes":
        desired_amount = int(input(f"How many {item_name} do you want to order? "))
        max_available = min(found_in_warehouse1, found_in_warehouse2)
        if desired_amount <= max_available:
            print(f"Order placed: {desired_amount} {item_name}")
        else:
            print(
                f"I am sorry only {total_available} {item_name} is available. Do you want to order {total_available} instead? (yes/no)"
            )
            if input().lower() == "yes":
                print(f"Order placed: {total_available} {item_name}")
                print(f"Thank you for visiting, {user_name}!")


def category_menu():
    category_mapping = []
    for item in stock:
        category_mapping.append(item["category"])
    dict_item_category_count = {i: category_mapping.count(i) for i in category_mapping}

    dict_id_category = {}
    for id, (key, value) in enumerate(dict_item_category_count.items()):
        dict_id_category[id + 1] = key
        print(f"{id+1} {key} ({value})")
    print()
    select_category = input("Type the category number to browse:")
    print(f"dict_item_category_count : {dict_item_category_count}")
    print(f"dict_id_category,{dict_id_category}")
    print()

    category_name = None
    for key_id, value_id in dict_id_category.items():
        if key_id == int(select_category):
            category_name = value_id
            count_items_by_category = 0
            for item in stock:
                if value_id == item["category"]:
                    count_items_by_category += 1
                    print(
                        f"{item['state']} {item['category']}, Warehouse {item['warehouse']}"
                    )
    print("." * 120)
    print(f"Total items in this category are: {count_items_by_category}")
    print("." * 120)
    print(f"Thank you for visiting, {user_name}!")


# Get the user name
user_name = input("Please enter your username: ")
# Greet the user
print(f"Hello, {user_name}! Welcome to our wedsite.")

while True:
    print("Menu:")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Browse by category")
    print("4. Quit")

    choice = input("Please pick a choice using the numeric values (1/2/3/4): ")

    if choice == "1":
        if "stock" in locals():
            list_all_items(stock)
        else:
            print("Error: Stock not defined.")
    elif choice == "2":
        search_and_order()
    elif choice == "3":
        category_menu()

    else:
        print("Error: Invalid category code")
    if choice == "4":
        print(f"Thank you for visiting, {user_name}!")
    break
