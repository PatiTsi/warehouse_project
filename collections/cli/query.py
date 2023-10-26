"""Command line interface to query the stock."""

from data import stock


# Function to list all items and count by warehouse


def list_all_items():
    total_warehouse1 = 0
    total_warehouse2 = 0

    for item in stock:
        print(
            f"{item['state']} {item['category']} (Warehouse {item['warehouse']}, {item['date_of_stock']} days)"
        )
        if item["warehouse"] == 1:
            total_warehouse1 += 1
        elif item["warehouse"] == 2:
            total_warehouse2 += 1

    print(f"Total items in Warehouse 1: {total_warehouse1}")
    print(f"Total items in Warehouse 2: {total_warehouse2}")


# Function to search for an item and place an order
def search_and_order():
    item_name = input("Enter the item name you want to search for: ").lower()

    # Search in both warehouses
    found_in_warehouse1 = [
        item
        for item in stock
        if item_name in f"{item['state']} {item['category']}" and item["warehouse"] == 1
    ]
    found_in_warehouse2 = [
        item
        for item in stock
        if item_name in f"{item['state']} {item['category']}" and item["warehouse"] == 2
    ]

    total_available = len(found_in_warehouse1) + len(found_in_warehouse2)

    if total_available == 0:
        print(f"{item_name} is Not in stock.")
        return

    print(f"Amount available: {total_available} item(s)")

    # Determine the location of the item
    location = []
    for item in found_in_warehouse1:
        location.append(f"Warehouse 1 (in stock for {item['date_of_stock']} days)")
    for item in found_in_warehouse2:
        location.append(f"Warehouse 2 (in stock for {item['date_of_stock']} days)")

    # print("Location:", ", ".join(location))
    print("Location:")
    for loc in location:
        print(f"- {loc}")

    # Check which warehouse has more of the item
    if found_in_warehouse1 and found_in_warehouse2:
        if found_in_warehouse1.count(item_name) > found_in_warehouse2.count(item_name):
            print("Maximum availability: Warehouse 1")
        else:
            print("Maximum availability: Warehouse 2")

    order_choice = input(
        "Do you want to place an order for this item? (yes/no): "
    ).lower()

    if order_choice == "yes":
        desired_amount = int(input(f"How many {item_name} do you want to order? "))
        if desired_amount <= total_available:
            print(f"Order placed: {desired_amount} {item_name}")
        else:
            max_available = min(len(found_in_warehouse1), len(found_in_warehouse2))
            print(
                f"Error: Only {max_available} {item_name} available. Do you want to order {max_available} instead? (yes/no)"
            )
            if input().lower() == "yes":
                print(f"Order placed: {max_available} {item_name}")


user_name = input("Please enter your name: ")  # Get the user name
print(f"Hello, {user_name}!")  # Greet the user

while True:
    print("\nMenu:")  # Show the menu and ask to pick a choice
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")

    choice = input("Please pick a choice using the numeric values (1/2/3): ")

    if choice == "1":  # If they pick 1
        list_all_items()
        print(f"Thank you for visiting, {user_name}!")
        break
    elif choice == "2":  # Else, if they pick 2
        search_and_order()
    elif choice == "3":
        print(f"Thank you for visiting, {user_name}!")  # Else, if they pick 3
        break
    else:
        print(
            "Error: Invalid operation. Please select 1, 2, or 3."
        )  # Thank the user for the visit