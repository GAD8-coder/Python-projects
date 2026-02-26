
#Super() =   Function used in a child class to call methods from a parent class (superclass)
#               Allows you to extend the functionality of the  inherited methods

class shape:
    def __init__(self, colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"Its is {self.colour} and {'filled' if self.is_filled else 'not filled'}" )
class Circle(shape):
    def __init__(self, colour , is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle of radius:{3.14 * self.radius*self.radius}cm^2")
        super().describe()

        

class Sqaure(shape):
    def __init__(self, colour , is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width
    
    def describe(self):
        print(f"It is a sqaure with area:{self.wdth *self.width}cm^2")
        super().describe()
    

class Triangle(shape):
    def __init__(self, colour , is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height
      
    def describe(self):
        print(f"It is a triangle with area:{self.width * self.height / 2}cm^2")
        super().describe()
    

#OBJECTS
circle = Circle(colour="Green",is_filled="True",radius= 5)
square = Sqaure(colour="Red",is_filled="False",width= 7 )
triangle = Triangle(colour="Blue",is_filled="True",width= 9, height= 5)

triangle.describe()