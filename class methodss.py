#Class Methods = Allows operations related to the class itself
#                Take (cls) as the first parameter, which represents as the class itself.
 
class Student:

    count = 0
    total_GPA = 0

    def __init__(self,Name , GPA):
        self.Name = Name
        self.GPA = GPA
        Student.count += 1   # Increases by 1 whenever we create a student object
        Student.total_GPA += GPA
#Instance method ; has self as a parameter
    def get_info(self):
        return f"{self.Name} {self.GPA}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"
    
    @classmethod
    def get_average_GPA(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA :{cls.total_GPA/cls.count :.2f}"
        
    
student_1 = Student("Dominic", 4.0)
student_2 = Student("Louis", 4.0)
student_3 = Student("Eugene", 2.0)
student_4 = Student("Leas", 3.0)
student_5 = Student("Squidward", 3.4)
    
#calling a class method
print(Student.get_count())    
print(Student.get_average_GPA())

