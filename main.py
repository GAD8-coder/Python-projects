# A concession stand program
menu = {"Pizza":10.00,
        "Rice": 20.00,
        "Meatpie": 30.00,
        "Shawama": 45.00}

cart = []
total = 0
print("-----MENU-----")

for key, value in menu.items():         #This prints the keys and values of the items in the menu
    print(f"{key} : GH$ {value:.2f}")
print("-------------")

while True:
    food = input("Select an item (Q to quit):")
    if food =="Q":
        break
    
    elif food in menu:
        cart.append((food, menu[food])) # cart stores tuples of (item, price)

print("----YOUR ORDER----")
for food in cart:
    total += menu.get(food)
    print(food , end=" ")
print()
print(f"Total is : GH$ {total:.2f}")
