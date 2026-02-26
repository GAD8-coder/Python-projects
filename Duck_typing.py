#Duck typing    = Another way to achieve polymorphisim besides inheritance
#                   object must have the minimum necessary attributes/ methods
#                   "if it looks like a duck , quacks like a duck then it must be a duck"
# 

class Animal:
    alive = True
    

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

#This class has nothing to do with animals
class Car:

    alive = False
    def speak(self):
        print("Honk")
        
animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)

 