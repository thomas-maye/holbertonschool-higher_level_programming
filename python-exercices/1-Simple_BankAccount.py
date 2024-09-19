#!/usr/bin/python3
"""Implementing a Simple BankAccount Class in Python"""


#!/usr/bin/python3
"""Implementing a Simple BankAccount Class in Python"""

class BankAccount:
    def __init__(self, account_number, owner):
        self._account_number = account_number
        self.owner = owner
        self._balance = 0.0

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, str) and value:
            self._owner = value
        else:
            raise ValueError("Owner name must be a non-empty string")

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate):
        super().__init__(account_number, owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

# Test cases for SavingsAccount
print("\n=== SavingsAccount Test ===")
savings = SavingsAccount("987654321", "Thomas", 0.03)
print(f"Account Number: {savings.account_number}")
print(f"Owner: {savings.owner}")
print(f"Interest Rate: {savings.interest_rate * 100}%")
savings.deposit(31000)
savings.withdraw(10000)
print(f"Initial Balance: ${savings.get_balance():.2f}")

# Deposit and apply interest
savings.deposit(31000)
savings.apply_interest()
print(f"Final Balance: ${savings.get_balance():.2f}")
