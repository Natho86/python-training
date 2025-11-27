# Exercise 37: Bank Account Class with Methods - SOLUTION
# Difficulty: Intermediate-
# Concepts: Classes, Methods, Encapsulation, Instance variables

# SOLUTION
class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, account_holder):
        """
        Initialize bank account.

        Args:
            account_holder: Name of the account holder
        """
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit

        Returns:
            bool: True if successful
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        else:
            print("Deposit amount must be positive!")
            return False

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount: Amount to withdraw

        Returns:
            bool: True if successful, False if insufficient funds
        """
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False

        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance:.2f}")
            return False

        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def transfer(self, amount, other_account):
        """
        Transfer money to another account.

        Args:
            amount: Amount to transfer
            other_account: Destination BankAccount object

        Returns:
            bool: True if successful
        """
        if amount <= 0:
            print("Transfer amount must be positive!")
            return False

        if amount > self.balance:
            print(f"Insufficient funds for transfer! Balance: ${self.balance:.2f}")
            return False

        # Perform the transfer
        self.balance -= amount
        other_account.balance += amount
        print(f"Transferred ${amount:.2f} to {other_account.account_holder}")
        print(f"Your new balance: ${self.balance:.2f}")
        return True

    def __str__(self):
        """String representation of account."""
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

# Test the BankAccount class
print("=== Testing Bank Account ===")
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

print(f"\nCreated accounts:")
print(account1)
print(account2)

print(f"\n--- Deposits ---")
account1.deposit(1000)
account2.deposit(500)

print(f"\n--- Withdrawals ---")
account1.withdraw(300)
account1.withdraw(800)  # Should fail - insufficient funds

print(f"\n--- Transfer ---")
account1.transfer(200, account2)

print(f"\n--- Final Balances ---")
print(account1)
print(account2)

"""
EXPLANATION:
1. __init__ creates the account with holder name and zero balance
2. Each method returns True/False to indicate success
3. We validate amounts before performing operations (positive, sufficient funds)
4. transfer() is a combination of withdraw and deposit
5. __str__ provides a readable representation when printing

Key Concepts:
- Methods can call other methods (transfer uses balance checks)
- Instance variables (self.balance) persist across method calls
- Validation ensures data integrity (can't overdraw)
- Methods can interact with other instances (transfer to other_account)
- Return values let callers know if operations succeeded
"""

# Extension solution: Transaction history
print("\n--- EXTENSION SOLUTION ---")

from datetime import datetime

class BankAccountWithHistory:
    """Bank account with transaction history tracking."""

    def __init__(self, account_holder):
        """Initialize account with transaction history."""
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def _record_transaction(self, transaction_type, amount, note=""):
        """
        Record a transaction (private method).

        Args:
            transaction_type: Type of transaction (deposit, withdrawal, transfer)
            amount: Transaction amount
            note: Additional information
        """
        transaction = {
            'timestamp': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': self.balance,
            'note': note
        }
        self.transactions.append(transaction)

    def deposit(self, amount):
        """Deposit with transaction recording."""
        if amount > 0:
            self.balance += amount
            self._record_transaction('deposit', amount)
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        else:
            print("Deposit amount must be positive!")
            return False

    def withdraw(self, amount):
        """Withdraw with transaction recording."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False

        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance:.2f}")
            return False

        self.balance -= amount
        self._record_transaction('withdrawal', amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def transfer(self, amount, other_account):
        """Transfer with transaction recording."""
        if amount <= 0:
            print("Transfer amount must be positive!")
            return False

        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance:.2f}")
            return False

        self.balance -= amount
        other_account.balance += amount

        # Record for both accounts
        self._record_transaction('transfer_out', amount,
                                 f"To {other_account.account_holder}")
        other_account._record_transaction('transfer_in', amount,
                                          f"From {self.account_holder}")

        print(f"Transferred ${amount:.2f} to {other_account.account_holder}")
        return True

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def print_history(self):
        """Print transaction history."""
        print(f"\n=== Transaction History for {self.account_holder} ===")
        if not self.transactions:
            print("No transactions yet.")
            return

        for i, trans in enumerate(self.transactions, 1):
            timestamp = trans['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            trans_type = trans['type'].replace('_', ' ').title()
            amount = trans['amount']
            balance = trans['balance']
            note = trans['note']

            print(f"\n{i}. {timestamp}")
            print(f"   Type: {trans_type}")
            print(f"   Amount: ${amount:.2f}")
            print(f"   Balance After: ${balance:.2f}")
            if note:
                print(f"   Note: {note}")

    def __str__(self):
        """String representation."""
        return f"{self.account_holder}: ${self.balance:.2f} ({len(self.transactions)} transactions)"

# Test enhanced account
print("\nTesting Enhanced Bank Account:")
alice = BankAccountWithHistory("Alice")
bob = BankAccountWithHistory("Bob")

alice.deposit(1000)
alice.withdraw(200)
alice.transfer(300, bob)
bob.deposit(100)

alice.print_history()
bob.print_history()

print(f"\n{alice}")
print(f"{bob}")
