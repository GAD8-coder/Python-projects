#Decorators =   A function that extends the behaviour of another func
#               without modifying the base function
#               pass the base function as an argument to the  decorator

#Adding something to a base function without changing it
#creating a decorator

#def add_sprinkles(func):
#    def wrapper(*args, **kwargs):
#        print("You add sprinkles")
#        func(*args, **kwargs)
#    return wrapper
#def add_fudge(func):
#    def wrapper(*args, **kwargs):
#        print("You add fudge")
#        func(*args, **kwargs)
#    return wrapper


#@add_sprinkles
#@add_fudge
#def get_ice_cream(flavor):
#    print(f"Here is your {flavor} ice cream")

#get_ice_cream("vanilla")

def add_nitrous(func):
    def body_parts(*args, **kwargs):
        print("You add nitrous")
        func(*args, **kwargs)
    return body_parts

def add_suspension(func):
    def body_parts(*args, **kwargs):
        print("You add suspension")
        func(*args, **kwargs)
    return body_parts


@add_nitrous
@add_suspension
def get_car(model):
    print(f"Here is your {model} car")

get_car("Mercedes Benz")