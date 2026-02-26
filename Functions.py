#Function == Block of code that runs when only it is called
#               data passed into a functiona re known as parameters

def my_function(first_name , last_name):
    print(first_name  + " " + last_name)

my_function("Dominic", "Atakplai")
my_function("David", "Atakplai")
#examples of args(*)
def another_func(*kids):
    print("The youngest child is " + kids[4])

another_func("Helena", "David", "Herty", "Harriet" , "Dominic")

def cars(*luxury_cars):
    print("The most expensive luxury car is a" +" "+ luxury_cars[3] )

cars("Benz", "BMW","Tesla","Cyber Truck","Bugaati","Rolls royce")
# Below is an example of  kwargs
def demanding_jobs(job1, job2, job3):
    print("The most demanding job is " + job1)

demanding_jobs(job1="AI/ML", job2= "Cybersecurity",job3= "Cloud computing")

#Examples of Kwargs
#def my_funx(**kid):
#    print("His last name is " + kid["last_name"])
#my_funx(first_name = "Dominic", last_name = "Atakplai")

#Default parameter value
# Calling a function without argument results to default value
# example of default argument 
#def fav_car(favourite = "Audi"):    # This sets default to Audi
#    print("My favourite car is"+ " " + favourite )

#fav_car("Lamborghini")
#fav_car("Maclaren")
#fav_car()

#Passing lists as an argument

#def my_list(food):
#    for x in food:
#        print(x)
#fruits = ["Apple","Banana","Orange"]
#my_list(fruits)

#Pass statement
#Recursion
#def tri_recursion(k):
#    if(k>0):
#        result = k + tri_recursion(k-1)
#        print(result)
#    else:
#        result = 0
#    return result

#print("\n\nrecursion Example results")
#tri_recursion(6)

#Lambda functions
x = lambda a : a + 10
print(x(5))

y = lambda q , p , r :q + p + r
print(y(12,2,3))

def multifunc(n):
    return lambda a : a * n
doubler = multifunc(5)

print(doubler(8))

def multifunction(x):
    return lambda a : a * x
multiple_three = multifunction(3)
multiple_two = multifunction(2)

print(multiple_three(3))
print(multiple_two(2))
