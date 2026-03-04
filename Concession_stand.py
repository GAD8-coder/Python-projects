#Concession stand program

menu = {"Pizza":20.50,
        "Rice":10.50,
        "Chips":4.50,
        "Popcorn":5.50,
        "Cola":15.50,
        "Meat-pie":70.50,
        "Soda" : 50.50,
        "Fries" : 20.15,
        "Pretzel" : 20.00,}


cart = []
total = 0

print("-----------MENU-----------")
for key , value in menu.items():
    print(f"{key:10}: GHC{value:.2f}")
print("--------------------------")


while True: 
    food = input("Select an item (Q to quit):")
    if food == "Q":
        break
#Checks if a user types in an item not in menu
    elif menu.get(food) is not None:
        cart.append(food) #Adds food item to cart

#Calculates total, gets value associated with food
print("---------YOUR ORDER--------------")
for food in cart:
    total += menu.get(food) 
    print(food , end=" ")

print()
print(f"Total : GHC{total:.2f} ")

