#Magic methods =   Dunder methods(double underscore) __init__,__str__,__eq__
#                   They're automatically called by many of python's built in operations,
#                   They allow developers to define or custormise the behaviour of objects

class Book:
    def __init__(self,Title , Author , Num_pages):
        self.Title = Title
        self.Author= Author
        self.Num_pages = Num_pages
#dunder str .. returns a string rep of the object when printed directly to the console
    def __str__(self):
        return f"'{self.Title}' by {self.Author}"
# In actual sense hwen you print an object directly the console returns a memory address
#0bjects
#NB//: When we call the class of book and pass in some arguments we call the (__init__  )

#__eq__: compares if two objects are equal
    def __eq__(self, other):
        return self.Title == other.Title and self.Author == other.Author
#__lt__/__gt__: compares if two objects are greater or less than
    def __lt__(self, other):
        return self.Num_pages < other.Num_pages
    
     
    def __gt__(self, other):
        return self.Num_pages > other.Num_pages
#__add__: Adds to objects together
    def __add__(self,other):
        return f" {self.Num_pages + other.Num_pages} pages"
#__contains__: searching for key words within one of the attributes of an object
    def __contains__(self, keyword):
        return keyword in self.Title or keyword in self.Author
#__getitem__: searching for a key given an object
    def __getitem__(self, key):#Accessing book attributes by indexing
        if key == "Title":
            return self.Title
        elif key == "Author":
            return self.Author
        elif key =="Num_pages":
            return self.Num_pages
        else:
            return f" key '{key}' was not found"


#objects........Object Attributes: 
book_1 = Book("ATomic Habits","James Clear",320)
book_2 = Book("In Pursuit of Purpose","Dr. Myles Munroe", 415)
book_3 = Book("Good Morning Holy spirit","Pastor Benny Hinn",300)

print(book_1['audio'])
# We can't use < or  > on two objects unless custormised(__lt__/ __gt__)