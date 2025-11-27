"""
Expense Tracker - Intermediate Python Project
==============================================
A comprehensive expense tracking application with categories, reports, and data persistence.

Features:
- Add, edit, and delete expenses
- Categorize expenses
- View reports by category and date range
- Monthly summaries and statistics
- JSON data persistence
- Input validation and error handling

Concepts: OOP, JSON, datetime, file I/O, dictionaries, list comprehensions, error handling
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict


class Expense:
    """Represents a single expense."""

    def __init__(self, amount, category, description, date=None, expense_id=None):
        """Initialize an expense."""
        self.id = expense_id if expense_id else datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert expense to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

    def __str__(self):
        """String representation of expense."""
        return f"{self.date} | ${self.amount:6.2f} | {self.category:15} | {self.description}"


class ExpenseTracker:
    """Main expense tracker application."""

    CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Utilities',
                  'Healthcare', 'Shopping', 'Other']

    def __init__(self, filename='expenses.json'):
        """Initialize the expense tracker."""
        self.filename = filename
        self.expenses = []
        self.load_data()

    def load_data(self):
        """Load expenses from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.expenses = [
                        Expense(
                            e['amount'],
                            e['category'],
                            e['description'],
                            e['date'],
                            e['id']
                        ) for e in data
                    ]
                print(f"Loaded {len(self.expenses)} expenses from {self.filename}")
            else:
                print("No existing data file found. Starting fresh!")
        except json.JSONDecodeError:
            print("Error reading data file. Starting with empty tracker.")
            self.expenses = []
        except Exception as e:
            print(f"Error loading data: {e}")
            self.expenses = []

    def save_data(self):
        """Save expenses to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([e.to_dict() for e in self.expenses], f, indent=2)
            print(f"Data saved to {self.filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_expense(self):
        """Add a new expense."""
        print("\n=== Add New Expense ===")

        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Invalid amount!")
            return

        # Show categories
        print("\nCategories:")
        for i, cat in enumerate(self.CATEGORIES, 1):
            print(f"{i}. {cat}")

        try:
            cat_choice = int(input("Select category (1-7): "))
            if 1 <= cat_choice <= len(self.CATEGORIES):
                category = self.CATEGORIES[cat_choice - 1]
            else:
                print("Invalid category!")
                return
        except ValueError:
            print("Invalid input!")
            return

        description = input("Description: ").strip()
        if not description:
            print("Description cannot be empty!")
            return

        date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
                date = date_input
            except ValueError:
                print("Invalid date format! Using today's date.")
                date = None
        else:
            date = None

        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        self.save_data()
        print(f"\n✓ Expense added successfully! (ID: {expense.id})")

    def view_all_expenses(self):
        """View all expenses."""
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        print(f"\n=== All Expenses ({len(self.expenses)} total) ===")
        print("-" * 80)
        print(f"{'Date':<12} | {'Amount':>8} | {'Category':<15} | Description")
        print("-" * 80)

        total = 0
        for expense in sorted(self.expenses, key=lambda x: x.date, reverse=True):
            print(expense)
            total += expense.amount

        print("-" * 80)
        print(f"{'TOTAL:':<12} | ${total:>7.2f}")

    def view_by_category(self):
        """View expenses grouped by category."""
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        print("\n=== Expenses by Category ===")

        category_totals = defaultdict(list)
        for expense in self.expenses:
            category_totals[expense.category].append(expense)

        grand_total = 0
        for category in sorted(category_totals.keys()):
            expenses = category_totals[category]
            category_total = sum(e.amount for e in expenses)
            grand_total += category_total

            print(f"\n{category} (${category_total:.2f}):")
            for expense in sorted(expenses, key=lambda x: x.date, reverse=True):
                print(f"  {expense.date} | ${expense.amount:6.2f} | {expense.description}")

        print(f"\nGrand Total: ${grand_total:.2f}")

    def monthly_report(self):
        """Generate monthly expense report."""
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        print("\n=== Monthly Report ===")

        # Group by month
        monthly_data = defaultdict(lambda: defaultdict(float))

        for expense in self.expenses:
            month = expense.date[:7]  # YYYY-MM
            monthly_data[month][expense.category] += expense.amount

        # Display report
        for month in sorted(monthly_data.keys(), reverse=True):
            print(f"\n{month}:")
            categories = monthly_data[month]
            month_total = sum(categories.values())

            for category in sorted(categories.keys()):
                amount = categories[category]
                percentage = (amount / month_total) * 100
                print(f"  {category:<15}: ${amount:8.2f} ({percentage:5.1f}%)")

            print(f"  {'TOTAL':<15}: ${month_total:8.2f}")

    def delete_expense(self):
        """Delete an expense by ID."""
        if not self.expenses:
            print("\nNo expenses to delete!")
            return

        # Show recent expenses
        print("\nRecent expenses:")
        for expense in sorted(self.expenses, key=lambda x: x.date, reverse=True)[:10]:
            print(f"ID: {expense.id} | {expense}")

        expense_id = input("\nEnter expense ID to delete (or 'cancel'): ").strip()

        if expense_id.lower() == 'cancel':
            return

        for i, expense in enumerate(self.expenses):
            if expense.id == expense_id:
                print(f"\nDeleting: {expense}")
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    self.expenses.pop(i)
                    self.save_data()
                    print("✓ Expense deleted!")
                return

        print("Expense ID not found!")

    def statistics(self):
        """Show expense statistics."""
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return

        print("\n=== Statistics ===")

        amounts = [e.amount for e in self.expenses]
        total = sum(amounts)
        average = total / len(amounts)

        print(f"Total Expenses: ${total:.2f}")
        print(f"Number of Transactions: {len(self.expenses)}")
        print(f"Average Expense: ${average:.2f}")
        print(f"Largest Expense: ${max(amounts):.2f}")
        print(f"Smallest Expense: ${min(amounts):.2f}")

        # Category breakdown
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount

        print("\nSpending by Category:")
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            bar = '█' * int(percentage / 2)
            print(f"  {category:<15}: ${amount:8.2f} ({percentage:5.1f}%) {bar}")

    def run(self):
        """Run the main application loop."""
        print("\n" + "="*50)
        print("         EXPENSE TRACKER")
        print("="*50)

        while True:
            print("\n=== Main Menu ===")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. View by Category")
            print("4. Monthly Report")
            print("5. Statistics")
            print("6. Delete Expense")
            print("7. Exit")

            choice = input("\nEnter choice (1-7): ").strip()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_all_expenses()
            elif choice == '3':
                self.view_by_category()
            elif choice == '4':
                self.monthly_report()
            elif choice == '5':
                self.statistics()
            elif choice == '6':
                self.delete_expense()
            elif choice == '7':
                print("\nThank you for using Expense Tracker!")
                break
            else:
                print("\nInvalid choice! Please enter 1-7.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
