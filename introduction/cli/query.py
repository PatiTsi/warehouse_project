from data import warehouse1, warehouse2


# Function to list items by warehouse
def list_items():
    print("Items in Warehouse 1:")
    for item in warehouse1:
        print(f"- {item}")
    print("\nItems in Warehouse 2:")
    for item in warehouse2:
        print(f"- {item}")


# Function to search for an item and place an order
def search_and_order():
    item_name = input("Enter the item name you want to search for: ")

    # Search in both warehouses
    found_in_warehouse1 = item_name in warehouse1
    found_in_warehouse2 = item_name in warehouse2

    total_available = found_in_warehouse1 + found_in_warehouse2

    if total_available == 0:
        print(f"{item_name} is Not in stock.")
        return

    print(f"Total available: {total_available} item(s)")

    # Determine the location of the item
    location = []
    if found_in_warehouse1:
        location.append("Warehouse 1")
    if found_in_warehouse2:
        location.append("Warehouse 2")

    print("Location:", ", ".join(location))

    # Check which warehouse has more of the item
    if found_in_warehouse1 and found_in_warehouse2:
        if warehouse1.count(item_name) > warehouse2.count(item_name):
            print("Warehouse 1 has more.")
        else:
            print("Warehouse 2 has more.")

    order_choice = input(
        "Do you want to place an order for this item? (yes/no): "
    ).lower()

    if order_choice == "yes":
        desired_amount = int(input(f"How many {item_name} do you want to order? "))
        if desired_amount <= total_available:
            print(f"Order placed: {desired_amount} {item_name}")
        else:
            max_available = min(found_in_warehouse1, found_in_warehouse2)
            print(
                f"Error: Only {max_available} {item_name} available. Do you want to order {max_available} instead? (yes/no)"
            )
            if input().lower() == "yes":
                print(f"Order placed: {max_available} {item_name}")


# Main program
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!")

while True:
    print("\nMenu:")
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
