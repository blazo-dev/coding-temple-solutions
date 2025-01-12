"""
Challenge: Create a BankAccount Class
Objective: Reinforce the concepts of instance attributes, the __init__ method, and instance methods.
Instructions:
Create a class named BankAccount with the following:
Instance attributes:
account_holder (string): The name of the account holder.
Balance (float): The current account balance, defaulting to 0.
Methods:
deposit(amount): Adds the given amount to the account balance and returns a message showing the new balance.
Withdraw(amount): Subtract the given amount from the balance if there are enough funds. Otherwise, it should return a message saying "Insufficient funds." If the withdrawal is successful, it should return the new balance.
Get_balance(): Returns a message displaying the current account balance."""


class BankAccount:

    def __init__(self, account_holder: str, balance: float = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than 0.")

        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance <= 0:
            return "Insufficient funds or invalid amount."

        self.balance -= amount

        print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        return self.balance

    def get_balance(self):
        print(f"{self.account_holder}, your current balance is {self.balance}.")
        return self.balance


bryan_account = BankAccount(account_holder="Bryan", balance=1000)

bryan_account.get_balance()
bryan_account.deposit(1000)
bryan_account.withdraw(1500)
