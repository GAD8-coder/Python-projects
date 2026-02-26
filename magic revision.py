#@property

class Rectangle:
    def __init__(self, width , height):
        self._width = width     #private attributes
        self._height = height    #private attributes

    @property
    def width(self):
        return f"{self._width:.2f}cm"
    @property
    def height(self):
        return f"{self._height:.2f}cm"


rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)