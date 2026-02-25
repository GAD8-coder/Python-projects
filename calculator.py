#This is a python calculator...
#Syntax, Loops, conditionals, functions , data structures

def add(x, y):
    return x + y

def subtract( p, q):
    return p - q

def Multiply(a , b):
    return a * b
    

def divide(e , h):
    return e / h

def main():
    is_running = True

    while is_running:
        print("\n THIS IS A PYTHON CALCULATOR...")
        print("1. Addition")
        print("2. subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose from the options : ")

        if choice == "1":
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter Second number:"))
                result = add(x , y)
                print(f" {x} + {y} Result: {result}")
            except ValueError:
                print("Invalid Input..please enter numbers only")

        elif choice == "2":
            try: 
                p = float(input("Enter first:"))
                q = float(input("Enter second:"))
                result = subtract(p , q)
                print(f"{p} - {q} Result: {result}")
            except ValueError:
                print("Invalid input Enter numbers only...")
            
        elif choice == "3":
            try:
                a = float(input("Enter first:"))
                b = float(input("Enter second:"))
                result = Multiply(a , b)
                print(f"{a} * {b} Result: {result}")
            except ValueError:
                print("Invalid input Enter numbers only...")

        elif choice == "4":
            try:
                e = float(input("Enter first:"))
                h = float(input("Enter second:"))
                result = divide(e , h)
                print(f"{e} / {h} Result: {result}")
            except ValueError:
                print("Invalid input Enter numbers only...")
            except ZeroDivisionError:
                print("Cannot divide by zero(0)..")

        else:
            print("Invalid input..Try again!")

if __name__ =="__main__":
    main()