# Membership operators checks whether a value or variable is found in a sequence..
#       (string, tuple, ists , set or dictionary)

grades = {"Dominic":"A",
        "Stanley": "B",
        "Constant": "C",
        "Agyekum" :"D"}

admitted = True

while admitted:
    student = input("Enter name of the student:")

    if student not in grades:
        print(f"{student} not found")    # retreives value at a given key
    else:
        print(f"{student}'s grade is {grades[student]}")
