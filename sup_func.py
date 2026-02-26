#super function revision:      It's normally used in the child class to call methods from the parent class
#NB//; The child class is the sub class and the parent class is the super class
# if child class shares smililar method as parent, child method will override parents method
# to extend the functionality of method of a parent , USE the super function
# super function can be used within a child class to be used within a constructor to assign attributes 
class Shapes:

    def __init__(self, colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'Not filled'}")

class Circle(Shapes):
    def __init__(self,colour,is_filled, radius):
        super().__init__(colour,is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is circle of radius {3.147 * self.radius * self.radius}cm^2")
        super().describe()



class Square(Shapes):
    def __init__(self,colour,is_filled, width):
        super().__init__(colour,is_filled)
        self.width = width

class Triangle(Shapes):
     def __init__(self,colour,is_filled, width, height):
        super().__init__(colour,is_filled)
        self.width = width
        self.height = height

#creating some objects here:
circle = Circle("Pink",True, 14)
square = Square("Blue",False,12)
triangle = Triangle("Yellow",True,8, 16)

circle.describe()