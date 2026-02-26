#Python slot machine
import random
def spin_row():
    symbols = [" 🍒 "," 🍉", "🍋"," ⭐","⚡"]

    return[random.choice(symbols) for _ in range(3)]   # For every iteration, it randomly selects three symbols



def print_row(row):
    print("*****************")
    print(" | ".join(row))       #joins each element of iterables by "|"
    print("*****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 8
        elif row[0] == "🍋":
            return bet * 10
        elif row[0] == "⚡":
            return bet * 12
        elif row[0] == "⭐":
            return bet * 15
    return 0
        

    

def main():
    balance = 100
    print("************************")
    print("Welcome to python slots" )
    print("Symbols:🍒 ,🍉,🍋, ⭐, ⚡")
    print("************************")

    while balance > 0:
        print(f"Current balance:GH${balance}")

        bet = input("Place your bet amount:")

        if  not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insuffiecient funds!!:( )")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won GH${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again?...(Y/N) :")

        if play_again != "Y":
            break

    print(f"Game over! Your final bet amount is GH${balance} ")


if __name__=='__main__':        #Allows program to be imported or standalone
    main()