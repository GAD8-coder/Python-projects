#Static methods =   A method that that belong to a class rather than from any object from that class(instance)
#                   Usually used for general utility functions
# 
# Instance Methods =    Best for operations on instances of the class (objects)
# Static methods    =   Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, Name , Position):
        self.Name = Name
        self.Postion = Position

    def get_info(self):         #Instance methods
        return f"{self.Name} = {self.Postion}"
    
    @staticmethod           #Belongs to the class not any method created from that class
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions
employee_1 = Employee("Eugene","Manager")
employee_2 = Employee("Squidward","Cashier")
employee_3 = Employee("SpongeBob","Cook")

print(employee_1.get_info())
print(employee_2.get_info())
print(employee_3.get_info())
