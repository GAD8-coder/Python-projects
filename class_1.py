#Inheritance = Allows a class to inherit attibutes and methods from another class
#               helps with code reusability and extensibility
#               class child(parent)/ sub and super classes

#class Animal:
#    def __init__(self, Name):
#        self.Name = Name
#        self.is_alive = True

#    def eat(self):
#        print(f"{self.Name} is eating")

#    def sleep(self):
#        print(f"{self.Name} is asleep")
        

#class Dog(Animal):
#    def speak(self):
#        print("WOOF!!")

#class Cat(Animal):
#    def speak(self):
#        print("MEOW!!")

#class Mouse(Animal):
#    def speak(self):
#        print("SQUEAK!!")

#dog = Dog("Sparkie")
#cat = Cat("Tom")
#mouse = Mouse("Jerry")

#print(dog.Name)
#dog.speak()

#-----------------------------------------------------------------------------

#MULTIPLE INHERITANCE =  inherits from more than one parent class
#                       C(A,B)

#MULTILEVEL INHERITANCE = inherit from a parent which inherits from another parent
#                           C(B) <- B(A)<- A

class Animal:
    def __init__(self, Name):
        self.name = Name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(Animal):
    def Hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(prey):
   pass
class Hawk(predator):
    pass

class Fish(prey,predator):
    pass

rabbit = Rabbit("Buggs")
fish = Fish("Nimo")
hawk = Hawk("Tony")

fish.sleep()