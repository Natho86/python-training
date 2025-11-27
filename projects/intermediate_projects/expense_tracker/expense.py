"""
Expense class definition for the Expense Tracker application.
"""

from datetime import datetime
from typing import Dict, Any


class Expense:
    """
    Represents a single expense with category, amount, date, and description.
    """

    def __init__(self, amount: float, category: str, description: str = "",
                 date: str = None, tags: list = None, expense_id: int = None):
        """
        Initialize an Expense object.

        Args:
            amount: The expense amount (positive number)
            category: Category of the expense (e.g., 'Food', 'Transport')
            description: Optional description of the expense
            date: Date in YYYY-MM-DD format (defaults to today)
            tags: Optional list of tags for categorization
            expense_id: Unique identifier (auto-generated if not provided)

        Raises:
            ValueError: If amount is not positive or date format is invalid
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.amount = float(amount)
        self.category = category.strip().title()
        self.description = description.strip()
        self.tags = tags if tags else []
        self.expense_id = expense_id

        # Validate and set date
        if date:
            try:
                datetime.strptime(date, '%Y-%m-%d')
                self.date = date
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
        else:
            self.date = datetime.now().strftime('%Y-%m-%d')

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert expense to dictionary for serialization.

        Returns:
            Dictionary representation of the expense
        """
        return {
            'id': self.expense_id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date,
            'tags': self.tags
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Expense':
        """
        Create an Expense object from a dictionary.

        Args:
            data: Dictionary containing expense data

        Returns:
            Expense object
        """
        return cls(
            amount=data['amount'],
            category=data['category'],
            description=data.get('description', ''),
            date=data['date'],
            tags=data.get('tags', []),
            expense_id=data.get('id')
        )

    def matches_filters(self, category: str = None, tags: list = None,
                       start_date: str = None, end_date: str = None) -> bool:
        """
        Check if expense matches given filters.

        Args:
            category: Filter by category (case-insensitive)
            tags: Filter by tags (any match)
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format

        Returns:
            True if expense matches all provided filters
        """
        # Category filter
        if category and self.category.lower() != category.lower():
            return False

        # Tags filter (any tag match)
        if tags and not any(tag in self.tags for tag in tags):
            return False

        # Date range filter
        if start_date and self.date < start_date:
            return False
        if end_date and self.date > end_date:
            return False

        return True

    def __str__(self) -> str:
        """String representation of the expense."""
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        return (f"#{self.expense_id} - {self.date} | ${self.amount:.2f} | "
                f"{self.category} | {self.description}{tags_str}")

    def __repr__(self) -> str:
        """Developer representation of the expense."""
        return (f"Expense(id={self.expense_id}, amount={self.amount}, "
                f"category='{self.category}', date='{self.date}')")
