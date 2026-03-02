import random

options = ("rock","paper","scissors")
running =  True

while running:
    player = None           #Stores the player's choice
    computer = random.choice(options)   

    while player not in options:            #prevents user from picking something outside options
        player = input("Enter a choice (rock , paper , scissors) :")

    print(f"Player: {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You Win✨ ")

    elif player == "paper" and computer == "rock":
        print("You win!✨")
    elif player == "scissors" and computer == "paper":
        print("You win!✨")
    else:
        print("You Lose!")
#   if user input after being lowercase does not equal == y, set running = False
    if not input("Play again ? (y/n) :").lower() == "y":  
        running = False

print("Thanks for playing")






