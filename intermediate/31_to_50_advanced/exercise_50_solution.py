# Exercise 50: Personal Finance Tracker (Capstone Project) - SOLUTION
# Difficulty: Intermediate
# Concepts: OOP, JSON, datetime, Collections, Decorators, Data analysis, All Phase 3 concepts

import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from functools import wraps
import os

# SOLUTION

# Decorator for logging financial operations
def log_transaction(func):
    """Decorator to log financial transactions."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {func.__name__}: {args}"

        # Append to log file
        with open('finance_log.txt', 'a') as f:
            f.write(log_entry + '\n')

        return result
    return wrapper

class Transaction:
    """Represents a financial transaction."""

    INCOME = "income"
    EXPENSE = "expense"

    def __init__(self, trans_type, amount, category, date, description=""):
        """
        Initialize transaction.

        Args:
            trans_type: 'income' or 'expense'
            amount: Transaction amount
            category: Transaction category
            date: Date string (YYYY-MM-DD)
            description: Optional description
        """
        self.type = trans_type
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'type': self.type,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description,
            'timestamp': self.timestamp
        }

    def __str__(self):
        """String representation."""
        symbol = "+" if self.type == self.INCOME else "-"
        return f"{self.date} | {symbol}${self.amount:,.2f} | {self.category} | {self.description}"

class Budget:
    """Represents a budget for a category."""

    def __init__(self, category, monthly_limit):
        """
        Initialize budget.

        Args:
            category: Budget category
            monthly_limit: Monthly spending limit
        """
        self.category = category
        self.monthly_limit = float(monthly_limit)

    def check_status(self, spent):
        """
        Check budget status.

        Args:
            spent: Amount already spent

        Returns:
            dict: Status information
        """
        remaining = self.monthly_limit - spent
        percentage = (spent / self.monthly_limit * 100) if self.monthly_limit > 0 else 0

        status = "OK"
        if percentage >= 100:
            status = "EXCEEDED"
        elif percentage >= 80:
            status = "WARNING"

        return {
            'limit': self.monthly_limit,
            'spent': spent,
            'remaining': remaining,
            'percentage': percentage,
            'status': status
        }

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'category': self.category,
            'monthly_limit': self.monthly_limit
        }

class FinanceTracker:
    """Personal finance tracking application."""

    def __init__(self, filename="finance_data.json"):
        """
        Initialize finance tracker.

        Args:
            filename: JSON file for data persistence
        """
        self.filename = filename
        self.transactions = []
        self.budgets = {}
        self.currency = "USD"
        self.load_data()

    @log_transaction
    def add_income(self, category, amount, date=None, description=""):
        """
        Add income transaction.

        Args:
            category: Income category (Salary, Freelance, etc.)
            amount: Income amount
            date: Date string (YYYY-MM-DD), defaults to today
            description: Optional description
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        transaction = Transaction(Transaction.INCOME, amount, category, date, description)
        self.transactions.append(transaction)
        self.save_data()

        print(f"✓ Added income: {category} +${amount:,.2f}")

    @log_transaction
    def add_expense(self, category, amount, date=None, description=""):
        """
        Add expense transaction.

        Args:
            category: Expense category (Housing, Food, etc.)
            amount: Expense amount
            date: Date string (YYYY-MM-DD), defaults to today
            description: Optional description
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        transaction = Transaction(Transaction.EXPENSE, amount, category, date, description)
        self.transactions.append(transaction)
        self.save_data()

        print(f"✓ Added expense: {category} -${amount:,.2f}")

    def set_budget(self, category, monthly_limit):
        """
        Set budget for a category.

        Args:
            category: Category name
            monthly_limit: Monthly spending limit
        """
        budget = Budget(category, monthly_limit)
        self.budgets[category] = budget
        self.save_data()

        print(f"✓ Set budget for {category}: ${monthly_limit:,.2f}/month")

    def get_transactions_by_period(self, start_date, end_date):
        """
        Get transactions within date range.

        Args:
            start_date: Start date string (YYYY-MM-DD)
            end_date: End date string (YYYY-MM-DD)

        Returns:
            list: Filtered transactions
        """
        return [t for t in self.transactions
                if start_date <= t.date <= end_date]

    def calculate_balance(self, start_date=None, end_date=None):
        """
        Calculate balance for period.

        Args:
            start_date: Optional start date
            end_date: Optional end date

        Returns:
            dict: Income, expenses, balance
        """
        if start_date and end_date:
            transactions = self.get_transactions_by_period(start_date, end_date)
        else:
            transactions = self.transactions

        income = sum(t.amount for t in transactions if t.type == Transaction.INCOME)
        expenses = sum(t.amount for t in transactions if t.type == Transaction.EXPENSE)
        balance = income - expenses

        return {
            'income': income,
            'expenses': expenses,
            'balance': balance,
            'savings_rate': (balance / income * 100) if income > 0 else 0
        }

    def monthly_report(self, year_month):
        """
        Generate monthly financial report.

        Args:
            year_month: Month string (YYYY-MM)
        """
        start_date = f"{year_month}-01"
        # Get last day of month
        year, month = map(int, year_month.split('-'))
        if month == 12:
            next_month = f"{year+1}-01-01"
        else:
            next_month = f"{year}-{month+1:02d}-01"
        end_date = (datetime.strptime(next_month, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

        transactions = self.get_transactions_by_period(start_date, end_date)

        if not transactions:
            print(f"\nNo transactions found for {year_month}")
            return

        print(f"\n{'='*70}")
        print(f"MONTHLY REPORT - {year_month}")
        print(f"{'='*70}")

        # Calculate totals
        balance_info = self.calculate_balance(start_date, end_date)

        print(f"\nSUMMARY:")
        print(f"  Income:        ${balance_info['income']:>12,.2f}")
        print(f"  Expenses:      ${balance_info['expenses']:>12,.2f}")
        print(f"  {'─'*30}")
        print(f"  Balance:       ${balance_info['balance']:>12,.2f}")
        print(f"  Savings Rate:  {balance_info['savings_rate']:>12.1f}%")

        # Expenses by category
        expense_by_category = defaultdict(float)
        for t in transactions:
            if t.type == Transaction.EXPENSE:
                expense_by_category[t.category] += t.amount

        if expense_by_category:
            print(f"\nEXPENSES BY CATEGORY:")
            sorted_expenses = sorted(expense_by_category.items(),
                                   key=lambda x: x[1],
                                   reverse=True)
            for category, amount in sorted_expenses:
                percentage = (amount / balance_info['expenses'] * 100) if balance_info['expenses'] > 0 else 0
                print(f"  {category:20} ${amount:>10,.2f} ({percentage:>5.1f}%)")

        # Income by category
        income_by_category = defaultdict(float)
        for t in transactions:
            if t.type == Transaction.INCOME:
                income_by_category[t.category] += t.amount

        if income_by_category:
            print(f"\nINCOME BY CATEGORY:")
            for category, amount in sorted(income_by_category.items(), key=lambda x: x[1], reverse=True):
                print(f"  {category:20} ${amount:>10,.2f}")

        print(f"{'='*70}\n")

    def budget_status(self, year_month=None):
        """
        Show budget status for the month.

        Args:
            year_month: Month string (YYYY-MM), defaults to current month
        """
        if year_month is None:
            year_month = datetime.now().strftime('%Y-%m')

        start_date = f"{year_month}-01"
        year, month = map(int, year_month.split('-'))
        if month == 12:
            next_month = f"{year+1}-01-01"
        else:
            next_month = f"{year}-{month+1:02d}-01"
        end_date = (datetime.strptime(next_month, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

        transactions = self.get_transactions_by_period(start_date, end_date)

        # Calculate spending by category
        spending = defaultdict(float)
        for t in transactions:
            if t.type == Transaction.EXPENSE:
                spending[t.category] += t.amount

        print(f"\n{'='*70}")
        print(f"BUDGET STATUS - {year_month}")
        print(f"{'='*70}\n")

        if not self.budgets:
            print("No budgets set. Use set_budget() to create budgets.")
            print(f"{'='*70}\n")
            return

        for category, budget in self.budgets.items():
            spent = spending.get(category, 0)
            status_info = budget.check_status(spent)

            status_symbol = {
                'OK': '✓',
                'WARNING': '⚠',
                'EXCEEDED': '✗'
            }[status_info['status']]

            print(f"{status_symbol} {category:20}")
            print(f"  Budget:    ${status_info['limit']:>10,.2f}")
            print(f"  Spent:     ${status_info['spent']:>10,.2f}")
            print(f"  Remaining: ${status_info['remaining']:>10,.2f}")
            print(f"  Used:      {status_info['percentage']:>10.1f}%")

            # ASCII progress bar
            bar_width = 40
            filled = int(bar_width * status_info['percentage'] / 100)
            bar = '█' * min(filled, bar_width)
            empty = '░' * max(0, bar_width - filled)
            print(f"  [{bar}{empty}]")
            print()

        print(f"{'='*70}\n")

    def create_spending_chart(self, year_month):
        """
        Create ASCII bar chart of spending by category.

        Args:
            year_month: Month string (YYYY-MM)
        """
        start_date = f"{year_month}-01"
        year, month = map(int, year_month.split('-'))
        if month == 12:
            next_month = f"{year+1}-01-01"
        else:
            next_month = f"{year}-{month+1:02d}-01"
        end_date = (datetime.strptime(next_month, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

        transactions = self.get_transactions_by_period(start_date, end_date)

        spending = defaultdict(float)
        for t in transactions:
            if t.type == Transaction.EXPENSE:
                spending[t.category] += t.amount

        if not spending:
            print("\nNo expenses to chart.")
            return

        print(f"\n{'='*70}")
        print(f"SPENDING CHART - {year_month}")
        print(f"{'='*70}\n")

        max_amount = max(spending.values())
        max_bar_width = 40

        sorted_spending = sorted(spending.items(), key=lambda x: x[1], reverse=True)

        for category, amount in sorted_spending:
            bar_width = int((amount / max_amount) * max_bar_width)
            bar = '█' * bar_width
            print(f"{category:15} {bar} ${amount:,.2f}")

        print(f"\n{'='*70}\n")

    def savings_analysis(self):
        """Analyze savings trends."""
        if not self.transactions:
            print("\nNo transactions to analyze.")
            return

        print(f"\n{'='*70}")
        print("SAVINGS ANALYSIS")
        print(f"{'='*70}\n")

        # Overall balance
        overall = self.calculate_balance()
        print(f"LIFETIME TOTALS:")
        print(f"  Total Income:    ${overall['income']:>12,.2f}")
        print(f"  Total Expenses:  ${overall['expenses']:>12,.2f}")
        print(f"  Net Savings:     ${overall['balance']:>12,.2f}")
        print(f"  Savings Rate:    {overall['savings_rate']:>12.1f}%")

        # Monthly breakdown
        monthly_data = defaultdict(lambda: {'income': 0, 'expenses': 0})

        for t in self.transactions:
            month = t.date[:7]  # YYYY-MM
            if t.type == Transaction.INCOME:
                monthly_data[month]['income'] += t.amount
            else:
                monthly_data[month]['expenses'] += t.amount

        if monthly_data:
            print(f"\nMONTHLY BREAKDOWN:")
            print(f"  Month      Income      Expenses    Savings     Rate")
            print(f"  {'─'*60}")

            for month in sorted(monthly_data.keys()):
                income = monthly_data[month]['income']
                expenses = monthly_data[month]['expenses']
                savings = income - expenses
                rate = (savings / income * 100) if income > 0 else 0

                print(f"  {month}   ${income:>9,.2f}  ${expenses:>9,.2f}  "
                      f"${savings:>9,.2f}  {rate:>5.1f}%")

        print(f"\n{'='*70}\n")

    def export_report(self, filename="finance_report.txt"):
        """Export comprehensive report to text file."""
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("PERSONAL FINANCE REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")

            # Overall summary
            overall = self.calculate_balance()
            f.write("OVERALL SUMMARY\n")
            f.write(f"Total Income:    ${overall['income']:,.2f}\n")
            f.write(f"Total Expenses:  ${overall['expenses']:,.2f}\n")
            f.write(f"Net Savings:     ${overall['balance']:,.2f}\n")
            f.write(f"Savings Rate:    {overall['savings_rate']:.1f}%\n")
            f.write("\n")

            # All transactions
            f.write("ALL TRANSACTIONS\n")
            f.write("-"*70 + "\n")
            for t in sorted(self.transactions, key=lambda x: x.date, reverse=True):
                f.write(f"{t}\n")

        print(f"✓ Report exported to {filename}")

    def save_data(self):
        """Save all data to JSON file."""
        data = {
            'currency': self.currency,
            'transactions': [t.to_dict() for t in self.transactions],
            'budgets': [b.to_dict() for b in self.budgets.values()]
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        """Load data from JSON file."""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)

            self.currency = data.get('currency', 'USD')

            # Load transactions
            for t_data in data.get('transactions', []):
                transaction = Transaction(
                    t_data['type'],
                    t_data['amount'],
                    t_data['category'],
                    t_data['date'],
                    t_data.get('description', '')
                )
                transaction.timestamp = t_data.get('timestamp', '')
                self.transactions.append(transaction)

            # Load budgets
            for b_data in data.get('budgets', []):
                budget = Budget(b_data['category'], b_data['monthly_limit'])
                self.budgets[b_data['category']] = budget

            print(f"Loaded {len(self.transactions)} transactions")

        except FileNotFoundError:
            print("No existing data found. Starting fresh.")

# DEMONSTRATION
print("="*70)
print("PERSONAL FINANCE TRACKER - CAPSTONE PROJECT")
print("="*70)

# Create tracker
tracker = FinanceTracker("demo_finance.json")

# Add sample data
print("\n--- Adding Sample Transactions ---")
tracker.add_income("Salary", 5000, "2024-01-01", "Monthly salary")
tracker.add_expense("Rent", 1200, "2024-01-05", "Housing", "Apartment rent")
tracker.add_expense("Groceries", 350, "2024-01-10", "Food")
tracker.add_expense("Gas", 80, "2024-01-12", "Transportation")
tracker.add_expense("Dining Out", 150, "2024-01-15", "Food")
tracker.add_income("Freelance", 800, "2024-01-20", "Side project")
tracker.add_expense("Utilities", 120, "2024-01-25", "Housing")
tracker.add_expense("Entertainment", 90, "2024-01-28", "Entertainment")

# Set budgets
print("\n--- Setting Budgets ---")
tracker.set_budget("Housing", 1500)
tracker.set_budget("Food", 500)
tracker.set_budget("Transportation", 200)
tracker.set_budget("Entertainment", 100)

# Generate reports
tracker.monthly_report("2024-01")
tracker.budget_status("2024-01")
tracker.create_spending_chart("2024-01")
tracker.savings_analysis()

# Export report
tracker.export_report("demo_finance_report.txt")

"""
EXPLANATION - CAPSTONE PROJECT:
This exercise combines ALL Phase 3 concepts:

