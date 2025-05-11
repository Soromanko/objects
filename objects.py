from codecs import backslashreplace_errors
from operator import index


class BankAccount:
    def __init__(self, account_holder, pin, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
        self.__pin = pin

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

    def check_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

class ATM:
    def __init__(self, accounts):
        self.accounts = accounts
        self.current_account = False
        self.balance = 0

    def menu(self):
        print("""
            0. Enter 0 to exit
            1. Enter 1 to deposit
            2. Enter 2 to withdraw
            3. Enter 3 to check balance
        """)
        user_input = int(input("Vyber si možnost: "))

        if user_input == 1:
            self.deposit()
        elif user_input == 2:
            self.withdraw()
        elif user_input == 3:
            self.check_balance()
        elif user_input < 0 or user_input > 4:
            print("Please Enter a valid input")

        return user_input

    def login(self):
        print("Prosím přihlaste se do svého účtu: ")
        i = 0
        for account in self.accounts:
            print(f"{i + 1} - {account.account_holder}")
            i += 1

        account_choice = int(input("Vyberte účet: ")) - 1

        if account_choice < 0 or account_choice >= i:
            print("Error")
            return self.login()

        selected_account = self.accounts[account_choice]
        pin = input("Zadejte PIN: ")

        if selected_account.check_pin(pin):
            self.current_account = selected_account
            print(f"Vítejte {selected_account.account_holder}")
            self.menu()
        else:
            print("Nesprávně zadaný PIN, zkuste to znovu prosím")
            return self.login

    def deposit(self):
        if self.current_account:
            amount = int(input("Please enter your deposit amount: "))
            self.current_account.deposit(amount)
            print("Amount has been deposited successfully")
        else:
            print("You have entered wrong pin, please re-enter your pin")
            self.login()
            return

        self.menu()

    def withdraw(self):
        if self.current_account:
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
                self.current_account.withdraw(amount)
        else:
            print("You have entered wrong pin")
            self.login()
            return

        self.menu()

    def check_balance(self):
        if self.current_account:
            print(f"Your current balance is : {self.current_account.get_balance()}")
        else:
            print("You have entered wrong pin")
            self.login()
            return

        self.menu()


#
#
#
#
#
#
bank_accounts = [BankAccount('John Pork', '1234', 1000)]

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
    pin = input("Zadejte nový pin: ")
    bank_accounts.append(BankAccount(name, pin))

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
    print("Zvolte 1 pro ATM")

    choice = int(input("Zvolte akci:"))
    if choice == 1:
        atm = ATM(bank_accounts)
        atm.menu()

menu()