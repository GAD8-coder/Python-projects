#Banking Program

class BankAccount:
    def __init__(self, accountNumber, OwnerName , initalBalance):
        self.accountNumber = accountNumber
        self.OwnerName = OwnerName
        self.balance = initalBalance
        self.transactionHistory = []  # A list to store transaction history

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount deposited")
        else:
            self.balance += amount    #Adds the deposited amount to the balance
            self.transactionHistory.append(f"Deposited: {amount}")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount to withdraw")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount    #Subtracts the withdrawn amount from the balance
            self.transactionHistory.append(f"Withdrew: {amount}")

    def printStatement(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Owner Name: {self.OwnerName}")
        print(f"Balance: {self.balance}")
        print("Transaction History:")
        for transaction in self.transactionHistory:
            print(transaction)



# Main Program Loop:

AllAccounts = {} #Dictionary to store all bank accounts with account number as key

def main():
    while True:
        print("***************************************")
        print("\n WELCOME TO GAD8 BANKING APPLICATION\n")
        print("***************************************")

        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Print Account Statement")
        print("5. Exit")

        choice = int(input("Enter your choice(1-5):"))

        if choice == 1:
            accountNumber = input("Enter Account Number:")
            if accountNumber in AllAccounts:
                print("Account Already exists!")
            else:
                OwnerName = input("Enter Owner Name:")
                Initialdeposit = float(input("Enter Initial Deposit: "))
                newAccount = BankAccount(accountNumber, OwnerName, Initialdeposit) #Obj instantiated
                AllAccounts[accountNumber] = newAccount # Add the new account to the dictionary
                print("Account Created Successfully!")

        if choice == 2:
            SearchNumber = input("Enter Account Number to Deposit Money:")

            if SearchNumber in AllAccounts:
                amount = float(input("Enter Amount to Deposit:"))
                AllAccounts[SearchNumber].deposit(amount)

        if choice == 3:
            
