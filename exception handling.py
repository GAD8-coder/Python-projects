#Exception = An event that interrupts the flow of a program
#           (ZeroDivisionError , TypeError, Value Error)
#           1. Try, 2.Except 3.Finally
#ZeroDivisionError  = Trying to divide a number ny zero (1/0)
#TypeError =   Attempting to perform an operation with a value of wrong datatype (1 + "1")
#ValueError =   Attempting to typecast a value with wrong datatype (int("Pizza"))

#try:
#    number = int(input("Enter a number:"))
#    print(1/ number)
#except ZeroDivisionError:
#    print("You can't divide by zero!")
#except ValueError:
#    print("Enter only numbers")
#finally:
#    print("Do some clean up here!")

def my_self(func):
    def wrapper(name, age):
        print(f"Hi {name}..you're {age} years old")
        return func(name,age)
    return wrapper 

@my_self
def greet(name,age):
    print(f"Hello, {name}")
