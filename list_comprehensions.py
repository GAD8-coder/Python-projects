#Lists comprehensions = Faster a concuse way if writing loops in python
#                       compact and easier to read than traditional loops
#           formula = [expression  for value  in iterable(range..etc) if condition]

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for key,value in kwargs.items():
        print(f"{key}:{value}")

shipping_label("Dr.", "Dominic","Atakplai",
               street="Ajei-Kwame street",
               city="Nmai-Dzorn",
               state="Accra",
               digital_adress="GD-245-4240")


