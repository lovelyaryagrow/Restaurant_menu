from menu import menu
from display import show_welcome, show_menu
from input_handler import get_item, ask_for_another_item
from order import add_item


def main():
    # Display restaurant information
    show_welcome()
    show_menu(menu)

    # Initialize total
    order_total = 0

    # Take first order
    item = get_item()
    order_total = add_item(menu, item, order_total)

    # Take additional orders
    while ask_for_another_item():
        item = get_item()
        order_total = add_item(menu, item, order_total)

    # Display final bill
    print("\n----------------------------")
    print(f"Total amount: Rs.{order_total}")
    print("Thank you for ordering!")
    print("----------------------------")


if __name__ == "__main__":
    main()
