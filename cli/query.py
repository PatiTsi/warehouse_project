"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# Function to list items by warehouse
def list_items():
    print("Items in Warehouse 1:")
    for item in warehouse1:
        print(f"- {item}")
    print("Items in Warehouse 2:")
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

    order_choice = input("Do you want to place an order for this item? (yes/no): ").lower()
    
    if order_choice == "yes":
        desired_amount = int(input(f"How many {item_name} do you want to order? "))
        if desired_amount <= total_available:
            print(f"Order placed: {desired_amount} {item_name}")
        else:
            max_available = min(found_in_warehouse1, found_in_warehouse2)
            print(f"Error: Only {max_available} {item_name} available. Do you want to order {max_available} instead? (yes/no)")
            if input().lower() == "yes":
                print(f"Order placed: {max_available} {item_name}")



user_name = input("Please enter your name: ")             # Get the user name
print(f"Hello, {user_name}!")                             # Greet the user

while True:
    print("\nMenu:")                                         # Show the menu and ask to pick a choice
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")

    choice = input("Please pick a choice using the numeric values (1/2/3): ")

    if choice == "1":                                               # If they pick 1
        list_items()
        break
    elif choice == "2":                                              # Else, if they pick 2
        search_and_order()
    elif choice == "3":
        print(f"Thank you for visiting, {user_name}!")                  # Else, if they pick 3
        break
    else:
        print("Error: Invalid operation. Please select 1, 2, or 3.")          # Thank the user for the visit      
