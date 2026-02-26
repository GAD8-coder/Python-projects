#class_variables = shared among all objects of a class
#                   Defined outside the constructor
#                    Allow you to share data among  all bjects created from that class
#                   Access a class variable by the name of the class.(Name of the class variable)
#                      It's more explicit to access a class variable by using the class name
#                       To modify a claa variable in place of class we use[name of class]
class student:
#   class variables...  
    class_gradyear = 2030           # class variable of class_grad_year
    num_of_students = 0
    num_of_boys = 1456
    
    def __init__(self, Name , age):      #instance variables ; those within the constructor
       self.Name = Name
       self.age = age
       student.num_of_students += 1

student1 = student("STANLEY", 50)
student2 = student("CONSTANT",40) 
student3 = student("TWUM-BENEDICT",45)
student4 = student("DOMINIC",55)     

print(f"My graduating class of {student.class_gradyear} has {student.num_of_students} students")
print(student1.Name)
print(student2.Name)
print(student3.Name)


