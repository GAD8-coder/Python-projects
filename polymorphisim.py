
#polymorphisim =   POLY = MANY
#                    MORPHE = FORM

#WAYS TO ACHIEVE PLOYMORHISIM
#   1. INheritance = An object could be treated as the same type as a parent class
#   2. DUCK-TYPING = Object must have neccesary attributes/methods
from abc import ABC , abstractmethod            
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius   

    def area(self):
        return 3.14 * self.radius **2  

         

    
        

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side **2
         

class Triangle(Shape):
    def __init__(self, base , height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping,radius):
        super().__init__(radius)
        self.topping = topping
        
        

shapes = [Circle(4), Square(8), Triangle(7,19), Pizza("Pepperoni", 14)]

for shape in shapes:
    print(f"{shape.area()}cm^2") 