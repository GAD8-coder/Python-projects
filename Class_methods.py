# class_methods..
#methods =     Actions that our objects can perform
#               They're functions that belong to an object

class student:
    def __init__(self, student_ID, Name, Level, course, GPA):
        self.student_ID = student_ID
        self.Name = Name
        self.Level= Level
        self.course = course
        self.GPA = GPA
    
    def study(self):
        print(f"{self.Name} studys his slides")

    def program(self):
        print(f"{self.Name} programs in python")

    def description(self):
        print(f"{self.student_ID},{self.Name},{self.course}, {self.GPA}")
 

Student_1 = student("01011001","ATAKPLAI GYAMFI DOMINIC","100","BSC COMPUTER SCIENCE",4.0)
Student_2 = student("01011002","LAWER LOUIS NARTEH","100","BSC COMPUTER SCIENCE", 4.0)
Student_3 = student("01011003","EMANUEL KENA ANOBI","100","BSC COMPUTER ENGINEERING", 4.0)

Student_1.description()