"""
ContactManager class for managing contact operations and data persistence.
"""

import json
import csv
import os
import shutil
from datetime import datetime
from typing import List, Optional
from contact import Contact


class ContactManager:
    """
    Manages a collection of contacts with CRUD operations and data persistence.
    """

    def __init__(self, data_file: str = "contacts.json",
                 backup_dir: str = "backups"):
        """
        Initialize the ContactManager.

        Args:
            data_file: Path to the JSON file for data persistence
            backup_dir: Directory for storing backups
        """
        self.data_file = data_file
        self.backup_dir = backup_dir
        self.contacts: List[Contact] = []
        self.next_id = 1

        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        self.load_contacts()

    def add_contact(self, first_name: str, last_name: str, phone: str = "",
                   email: str = "", address: str = "", notes: str = "") -> Contact:
        """
        Add a new contact.

        Args:
            first_name: Contact's first name
            last_name: Contact's last name
            phone: Phone number (optional)
            email: Email address (optional)
            address: Physical address (optional)
            notes: Additional notes (optional)

        Returns:
            The created Contact object

        Raises:
            ValueError: If contact data is invalid
        """
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            address=address,
            notes=notes,
            contact_id=self.next_id
        )

        self.contacts.append(contact)
        self.next_id += 1
        self.save_contacts()
        return contact

    def get_contact(self, contact_id: int) -> Contact:
        """
        Get a contact by ID.

        Args:
            contact_id: The contact ID to find

        Returns:
            The Contact object

        Raises:
            ValueError: If contact not found
        """
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact
        raise ValueError(f"Contact with ID {contact_id} not found")

    def update_contact(self, contact_id: int, **kwargs) -> Contact:
        """
        Update an existing contact.

        Args:
            contact_id: The contact ID to update
            **kwargs: Fields to update

        Returns:
            The updated Contact object

        Raises:
            ValueError: If contact not found or invalid data
        """
        contact = self.get_contact(contact_id)

        # Update fields
        if 'first_name' in kwargs:
            if not kwargs['first_name'].strip():
                raise ValueError("First name cannot be empty")
            contact.first_name = kwargs['first_name'].strip().title()

        if 'last_name' in kwargs:
            if not kwargs['last_name'].strip():
                raise ValueError("Last name cannot be empty")
            contact.last_name = kwargs['last_name'].strip().title()

        if 'phone' in kwargs:
            phone = kwargs['phone'].strip()
            contact.phone = Contact._validate_phone(phone) if phone else ""

        if 'email' in kwargs:
            email = kwargs['email'].strip()
            contact.email = Contact._validate_email(email) if email else ""

        if 'address' in kwargs:
            contact.address = kwargs['address'].strip()

        if 'notes' in kwargs:
            contact.notes = kwargs['notes'].strip()

        self.save_contacts()
        return contact

    def delete_contact(self, contact_id: int) -> None:
        """
        Delete a contact by ID.

        Args:
            contact_id: The contact ID to delete

        Raises:
            ValueError: If contact not found
        """
        contact = self.get_contact(contact_id)
        self.contacts.remove(contact)
        self.save_contacts()

    def get_all_contacts(self, sort_by: str = "name") -> List[Contact]:
        """
        Get all contacts, optionally sorted.

        Args:
            sort_by: Sort criteria ("name", "id", or "email")

        Returns:
            List of Contact objects
        """
        if sort_by == "name":
            return sorted(self.contacts)
        elif sort_by == "id":
            return sorted(self.contacts, key=lambda c: c.contact_id)
        elif sort_by == "email":
            return sorted(self.contacts, key=lambda c: c.email.lower())
        else:
            return self.contacts

    def search_contacts(self, query: str) -> List[Contact]:
        """
        Search contacts by query string.

        Args:
            query: Search query (searches in all fields)

        Returns:
            List of matching Contact objects
        """
        if not query:
            return self.contacts

        return [
            contact for contact in self.contacts
            if contact.matches_search(query)
        ]

    def filter_by_field(self, field: str, value: str) -> List[Contact]:
        """
        Filter contacts by a specific field.

        Args:
            field: Field name to filter by
            value: Value to match (case-insensitive)

        Returns:
            List of matching Contact objects
        """
        value_lower = value.lower()
        results = []

        for contact in self.contacts:
            if field == "first_name" and contact.first_name.lower() == value_lower:
                results.append(contact)
            elif field == "last_name" and contact.last_name.lower() == value_lower:
                results.append(contact)
            elif field == "email" and contact.email.lower() == value_lower:
                results.append(contact)
            elif field == "phone" and contact.phone == value:
                results.append(contact)

        return results

    def import_from_csv(self, filename: str) -> tuple:
        """
        Import contacts from CSV file.

        Args:
            filename: CSV file to import from

        Returns:
            Tuple of (success_count, error_count, errors_list)

        Raises:
            FileNotFoundError: If file doesn't exist
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")

        success_count = 0
        error_count = 0
        errors = []

        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                    try:
                        contact = Contact.from_csv_row(row)
                        contact.contact_id = self.next_id
                        self.contacts.append(contact)
                        self.next_id += 1
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        errors.append(f"Row {row_num}: {str(e)}")

            if success_count > 0:
                self.save_contacts()

            return success_count, error_count, errors

        except Exception as e:
            raise Exception(f"Failed to import CSV: {e}")

    def export_to_csv(self, filename: str) -> None:
        """
        Export all contacts to CSV file.

        Args:
            filename: Output CSV filename
        """
        if not self.contacts:
            raise ValueError("No contacts to export")

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'first_name', 'last_name', 'phone',
                         'email', 'address', 'notes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for contact in sorted(self.contacts):
                writer.writerow(contact.to_csv_row())

    def create_backup(self) -> str:
        """
        Create a backup of the current contacts file.

        Returns:
            Path to the backup file

        Raises:
            Exception: If backup creation fails
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError("No data file to backup")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"contacts_backup_{timestamp}.json"
        backup_path = os.path.join(self.backup_dir, backup_filename)

        try:
            shutil.copy2(self.data_file, backup_path)
            return backup_path
        except Exception as e:
            raise Exception(f"Failed to create backup: {e}")

    def restore_from_backup(self, backup_file: str) -> None:
        """
        Restore contacts from a backup file.

        Args:
            backup_file: Path to backup file

        Raises:
            FileNotFoundError: If backup file doesn't exist
            Exception: If restore fails
        """
        if not os.path.exists(backup_file):
            raise FileNotFoundError(f"Backup file not found: {backup_file}")

        try:
            # Create a backup of current data before restoring
            if os.path.exists(self.data_file):
                self.create_backup()

            # Restore from backup
            shutil.copy2(backup_file, self.data_file)
            self.load_contacts()

        except Exception as e:
            raise Exception(f"Failed to restore from backup: {e}")

    def list_backups(self) -> List[str]:
        """
        List all available backup files.

        Returns:
            List of backup filenames sorted by date (newest first)
        """
        if not os.path.exists(self.backup_dir):
            return []

        backups = [
            f for f in os.listdir(self.backup_dir)
            if f.startswith("contacts_backup_") and f.endswith(".json")
        ]

        return sorted(backups, reverse=True)

    def get_statistics(self) -> dict:
        """
        Get statistics about the contacts.

        Returns:
            Dictionary containing statistics
        """
        total = len(self.contacts)
        with_phone = sum(1 for c in self.contacts if c.phone)
        with_email = sum(1 for c in self.contacts if c.email)
        with_address = sum(1 for c in self.contacts if c.address)
        with_notes = sum(1 for c in self.contacts if c.notes)

        return {
            'total': total,
            'with_phone': with_phone,
            'with_email': with_email,
            'with_address': with_address,
            'with_notes': with_notes,
            'complete': sum(1 for c in self.contacts
                          if c.phone and c.email and c.address)
        }

    def save_contacts(self) -> None:
        """
        Save contacts to JSON file.

        Raises:
            IOError: If save fails
        """
        data = {
            'next_id': self.next_id,
            'contacts': [contact.to_dict() for contact in self.contacts]
        }

        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to save contacts: {e}")

    def load_contacts(self) -> None:
        """
        Load contacts from JSON file.

        Raises:
            ValueError: If JSON is invalid
            Exception: If load fails
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.next_id = data.get('next_id', 1)
                self.contacts = [
                    Contact.from_dict(contact_data)
                    for contact_data in data.get('contacts', [])
                ]
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            self.contacts = []
            self.next_id = 1
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in data file: {e}")
        except Exception as e:
            raise Exception(f"Failed to load contacts: {e}")
