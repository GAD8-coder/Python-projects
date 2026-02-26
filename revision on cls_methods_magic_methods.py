#Revision on stattic methods

class Student:
    def __init__(self, Name, course, GPA):
        self.Name = Name
        self.course = course
        self.GPA = GPA
    
    def __str__(self):
        return f"{self.Name},{self.course},{self.GPA}"
    
    def __eq__(self, other):
        return self.course == other.course  or  self.GPA == other.GPA

stu1 = Student("Claris","BSC Sociology", 3.0)
stu2 = Student("Dominic","BSC Computer Science", 3.9)
stu3 = Student("Pearl","BSC Mathematics",2.9)
stu4 = Student("Amanda","BSC Computer Science",3.8)

print(stu2 == stu4)