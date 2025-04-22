import products
import store


def exit_store():
    """
    Exit the program.
    """
    print("GOODBYE!")


def make_order(store_instance):
    """
    Handle making an order.
    """
    list_all_products(store_instance)

    print("\nTo FINISH your order, press ENTER.")

    shopping_list = []

    while True:
        user_order = input("\nEnter the product # you want: ").strip()

        if user_order == "":
            break

        if not user_order.strip():
            print("Empty input not valid. Please enter a product #.")
            continue

        try:
            product_id = int(user_order) - 1
            store_inventory = store_instance.get_active_products()

            if product_id < 0 or product_id >= len(store_inventory):
                print("Invalid product number. Try again.")
                continue

            product = store_inventory[product_id]

            while True:
                amount = input("Enter the amount you want: ").strip()

                if user_order == "":
                    break

                if not amount.isdigit():
                    print("Please enter a valid number for the amount.")
                    continue

                amount = int(amount)
                if amount <= 0 or amount > product.quantity:
                    print(f"Please enter an amount between 1 and {product.quantity}.")
                    continue

                else:
                    break


            shopping_list.append((product, amount))

            # Update product quantity
            product.buy(amount)

            if product.quantity == 0:
                print_framed_message(f"{product.name} is now SOLD OUT!")

                # Check if anything is left to buy
                active_products = [product for product in store_instance.product_list if product.is_active]
                if not active_products:
                    print_framed_message("EVERYTHING IS SOLD OUT!")
                    return
                else:
                    list_all_products(store_instance)

        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        print_framed_message(f"Order made! Total payment {store_instance.order(shopping_list)}")


def show_total_quantity(store_instance):
    """
    Show the total number of items in the store.
    """
    print(f"\nTotal of {store_instance.get_total_quantity()} items in store.")


def list_all_products(store_instance):
    """
    List all products in the store.
    """
    if len(store_instance.get_all_products()) == 0:
        print_framed_message("EVERYTHING IS SOLD OUT!")

    else:
        for index, product in enumerate(store_instance.get_all_products(), start=1):
            print(f"{index}. {product}")


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


def execute_user_choice(store_instance):
    """
    Handle user input and calls corresponding function.
    """
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
            if len(store_instance.get_all_products()) == 0:
                exit_store()
                return

            input("\nPress ENTER to get back to the MENU.")
            print()
            start()

        else:
            print("Invalid choice, please try again.")


def start():
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
    start()
    execute_user_choice(best_buy)


if __name__ == "__main__":
    main()

