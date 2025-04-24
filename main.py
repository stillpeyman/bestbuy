import products
import store


def display_menu():
    """
    Display the store menu.
    """
    title = "STORE MENU"
    options = [
        "1. List all products in store",
        "2. Show total amount in store",
        "3. Make an order",
        "4. Quit"
    ]

    # space on each side
    padding = 4

    # centered title, underlined with dashes
    lines = [title.center(40)]

    # determine max width
    max_length = max(len(line) for line in lines)
    width = max_length + padding * 2
    border = "*" * (width + 2)

    # dashed lines under title but in full width
    dash_line = "–" * (width - 2)
    lines.append(dash_line)

    # left-aligned options
    for option in options:
        lines.append(option)

    # print framed border
    print(border)
    # top spacing
    print("*" + " " * width + "*")

    for i, line in enumerate(lines):
        # center first two lines
        if i < 2:
            padded_line = line.center(width)

        else:
            # left-align options
            padded_line = (" " * 4 + line).ljust(width)

        print(f"*{padded_line}*")

    # bottom spacing
    print("*" + " " * width + "*")
    print(border)


def start(store_instance):
    """
    Handle user input and calls corresponding function.
    """
    display_menu()

    choices = {
        "1": list_all_products,
        "2": show_total_quantity,
        "3": make_order,
        "4": exit_store
    }

    while True:
        user_choice = input("\nPlease choose a number: ").strip()
        print()
        action = choices.get(user_choice)

        if user_choice == "4":
            exit_store()
            return

        elif action:
            action(store_instance)
            input("\nPress ENTER to get back to the MENU.")
            print()
            display_menu()

        else:
            print("Invalid choice, please try again.")


def list_all_products(store_instance):
    """
    List all products in the store.
    """
    if len(store_instance.get_all_products()) == 0:
        print_framed_message("EVERYTHING IS SOLD OUT!")

    else:
        for index, product in enumerate(store_instance.get_all_products(), start=1):
            print(f"{index}. {product}")


def show_total_quantity(store_instance):
    """
    Show the total number of items in the store.
    """
    print(f"\nTotal of {store_instance.get_total_quantity()} items in store.")


def show_available_products_for_order(store_instance, reserved_quantities):
    """
    Show available products for order, with their remaining quantities.
    """
    # init a list of tuples (available_product, quantity: available_left)
    available_products = []

    for product in store_instance.get_active_products():
        reserved = reserved_quantities.get(product, 0)
        if reserved < product.quantity:
            available_left = product.quantity - reserved
            available_products.append((product, available_left))

    if not available_products:
        return []

    print("-" * 10)
    for i, (product, available_left) in enumerate(available_products, start=1):
        print(f"{i}. {product.name}, Price: {product.price}, Quantity: {available_left}")
    print("-" * 10)

    # Return list of only products because in make_order() user will choose from this list by index number
    return [product for product, _ in available_products]


def make_order(store_instance):
    """
    Handle making an order.
    """
    shopping_list = []
    reserved_quantities = {}

    print("\nTo FINISH your order, press ENTER.")
    print("To CANCEL your order, enter 'q'.")

    while True:
        # Create a list of available products and show available products before each selection
        available_products = show_available_products_for_order(store_instance, reserved_quantities)

        if not available_products:
            print_framed_message("EVERYTHING IS SOLD OUT!")
            break

        user_order = input("\nEnter the product # you want: ").strip()

        if user_order == "":
            break

        if user_order.lower().strip() == "q":
            print("ORDER CANCELLED.")
            return

        if not user_order.isdigit() or not (1 <= int(user_order) <= len(available_products)):
            print("Invalid choice. Try again.")
            continue

        product_nr = int(user_order) - 1
        product = available_products[product_nr]

        while True:
            amount = input("Enter the amount you want: ").strip()

            if amount == "":
                break

            if amount.lower().strip() == "q":
                print("ORDER CANCELLED.")
                return

            if not amount.isdigit():
                print("Please enter a valid number for the amount.")
                continue

            amount = int(amount)
            reserved = reserved_quantities.get(product, 0)
            available_to_order = product.quantity - reserved

            if amount <= 0 or amount > available_to_order:
                print(f"Please enter an amount between 1 and {available_to_order}.")
                continue

            break

        # Update reserved quantities and add to shopping list
        reserved_quantities[product] = reserved + amount
        shopping_list.append((product, amount))

        print(f"Your current total is {store_instance.calculate_subtotal(shopping_list)}")

        # Check if product now sold out (based on reserved)
        if reserved_quantities.get(product, 0) == product.quantity:
            print_framed_message(f"{product.name} is now SOLD OUT!")

    if shopping_list:
        print_framed_message(f"Order made! Total payment {store_instance.order(shopping_list)}")


def print_framed_message(message: str, pad: int = 4):
    """
    Print any message framed with asterisks, padded and centered.
    """
    lines = message.split("\n")
    max_length = max(len(line) for line in lines)
    width = max_length + pad * 2
    border = "*" * (width + 2)

    print()
    print(border)
    for line in lines:
        print("*" + line.center(width) + "*")
    print(border)
    print()


def exit_store():
    """
    Exit the program.
    """
    print("GOODBYE!")


def main():
    """
    Main function starts the program.
    """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    # create Store instance
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

