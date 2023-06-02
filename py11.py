import random

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def generate_transaction_code(self):
        transaction_code = random.randint(1000, 9999)
        return transaction_code

    def deposit(self, amount):
        transaction_code = self.generate_transaction_code()
        self.balance += amount
        print(f"Deposit of {amount} successful. Transaction code: {transaction_code}")

    def withdraw(self, amount):
        if amount <= self.balance:
            transaction_code = self.generate_transaction_code()
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Transaction code: {transaction_code}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

account = BankAccount("1234567890", "Ben Tennyson")
account.display_balance()

account.deposit(1000)
account.display_balance()

account.withdraw(500)
account.display_balance()

account.withdraw(1000) 
account.display_balance()
