# hangman game in python
import random

words = ("apple","orange","banana","coconut","pineapple","pkeach")


#dictionary of key:()
hangman_art = {0: ("     ",
                   "     ",
                   "     ",),
               1: ("  O  ",
                   "     ",
                   "     ",),

               2: ("  O  ",
                   "  |  ",
                   "     ",),

               3: ("  O  ",
                   "/ |  ",
                   "     ",),

               4: ("  O  ",
                   " /|\ ",
                   "     ",),

               5: ("  O  ",
                   " /|\  ",
                   " /   ",),

               6: ("   O  ",
                   "  /|\ ",
                   "  / \ ",),}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))      #Displays a space character between each hint.

def display_answer(answer):
     print(" ".join(answer))      #Displays a space character between each hint.


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)     #Total number of underscores corresponding to answer   
    print(hint )
    wrong_guesses = 0                      
    guessed_letters = set()                 #Keeps track of incorrect guesses made
    is_running = True


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter :").lower()
#A loop that iterates ones for each charater within the answer>>

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")  
            continue
#Adds guessed letters into guessed letters set().
        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        guessed_letters.add(guess)

       
        if guess in answer: 
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
#Ones wrong  guesses is >= 6.. you lose
        elif wrong_guesses >= len(hangman_art) - 1: 
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!!! ")
            is_running = False






if __name__ == "__main__":          #If runnning file directly i'd like to call main function to run the prgram
    main()
