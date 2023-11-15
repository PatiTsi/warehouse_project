from data import stock, personnel
from datetime import datetime


# Get/Return the user name.
def get_user_name():
    return input("Please enter the username: ")


# Greet the user
def greet_user(username):
    print(f"Hello {username}, Welcome to the Re_conNect website")


# Show the menu and ask to pick a choice
def select_operation():
    while True:
        print("*" * 120)
        print("What would you like to do?")
        print("-" * 120)
        print("1. List items by warehouse")
        print("2. Search an item and place an order")
        print("3. Browse by category")
        print("4. Quit")
        print("-" * 120)
        menu_option = input("Please pick a choice using the numeric values (1/2/3/4): ")

        if menu_option in ["1", "2", "3", "4"]:
            return menu_option
        else:
            print(
                "Invalid input, please enter a number between 1 and 4 for a valid option"
            )
            print("*" * 100)


# List and count all items by warehouse.
def list_item_by_warehouse():
    total_warehouses = {}

    for item in stock:
        item_name = item["state"] + " " + item["category"]
        warehouse = item["warehouse"]
        if warehouse not in total_warehouses:
            total_warehouses[warehouse] = []

        total_warehouses[warehouse].append(item_name)

    for warehouse, items in total_warehouses.items():
        print(f"Items in warehouse {warehouse}:")
        for id, item in enumerate(items, start=1):
            print(f"{id}. {item}")
        print(f"Total items in Warehouse {warehouse} is {len(items)}")
        print("*" * 40)

    continue_session = input(
        f"Do you want to continue with another operation? (yes/no)"
    )
    if continue_session == "yes":
        select_operation()


# Search for an item and place an order
def search_and_order_item(user_name):
    item_name = input("Enter the item name you want to search for: ").lower()
    search_item_state = " ".join(item_name.split(" ")[:-1]).capitalize()
    search_item_category = item_name.split()[-1].capitalize()

    location = []
    found_in_warehouses = {1: 0, 2: 0, 3: 0, 4: 0}
    order_item = None

    for item in stock:
        if (
            item["state"] == search_item_state
            and item["category"] == search_item_category
        ):
            days = (
                datetime.now()
                - datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
            ).days
            location.append(f"Warehouse {item['warehouse']} (in stock for {days} days)")
            found_in_warehouses[item["warehouse"]] += 1
            if found_in_warehouses[item["warehouse"]] == 1:
                order_item = item

    total_available = sum(found_in_warehouses.values())

    if total_available == 0:
        print(f"{item_name} is not in stock.")
        return "Searched for an item and found 0 available."

    print(f"Amount available: {total_available} item(s)")
    print("Location:")
    for loc in location:
        print(f"- {loc}")

    max_available_warehouse = max(found_in_warehouses, key=found_in_warehouses.get)
    print(f"Maximum availability: Warehouse {max_available_warehouse}")

    order_choice = input("Would you like to order this item? (yes/no) ").lower()

    if order_choice == "yes":
        if order_item and can_place_order(user_name):
            desired_amount = int(input(f"How many {item_name} do you want to order? "))
            max_available = found_in_warehouses[max_available_warehouse]
            if desired_amount <= max_available:
                print(f"Order placed: {desired_amount} {item_name}")
                return f"Ordered {desired_amount} {item_name}"
            else:
                print(f"I am sorry, only {max_available} {item_name} is available.")
                return f"Attempted to order {desired_amount} {item_name}, but only {max_available} available."
        else:
            return "Order not placed. Authentication failed or item not found."

    return "Searched for an item and did not place an order."


# Check if the user can place an order
def can_place_order(user_name):
    password = input("Please enter your password: ")
    for person in personnel:
        #    if person["name"] == user_name and person["password"] == password:
        #        return True
        # print("Authentication failed. Please check your username and password.")
        # return False
        if (
            "name" in person
            and "password" in person
            and person["name"] == user_name
            and person["password"] == password
        ):
            return True

    print("Authentication failed. Please check your employee username and password.")
    return False


# Browse items by category
def browse_by_category():
    category_mapping = [item["category"] for item in stock]
    category_count = {
        category: category_mapping.count(category) for category in set(category_mapping)
    }
    category_id_mapping = {
        id + 1: category for id, category in enumerate(category_count)
    }

    for category_id, category_name in category_id_mapping.items():
        print(f"{category_id} {category_name} ({category_count[category_name]})")

    select_category = input("Type the category number to browse: ")
    category_id = int(select_category)

    if category_id in category_id_mapping:
        category_name = category_id_mapping[category_id]
        count_items_by_category = 0

        for item in stock:
            if item["category"] == category_name:
                print(
                    f"{item['state']} {item['category']}, Warehouse {item['warehouse']}"
                )
                count_items_by_category += 1

        print("." * 120)
        print(f"Total items in this category are: {count_items_by_category}")
        print("." * 120)
        return f"Browsed the category {category_name}."
    else:
        return "Invalid category choice."


# Run the main script
def main():
    user_name = get_user_name()
    greet_user(user_name)

    actions = []

    while True:
        operation = select_operation()
        # If user pick option 1
        if operation == "1":
            actions.append(list_item_by_warehouse())
        # If user pick option 2
        elif operation == "2":
            actions.append(search_and_order_item(user_name))
        # If user pick option 3
        elif operation == "3":
            actions.append(browse_by_category())
        # If user pick option 4
        else:
            break

    print(f"Thank you for your visit, {user_name}!")
    if actions:
        print("In this session you have:")
        for i, action in enumerate(actions, start=1):
            print(f"{i}. {action}")


if __name__ == "__main__":
    main()
