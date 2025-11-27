# Exercise 37: Bank Account Class with Methods
# Difficulty: Intermediate-
# Concepts: Classes, Methods, Encapsulation, Instance variables

"""
PROBLEM:
Create a BankAccount class with the following features:
- Attributes: account_holder, balance (starts at 0)
- Methods:
  - deposit(amount): adds money to the balance
  - withdraw(amount): removes money if sufficient balance exists
  - get_balance(): returns the current balance
  - transfer(amount, other_account): transfers money to another account

EXAMPLE:
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

account1.deposit(1000)
print(account1.get_balance())  # 1000

account1.withdraw(300)
print(account1.get_balance())  # 700

account1.transfer(200, account2)
print(account1.get_balance())  # 500
print(account2.get_balance())  # 200

HINTS:
1. Check if there's sufficient balance before withdrawing
2. A transfer is just a withdrawal from one account and deposit to another
3. Return True/False to indicate success or failure of operations

EXTENSION:
Add transaction history that records all deposits, withdrawals, and transfers with
timestamps. Add a method to print the transaction history.
"""

# Write your solution here
