"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instraction here.
    # The 'item' name will contain each of the strings(iten names) in the list.
    """

from data import warehouse1, warehouse2


# If they pick the 1 choice: list items by warehouse
#
def list_items():
    print("*" * 25)
    print("Items in Warehouse 1:")
    print("*" * 25)

    for item in warehouse1:
        print(f"- {item}")

    print("*" * 25)
    print("Items in Warehouse 2:")
    print("*" * 25)

    for item in warehouse2:
        print(f"- {item}")


# If they pick the 2 choice: search for an item and place an order
def search_and_order():
    item_name = input("Enter the item name you want to search for: ")

    # Search in both warehouses
    found_in_warehouse1 = item_name in warehouse1
    found_in_warehouse2 = item_name in warehouse2

    total_available = found_in_warehouse1 + found_in_warehouse2

    if total_available == 0:
        print(f"{item_name} is Not in stock.")
        return

    print(f"Total availability of the item: {item_name} is {total_available} item(s)")

    # Determine the location of the item
    location = []
    if found_in_warehouse1:
        location.append("Warehouse 1")
    if found_in_warehouse2:
        location.append("Warehouse 2")

    print("Location:", ", ".join(location))

    # Check which warehouse has more of the items
    if found_in_warehouse1 and found_in_warehouse2:
        if warehouse1.count(item_name) > warehouse2.count(item_name):
            print("Maximum quantity Location Warehouse 1")
        else:
            print("Maximum quantity Location Warehouse 2")

    order_choice = input(
        f"Do you want to place an order for the item {item_name} ? (yes/no): "
    ).lower()

    if order_choice == "yes":
        desired_amount = int(input(f"How many {item_name} do you want to order? "))
        if desired_amount <= total_available:
            print(f"Order placed: {desired_amount} {item_name}")
        else:
            max_available = min(found_in_warehouse1, found_in_warehouse2)
            print("*" * 100)
            print(
                f"Error: Only {total_available} {item_name} available. Do you want to order {total_available} instead? (yes/no)"
            )
            print("*" * 100)

            if input().lower() == "yes":
                print(f"Order placed: {total_available} {item_name}")


2
# Get the user name
user_name = input("Please enter your username: ")
# Greet the user
print(f"Hello, {user_name}! Welcome to our wedsite.")

# Show the menu and ask to pick a choice
while True:
    print("Menu:")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")

    choice = input("Please pick a choice using the numeric values (1/2/3): ")

    if choice == "1":
        list_items()
        break
    elif choice == "2":
        search_and_order()
    elif choice == "3":
        print(f"Thank you for visiting, {user_name}!")
        break
    else:
        print("Error: Invalid operation. Please select 1, 2, or 3.")
