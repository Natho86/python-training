# Exercise 50: Personal Finance Tracker (Capstone Project)
# Difficulty: Intermediate
# Concepts: OOP, JSON, datetime, Collections, Decorators, Data analysis, All Phase 3 concepts

"""
PROBLEM:
Create a comprehensive personal finance tracker that combines all concepts from Phase 3:

Features:
1. Track income and expenses with categories
2. Set and monitor monthly budgets
3. Generate financial reports (daily, monthly, yearly)
4. Visualize spending patterns with ASCII charts
5. Calculate savings rate and financial trends
6. Export reports to JSON and text formats
7. Use decorators for logging transactions
8. Support multiple currencies with conversion

Classes:
- Transaction (income/expense with amount, category, date, description)
- Budget (category-wise monthly budgets)
- Account (manages transactions and balances)
- FinanceTracker (main application class)

EXAMPLE:
tracker = FinanceTracker()

# Add transactions
tracker.add_income("Salary", 5000, "2024-01-01")
tracker.add_expense("Rent", 1200, "Housing", "2024-01-05")
tracker.add_expense("Groceries", 350, "Food", "2024-01-10")

# Set budgets
tracker.set_budget("Food", 500)
tracker.set_budget("Housing", 1500)

# Generate reports
tracker.monthly_report("2024-01")
tracker.budget_status()
tracker.savings_analysis()

HINTS:
1. Use enums or constants for transaction types (INCOME/EXPENSE)
2. Store transactions chronologically
3. Use defaultdict for category grouping
4. Calculate totals with sum() and filter()
5. Use decorators to log all financial operations
6. Save everything to JSON for persistence

EXTENSION:
Add recurring transactions (monthly salary, rent).
Add financial goals and progress tracking.
Create a simple CLI menu for interactive use.
Add data export to CSV format.
"""

# Write your solution here
