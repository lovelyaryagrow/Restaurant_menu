def add_item(menu, item, order_total):
    if item in menu:
        order_total += menu[item]
        print(f"Item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available in the menu!")

    return order_total
