#Python File Detection

import os       #Gain Access to operating system
 
file_path = "C:/Users/DOMINIC/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
        
else:
    print("That location does not exist")