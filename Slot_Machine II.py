# demo slot machnine program
import random
def spin_row():
    symbols = ["⭐","⚡","🌠","🌞"]

    return [ random.choice(symbols)  for _ in range(3)]

def print_row(row):
    print("*************")
    print("|".join(row))
    print("**************")

def getPayout(row, bet):
    if row[0] == row[1]== row[2]:
        if row[0] == "⭐":
            return bet * 20
        if row[0] == "⚡":
            return bet * 15
        if row[0] == "🌠":
            return bet * 10
        if row[0] == "🌞":
            return bet * 5
    return 0

def main():
    balance = 100

    print("***************************")
    print("Welcome to Slot Machine 3.0")
    print("Symbols:⭐,⚡,🌠,🌞 ")
    print("************************")

    while balance > 0:
        print(f"Your current balance : {balance}")

        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter valid number")
        else:
            return 0
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!...")
            continue
        if bet <= 0:
            print("Amount must me greater than Zero!...")

        balance -= bet
        row = spin_row()
        print("Spinning...")
        print_row(row)

        payout = getPayout(row, bet)

        if payout > 0:
            print(f"You won GH${payout}")
        else:
            print("Sorry you lost this round")
        balance += payout

        play_again = input("Do you wan to play again?(Y/N) :")

        if play_again != "Y":
            break

if __name__ =='__main__':
    main()