from codecs import backslashreplace_errors
from operator import index


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Deposit must be positive!")
            return

        self.__balance += amount
        print(f"Deposit accepted, New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Withdraw must be positive!")
            return

        if amount > self.__balance:
            print(f"({self.account_holder})Insufficient funds.")
            return

        self.__balance -= amount
        print(f"({self.account_holder})Withdraw accepted, New balance: {self.__balance}")

    def __update_balance(self, new_balance):
        self.__balance += new_balance

    def transfer(self, other_account, amount):
        if amount < 0:
            print(f"({self.account_holder})Transfer amount must be positive!")
            return
        other_account.withdraw(amount)
        self.__balance += amount
        print(f"({other_account.account_holder} > {self.account_holder})Transfer accepted, New balance: {self.__balance}")

class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        user_input = int(input("""
            0. Enter 0 to exit
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
        """))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input < 0 or user_input > 4:
            print("Please Enter a valid input")

        return user_input

    def create_pin(self):
        if self.pin == "":
            self.pin = input("Create you pin please: ")
            print("Your pin has been set successfully")
        else:
            print("There is already a pin")

        self.menu()

    def check_pin(self):
        pin = input("Enter your pin please: ")
        if pin == self.pin:
            return 1
        else:
            return 0

    def deposit(self):
        if self.pin == "":
            self.create_pin()

        if self.check_pin():
            amount = input("Please enter your deposit amount: ")
            self.balance += int(amount)
            print("Amount has been deposited successfully")
        else:
            print("You have entered wrong pin, please re-enter your pin")
            self.deposit()

        self.menu()

    def withdraw(self):
        if self.pin == "":
            self.create_pin()
        if self.check_pin():
            amount = int(input("Please enter your withdrawal amount or press 0 to return to menu: "))
            if amount == 0:
                pass
            elif amount < 0:
                print("Invalid amount")
            elif self.balance >= amount:
                self.balance -= amount
                print("Amount has been withdrawn successfully")
            else:
                print("Insufficient balance")
                self.withdraw()
        else:
            print("You have entered wrong pin")
            self.withdraw()

        self.menu()

    def check_balance(self):
        if self.pin == "":
            self.create_pin()
        if self.check_pin():
            print(f"Your current balance is : {self.balance}")
        else:
            print("You have entered wrong pin")
            self.check_balance()

        self.menu()

atm = ATM()
atm.menu()

#
#
#
#
#
#
bank_accounts = [BankAccount('John Pork', 1000)]

def menu():
    print("Vítejte v bance!")
    print("1 - seznam účtů")
    print("2 - přidat účet")
    print("3 - převod financí")
    print("4 - výběr financí")
    print("5 - vklad financí")
    print("6 - výběr automatů")

    choice = int(input("Zvolte akci:"))
    if choice == 1:
        print_accounts()
    elif choice == 2:
        add_account()
    elif choice == 3:
        transfer()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        deposit()
    elif choice == 6:
        main()
    else:
        print("Chybná akce, vyber znovu")

    menu()

def print_accounts():
    i = 0
    for bank_account in bank_accounts:
        print(f"{i+1} - {bank_account.account_holder}")
        i += 1

def add_account():
    name = input("Název účtu: ")
    bank_accounts.append(BankAccount(name))

def transfer():
    print("Dostupné účty:")
    print_accounts()

    index_from = input("Účet ze kterého:")
    index_to = input("Účet do kterého:")
    amount = input("Částka:")


    bank_accounts[int(index_to)-1].transfer(bank_accounts[int(index_from)-1], int(amount))

def withdraw():
    print("Dostupné účty:")
    print_accounts()

    index_from = input("Účet ze kterého:")
    amount = input("Částka:")


    bank_accounts[int(index_from)-1].withdraw(int(amount))

def deposit():
    print("Dostupné účty:")
    print_accounts()

    index_from = input("Účet do kterého:")
    amount = input("Částka:")


    bank_accounts[int(index_from)-1].deposit(int(amount))

def main():
    bank = ATM()

    print("Zvolte 1 pro ATM")

    choice = int(input("Zvolte akci:"))
    if choice == 1:
        bank.menu()
        return

menu()