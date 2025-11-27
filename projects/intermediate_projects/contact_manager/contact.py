"""
Contact class definition for the Contact Manager application.
"""

import re
from typing import Dict, Any


class Contact:
    """
    Represents a contact with personal information and validation.
    """

    def __init__(self, first_name: str, last_name: str, phone: str = "",
                 email: str = "", address: str = "", notes: str = "",
                 contact_id: int = None):
        """
        Initialize a Contact object.

        Args:
            first_name: Contact's first name (required)
            last_name: Contact's last name (required)
            phone: Phone number (optional)
            email: Email address (optional)
            address: Physical address (optional)
            notes: Additional notes (optional)
            contact_id: Unique identifier (auto-generated if not provided)

        Raises:
            ValueError: If required fields are empty or data is invalid
        """
        # Validate and set required fields
        if not first_name or not first_name.strip():
            raise ValueError("First name is required")
        if not last_name or not last_name.strip():
            raise ValueError("Last name is required")

        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.contact_id = contact_id

        # Validate and set optional fields
        self.phone = self._validate_phone(phone.strip()) if phone else ""
        self.email = self._validate_email(email.strip()) if email else ""
        self.address = address.strip()
        self.notes = notes.strip()

    @staticmethod
    def _validate_phone(phone: str) -> str:
        """
        Validate phone number format.

        Args:
            phone: Phone number to validate

        Returns:
            Validated phone number

        Raises:
            ValueError: If phone format is invalid
        """
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)

        # Check if it contains only digits and optional + prefix
        if not re.match(r'^\+?\d{10,15}$', cleaned):
            raise ValueError(
                "Invalid phone number. Use format: +1234567890 or (123) 456-7890"
            )

        return phone

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Validate email address format.

        Args:
            email: Email address to validate

        Returns:
            Validated email address

        Raises:
            ValueError: If email format is invalid
        """
        # Basic email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email address format")

        return email.lower()

    def get_full_name(self) -> str:
        """
        Get the contact's full name.

        Returns:
            Full name as "First Last"
        """
        return f"{self.first_name} {self.last_name}"

    def matches_search(self, query: str) -> bool:
        """
        Check if contact matches search query.

        Args:
            query: Search query (case-insensitive)

        Returns:
            True if contact matches query
        """
        query_lower = query.lower()
        searchable_fields = [
            self.first_name.lower(),
            self.last_name.lower(),
            self.get_full_name().lower(),
            self.phone,
            self.email.lower(),
            self.address.lower(),
            self.notes.lower()
        ]

        return any(query_lower in field for field in searchable_fields)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert contact to dictionary for serialization.

        Returns:
            Dictionary representation of the contact
        """
        return {
            'id': self.contact_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'notes': self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Contact':
        """
        Create a Contact object from a dictionary.

        Args:
            data: Dictionary containing contact data

        Returns:
            Contact object
        """
        return cls(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data.get('phone', ''),
            email=data.get('email', ''),
            address=data.get('address', ''),
            notes=data.get('notes', ''),
            contact_id=data.get('id')
        )

    def to_csv_row(self) -> Dict[str, str]:
        """
        Convert contact to CSV row format.

        Returns:
            Dictionary with string values for CSV writing
        """
        return {
            'id': str(self.contact_id) if self.contact_id else '',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'notes': self.notes
        }

    @classmethod
    def from_csv_row(cls, row: Dict[str, str]) -> 'Contact':
        """
        Create a Contact object from a CSV row.

        Args:
            row: Dictionary from CSV reader

        Returns:
            Contact object
        """
        contact_id = int(row['id']) if row.get('id') and row['id'].isdigit() else None

        return cls(
            first_name=row['first_name'],
            last_name=row['last_name'],
            phone=row.get('phone', ''),
            email=row.get('email', ''),
            address=row.get('address', ''),
            notes=row.get('notes', ''),
            contact_id=contact_id
        )

    def __str__(self) -> str:
        """String representation of the contact."""
        lines = [
            f"ID: {self.contact_id}",
            f"Name: {self.get_full_name()}",
        ]

        if self.phone:
            lines.append(f"Phone: {self.phone}")
        if self.email:
            lines.append(f"Email: {self.email}")
        if self.address:
            lines.append(f"Address: {self.address}")
        if self.notes:
            lines.append(f"Notes: {self.notes}")

        return "\n".join(lines)

    def __repr__(self) -> str:
        """Developer representation of the contact."""
        return (f"Contact(id={self.contact_id}, name='{self.get_full_name()}', "
                f"phone='{self.phone}', email='{self.email}')")

    def __eq__(self, other) -> bool:
        """Check equality based on contact ID."""
        if not isinstance(other, Contact):
            return False
        return self.contact_id == other.contact_id

    def __lt__(self, other) -> bool:
        """Compare contacts for sorting (by last name, then first name)."""
        if not isinstance(other, Contact):
            return NotImplemented
        return (self.last_name, self.first_name) < (other.last_name, other.first_name)
