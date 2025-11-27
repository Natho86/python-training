#!/usr/bin/env python3
"""
Expense Tracker - Main Application
A command-line application for tracking personal expenses.
"""

import sys
from datetime import datetime
from expense_manager import ExpenseManager


class ExpenseTrackerApp:
    """Main application class for the Expense Tracker."""

    def __init__(self):
        """Initialize the application."""
        self.manager = ExpenseManager()
        self.running = True

    def run(self):
        """Run the main application loop."""
        self.display_welcome()

        while self.running:
            self.display_menu()
            choice = input("\nEnter your choice (1-10): ").strip()
            self.handle_choice(choice)

    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "="*60)
        print(" "*15 + "EXPENSE TRACKER")
        print("="*60)
        print(f"\nTotal Expenses: {len(self.manager.expenses)}")
        print(f"Total Amount: ${self.manager.get_total():.2f}")
        print("="*60)

    def display_menu(self):
        """Display the main menu."""
        print("\n" + "-"*60)
        print("MAIN MENU")
        print("-"*60)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Expenses by Date Range")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. View Statistics")
        print("8. Export to CSV")
        print("9. Search Expenses")
        print("10. Exit")
        print("-"*60)

    def handle_choice(self, choice: str):
        """
        Handle user menu choice.

        Args:
            choice: User's menu selection
        """
        actions = {
            '1': self.add_expense,
            '2': self.view_all_expenses,
            '3': self.view_by_category,
            '4': self.view_by_date_range,
            '5': self.update_expense,
            '6': self.delete_expense,
            '7': self.view_statistics,
            '8': self.export_to_csv,
            '9': self.search_expenses,
            '10': self.exit_app
        }

        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"\n[ERROR] {e}")
                input("\nPress Enter to continue...")
        else:
            print("\n[ERROR] Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

    def add_expense(self):
        """Add a new expense."""
        print("\n" + "="*60)
        print("ADD NEW EXPENSE")
        print("="*60)

        try:
            # Get amount
            amount_str = input("Amount: $").strip()
            amount = float(amount_str)

            # Get category
            print(f"\nExisting categories: {', '.join(self.manager.get_all_categories()) or 'None'}")
            category = input("Category: ").strip()
            if not category:
                raise ValueError("Category cannot be empty")

            # Get description
            description = input("Description (optional): ").strip()

            # Get date
            date_str = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
            date = date_str if date_str else None

            # Get tags
            print("\nExisting tags: " + (', '.join(self.manager.get_all_tags()) or 'None'))
            tags_str = input("Tags (comma-separated, optional): ").strip()
            tags = [tag.strip() for tag in tags_str.split(',')] if tags_str else []

            # Add expense
            expense = self.manager.add_expense(
                amount=amount,
                category=category,
                description=description,
                date=date,
                tags=tags
            )

            print(f"\n[SUCCESS] Expense added successfully!")
            print(f"\n{expense}")

        except ValueError as e:
            print(f"\n[ERROR] {e}")

        input("\nPress Enter to continue...")

    def view_all_expenses(self):
        """View all expenses."""
        print("\n" + "="*60)
        print("ALL EXPENSES")
        print("="*60)

        expenses = self.manager.expenses
        if not expenses:
            print("\nNo expenses found.")
        else:
            self.display_expenses(expenses)
            print(f"\nTotal: ${self.manager.get_total():.2f}")

        input("\nPress Enter to continue...")

    def view_by_category(self):
        """View expenses by category."""
        print("\n" + "="*60)
        print("VIEW BY CATEGORY")
        print("="*60)

        categories = self.manager.get_all_categories()
        if not categories:
            print("\nNo categories found.")
            input("\nPress Enter to continue...")
            return

        print("\nAvailable categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        choice = input("\nEnter category name: ").strip()
        expenses = self.manager.get_expenses(category=choice)

        if not expenses:
            print(f"\nNo expenses found in category '{choice}'.")
        else:
            print(f"\nExpenses in category '{choice}':")
            self.display_expenses(expenses)
            print(f"\nTotal: ${self.manager.get_total(category=choice):.2f}")

        input("\nPress Enter to continue...")

    def view_by_date_range(self):
        """View expenses by date range."""
        print("\n" + "="*60)
        print("VIEW BY DATE RANGE")
        print("="*60)

        try:
            start_date = input("Start date (YYYY-MM-DD): ").strip()
            end_date = input("End date (YYYY-MM-DD): ").strip()

            # Validate dates
            datetime.strptime(start_date, '%Y-%m-%d')
            datetime.strptime(end_date, '%Y-%m-%d')

            expenses = self.manager.get_expenses(start_date=start_date, end_date=end_date)

            if not expenses:
                print(f"\nNo expenses found between {start_date} and {end_date}.")
            else:
                print(f"\nExpenses from {start_date} to {end_date}:")
                self.display_expenses(expenses)
                print(f"\nTotal: ${self.manager.get_total(start_date=start_date, end_date=end_date):.2f}")

        except ValueError as e:
            print(f"\n[ERROR] Invalid date format: {e}")

        input("\nPress Enter to continue...")

    def update_expense(self):
        """Update an existing expense."""
        print("\n" + "="*60)
        print("UPDATE EXPENSE")
        print("="*60)

        try:
            expense_id = int(input("Enter expense ID to update: ").strip())
            expense = self.manager.get_expense(expense_id)

            print(f"\nCurrent expense:\n{expense}")
            print("\nLeave fields blank to keep current values.")

            updates = {}

            # Amount
            amount_str = input(f"New amount (current: ${expense.amount:.2f}): $").strip()
            if amount_str:
                updates['amount'] = float(amount_str)

            # Category
            category = input(f"New category (current: {expense.category}): ").strip()
            if category:
                updates['category'] = category

            # Description
            description = input(f"New description (current: {expense.description}): ").strip()
            if description:
                updates['description'] = description

            # Date
            date = input(f"New date (current: {expense.date}): ").strip()
            if date:
                updates['date'] = date

            # Tags
            tags_str = input(f"New tags (current: {', '.join(expense.tags)}): ").strip()
            if tags_str:
                updates['tags'] = [tag.strip() for tag in tags_str.split(',')]

            if updates:
                self.manager.update_expense(expense_id, **updates)
                print("\n[SUCCESS] Expense updated successfully!")
                print(f"\n{self.manager.get_expense(expense_id)}")
            else:
                print("\n[INFO] No changes made.")

        except ValueError as e:
            print(f"\n[ERROR] {e}")

        input("\nPress Enter to continue...")

    def delete_expense(self):
        """Delete an expense."""
        print("\n" + "="*60)
        print("DELETE EXPENSE")
        print("="*60)

        try:
            expense_id = int(input("Enter expense ID to delete: ").strip())
            expense = self.manager.get_expense(expense_id)

            print(f"\nExpense to delete:\n{expense}")
            confirm = input("\nAre you sure you want to delete this expense? (yes/no): ").strip().lower()

            if confirm == 'yes':
                self.manager.delete_expense(expense_id)
                print("\n[SUCCESS] Expense deleted successfully!")
            else:
                print("\n[INFO] Deletion cancelled.")

        except ValueError as e:
            print(f"\n[ERROR] {e}")

        input("\nPress Enter to continue...")

    def view_statistics(self):
        """View expense statistics."""
        print("\n" + "="*60)
        print("EXPENSE STATISTICS")
        print("="*60)

        date_filter = input("\nFilter by date range? (yes/no): ").strip().lower()
        start_date = None
        end_date = None

        if date_filter == 'yes':
            try:
                start_date = input("Start date (YYYY-MM-DD): ").strip()
                end_date = input("End date (YYYY-MM-DD): ").strip()
                datetime.strptime(start_date, '%Y-%m-%d')
                datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError as e:
                print(f"\n[ERROR] Invalid date format: {e}")
                input("\nPress Enter to continue...")
                return

        stats = self.manager.get_statistics(start_date, end_date)

        if stats['count'] == 0:
            print("\nNo expenses found.")
        else:
            print(f"\nTotal Expenses: {stats['count']}")
            print(f"Total Amount: ${stats['total']:.2f}")
            print(f"Average Amount: ${stats['average']:.2f}")

            print("\n" + "-"*60)
            print("BREAKDOWN BY CATEGORY")
            print("-"*60)
            for category, amount in stats['top_categories']:
                percentage = (amount / stats['total']) * 100
                bar_length = int(percentage / 2)
                bar = '█' * bar_length
                print(f"{category:20} ${amount:8.2f} ({percentage:5.1f}%) {bar}")

        input("\nPress Enter to continue...")

    def export_to_csv(self):
        """Export expenses to CSV."""
        print("\n" + "="*60)
        print("EXPORT TO CSV")
        print("="*60)

        try:
            filename = input("Enter filename (e.g., expenses.csv): ").strip()
            if not filename:
                filename = "expenses.csv"
            if not filename.endswith('.csv'):
                filename += '.csv'

            date_filter = input("\nFilter by date range? (yes/no): ").strip().lower()
            start_date = None
            end_date = None

            if date_filter == 'yes':
                start_date = input("Start date (YYYY-MM-DD): ").strip()
                end_date = input("End date (YYYY-MM-DD): ").strip()

            self.manager.export_to_csv(filename, start_date, end_date)
            print(f"\n[SUCCESS] Expenses exported to {filename}")

        except Exception as e:
            print(f"\n[ERROR] Failed to export: {e}")

        input("\nPress Enter to continue...")

    def search_expenses(self):
        """Search expenses by keyword."""
        print("\n" + "="*60)
        print("SEARCH EXPENSES")
        print("="*60)

        keyword = input("Enter search keyword: ").strip().lower()
        if not keyword:
            print("\n[ERROR] Search keyword cannot be empty.")
            input("\nPress Enter to continue...")
            return

        # Search in description, category, and tags
        matching_expenses = [
            expense for expense in self.manager.expenses
            if keyword in expense.description.lower() or
               keyword in expense.category.lower() or
               any(keyword in tag.lower() for tag in expense.tags)
        ]

        if not matching_expenses:
            print(f"\nNo expenses found matching '{keyword}'.")
        else:
            print(f"\nExpenses matching '{keyword}':")
            self.display_expenses(matching_expenses)
            total = sum(expense.amount for expense in matching_expenses)
            print(f"\nTotal: ${total:.2f}")

        input("\nPress Enter to continue...")

    def display_expenses(self, expenses):
        """
        Display a list of expenses.

        Args:
            expenses: List of Expense objects
        """
        print("\n" + "-"*60)
        for expense in sorted(expenses, key=lambda e: e.date, reverse=True):
            print(expense)
        print("-"*60)

    def exit_app(self):
        """Exit the application."""
        print("\n" + "="*60)
        print("Thank you for using Expense Tracker!")
        print("="*60 + "\n")
        self.running = False


def main():
    """Main entry point of the application."""
    try:
        app = ExpenseTrackerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
