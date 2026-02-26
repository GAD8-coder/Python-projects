class Student:
    def __init__(self, Name , Course , GPA):
        self.Name = Name
        self.Course = Course
        self.GPA = GPA

student1 = Student("Dominic","Computer Science", 4.0)
student2 = Student("Gyamfi","Information Technology",3.8)
student3 = Student("Byran","Law",3.5)

print(student1.Course)
        