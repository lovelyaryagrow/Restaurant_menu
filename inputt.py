def get_item():
    item = input("Enter the name of item you want to order: ")
    return item.strip().lower()


def ask_for_another_item():
    answer = input(
        "Do you want to add another item to your order? (Yes/No): "
    )

    return answer.strip().lower() == "yes"
