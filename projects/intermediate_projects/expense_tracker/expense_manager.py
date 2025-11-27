"""
ExpenseManager class for managing expense operations and data persistence.
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict
from expense import Expense


class ExpenseManager:
    """
    Manages a collection of expenses with CRUD operations and reporting.
    """

    def __init__(self, data_file: str = "expenses.json"):
        """
        Initialize the ExpenseManager.

        Args:
            data_file: Path to the JSON file for data persistence
        """
        self.data_file = data_file
        self.expenses: List[Expense] = []
        self.next_id = 1
        self.load_expenses()

    def add_expense(self, amount: float, category: str, description: str = "",
                   date: str = None, tags: list = None) -> Expense:
        """
        Add a new expense.

        Args:
            amount: Expense amount
            category: Expense category
            description: Optional description
            date: Optional date (defaults to today)
            tags: Optional list of tags

        Returns:
            The created Expense object

        Raises:
            ValueError: If expense data is invalid
        """
        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=date,
            tags=tags,
            expense_id=self.next_id
        )
        self.expenses.append(expense)
        self.next_id += 1
        self.save_expenses()
        return expense

    def get_expense(self, expense_id: int) -> Expense:
        """
        Get an expense by ID.

        Args:
            expense_id: The expense ID to find

        Returns:
            The Expense object

        Raises:
            ValueError: If expense not found
        """
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        raise ValueError(f"Expense with ID {expense_id} not found")

    def update_expense(self, expense_id: int, **kwargs) -> Expense:
        """
        Update an existing expense.

        Args:
            expense_id: The expense ID to update
            **kwargs: Fields to update (amount, category, description, date, tags)

        Returns:
            The updated Expense object

        Raises:
            ValueError: If expense not found or invalid data
        """
        expense = self.get_expense(expense_id)

        # Update fields
        if 'amount' in kwargs:
            if kwargs['amount'] <= 0:
                raise ValueError("Amount must be positive")
            expense.amount = float(kwargs['amount'])

        if 'category' in kwargs:
            expense.category = kwargs['category'].strip().title()

        if 'description' in kwargs:
            expense.description = kwargs['description'].strip()

        if 'date' in kwargs:
            try:
                datetime.strptime(kwargs['date'], '%Y-%m-%d')
                expense.date = kwargs['date']
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")

        if 'tags' in kwargs:
            expense.tags = kwargs['tags']

        self.save_expenses()
        return expense

    def delete_expense(self, expense_id: int) -> None:
        """
        Delete an expense by ID.

        Args:
            expense_id: The expense ID to delete

        Raises:
            ValueError: If expense not found
        """
        expense = self.get_expense(expense_id)
        self.expenses.remove(expense)
        self.save_expenses()

    def get_expenses(self, category: str = None, tags: list = None,
                    start_date: str = None, end_date: str = None) -> List[Expense]:
        """
        Get expenses matching the given filters.

        Args:
            category: Filter by category
            tags: Filter by tags
            start_date: Filter by start date
            end_date: Filter by end date

        Returns:
            List of matching Expense objects
        """
        if not any([category, tags, start_date, end_date]):
            return self.expenses

        return [
            expense for expense in self.expenses
            if expense.matches_filters(category, tags, start_date, end_date)
        ]

    def get_total(self, category: str = None, tags: list = None,
                 start_date: str = None, end_date: str = None) -> float:
        """
        Get total amount of expenses matching filters.

        Args:
            category: Filter by category
            tags: Filter by tags
            start_date: Filter by start date
            end_date: Filter by end date

        Returns:
            Total amount
        """
        expenses = self.get_expenses(category, tags, start_date, end_date)
        return sum(expense.amount for expense in expenses)

    def get_statistics(self, start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """
        Get expense statistics for the given date range.

        Args:
            start_date: Start date filter
            end_date: End date filter

        Returns:
            Dictionary containing various statistics
        """
        expenses = self.get_expenses(start_date=start_date, end_date=end_date)

        if not expenses:
            return {
                'total': 0,
                'count': 0,
                'average': 0,
                'by_category': {},
                'top_categories': []
            }

        # Calculate totals by category
        by_category = defaultdict(float)
        for expense in expenses:
            by_category[expense.category] += expense.amount

        # Sort categories by total amount
        top_categories = sorted(
            by_category.items(),
            key=lambda x: x[1],
            reverse=True
        )

        total = sum(expense.amount for expense in expenses)

        return {
            'total': total,
            'count': len(expenses),
            'average': total / len(expenses),
            'by_category': dict(by_category),
            'top_categories': top_categories
        }

    def export_to_csv(self, filename: str, start_date: str = None,
                     end_date: str = None) -> None:
        """
        Export expenses to CSV file.

        Args:
            filename: Output CSV filename
            start_date: Optional start date filter
            end_date: Optional end date filter
        """
        expenses = self.get_expenses(start_date=start_date, end_date=end_date)

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'date', 'category', 'amount', 'description', 'tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in expenses:
                row = expense.to_dict()
                row['tags'] = ';'.join(row['tags'])  # Convert list to string
                writer.writerow(row)

    def save_expenses(self) -> None:
        """Save expenses to JSON file."""
        data = {
            'next_id': self.next_id,
            'expenses': [expense.to_dict() for expense in self.expenses]
        }

        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to save expenses: {e}")

    def load_expenses(self) -> None:
        """Load expenses from JSON file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.next_id = data.get('next_id', 1)
                self.expenses = [
                    Expense.from_dict(exp_data)
                    for exp_data in data.get('expenses', [])
                ]
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            self.expenses = []
            self.next_id = 1
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in data file: {e}")
        except Exception as e:
            raise Exception(f"Failed to load expenses: {e}")

    def get_all_categories(self) -> List[str]:
        """
        Get a list of all unique categories.

        Returns:
            Sorted list of category names
        """
        categories = set(expense.category for expense in self.expenses)
        return sorted(categories)

    def get_all_tags(self) -> List[str]:
        """
        Get a list of all unique tags.

        Returns:
            Sorted list of tag names
        """
        tags = set()
        for expense in self.expenses:
            tags.update(expense.tags)
        return sorted(tags)
