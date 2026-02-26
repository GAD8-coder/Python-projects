# Object = A "bundle" of related attributes (variables) and methods (functions)
#          ex. phne , cup , book
#           You need a "class to create many objects "
#A class = (blueprint) used to design the strucutre and layout of an object
# To Access an attribute of a class is done by using ["."] the atrribute access operator
#Attributes = variables that an object has
# SELF  = refers to object we're currently working with
class Car:   
    #constructor initializes or setsup the initial state of the object 
    def __init__(self , model , year, color, for_sale):     # Constructor methods needed to construct objects
# Instance variables:...
        self.model = model                                  #When name of model is received it's assigned to the self.model obj
        self.year = year
        self.color = color
        self.for_sale = for_sale
  

#objects
car1 = Car("Bentley", 2026 ,"Periwinkle", False) 
car2 = Car("Covette", 2020 , "Silver", True)       # this invokes the constructor(calls the constructor)
car3 = Car("Bugatti CHeron",2025 , "Grey", False)
car4 = Car("Covette",2026,"Wine",False)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)