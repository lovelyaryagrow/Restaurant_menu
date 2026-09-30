menu={'Pizza':100,
      'Pasta':50,
      'Burger':35,
      'Salad':80,
      'Coffee':65,
      'pizza':100,
      'pasta':50,
      'burger':35,
      'salad':80,
      'coffee':65,
    }
print("Welcome to our restaurant")
print("Pizza: Rs.100\nPasta: Rs.50\nBurger: Rs.35\nSalad: Rs.80\nCoffee: Rs.65")

order_total=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item{item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available in the menu!")
another_order=input("Do you want to add another item to your order?(Yes/No/yes/no)")
while another_order == "Yes" or another_order == "yes":
    item_2=input("Enter the name of second item you want to order=")
    if item_2 in menu:
        order_total+=menu[item_2]
        print("Item {item_2} has been added to your order")
    else:
        print("Ordered item {item_2} is not available in the menu!")
    another_order=input("Do you want to add another item to your order?(Yes/No/yes/no)")

print(f"The total amount of items you ordered is {order_total}")










     

