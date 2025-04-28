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

    choice = int(input("Zvolte akci:"))
    if choice == 1:
        print_accounts()
    elif choice == 2:
        add_account()
    elif choice == 3:
        transfer()
    elif choice == 4:
        # TODO: výběr
        print("")
    elif choice == 5:
        # TODO: vklad
        print("")
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

menu()