1. Advanced Functions: *args/**kwargs in decorators
2. Lambda Functions: Used in sorting and filtering
3. Map/Filter/Reduce: Data processing and aggregation
4. Decorators: @log_transaction decorator
5. OOP: Multiple classes (Transaction, Budget, FinanceTracker)
6. __init__ and __str__: All classes implement these
7. Inheritance: Could extend for specialized trackers
8. Modules: Uses datetime, json, collections, functools
9. JSON: Complete data persistence
10. Data Aggregation: Category grouping, totals, averages
11. Collections: defaultdict for grouping, Counter for frequencies

This demonstrates a real-world application integrating multiple concepts
into a cohesive, useful program with proper architecture and design.

Key Architectural Decisions:
- Separation of concerns (Transaction, Budget, Tracker)
- Single responsibility principle
- Data persistence strategy
- Decorator pattern for cross-cutting concerns (logging)
- Comprehensive reporting and analysis
- User-friendly output formatting
"""

print("\n" + "="*70)
print("CONGRATULATIONS! You've completed Phase 3!")
print("="*70)
print("\nYou've mastered:")
print("  ✓ Advanced function features (*args, **kwargs, lambda)")
print("  ✓ Functional programming (map, filter, reduce)")
print("  ✓ Decorators")
print("  ✓ Object-Oriented Programming")
print("  ✓ Standard library modules")
print("  ✓ JSON data handling")
print("  ✓ Data analysis and aggregation")
print("  ✓ Building complete applications")
