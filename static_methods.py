#STATIC METHOD: A method that belong to a class rather any object from that class
#               Usually used for general utility functions

#Instance Methods: Best for operations on instances of the class (objects)
#Static methods: BEst for utility functuons that do not need access to class data

class Employee:
    def __init__(self, Name, position):
        self.Name = Name
        self.position = position

    def get_info(self):
        return f"{self.Name} = {self.position}"
    
    @staticmethod           #Method not for any objects but for the class
    def is_valid_position(position):
        valid_position = ["Manager","Cashier","Chef", "Janitor"]
        return position in valid_position
    
#Instance Methods:  for instance methods you access an object then call the instance method
employee_1 = Employee("Dominic", "Senior MLops Enginner")
employee_2 = Employee("Amanda","Manager")
employee_3 = Employee("Priscilla", "Assistant Manager")
employee_4 = Employee("Chloe","Secretary")
    
print(Employee.is_valid_position("Rocket scientist"))   
print(employee_4.get_info())