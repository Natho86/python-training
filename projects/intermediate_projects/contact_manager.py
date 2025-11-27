"""
Contact Manager - Intermediate Python Project
==============================================
A comprehensive contact management system with CRUD operations, search, and CSV import/export.

Features:
- Create, Read, Update, Delete contacts
- Search and filter functionality
- Email and phone validation
- Import/Export to CSV
- Backup system
- Group contacts by category

Concepts: OOP, CSV, file I/O, dictionaries, error handling, data validation, regular expressions
"""

import csv
import json
import os
import re
from datetime import datetime


class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone, email, category='General', address='', notes='', contact_id=None):
        """Initialize a contact."""
        self.id = contact_id if contact_id else datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category
        self.address = address
        self.notes = notes
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_email(email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone):
        """Validate phone format (flexible)."""
        # Remove common separators
        digits = re.sub(r'[\s\-\(\)]', '', phone)
        # Check if it's 10 digits or more
        return len(digits) >= 10 and digits.isdigit()

    def to_dict(self):
        """Convert contact to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'category': self.category,
            'address': self.address,
            'notes': self.notes,
            'created_date': self.created_date
        }

    def __str__(self):
        """String representation."""
        return f"{self.name} | {self.phone} | {self.email} | {self.category}"


class ContactManager:
    """Main contact manager application."""

    CATEGORIES = ['Family', 'Friends', 'Work', 'Business', 'General', 'Other']

    def __init__(self, filename='contacts.json'):
        """Initialize the contact manager."""
        self.filename = filename
        self.contacts = []
        self.load_data()

    def load_data(self):
        """Load contacts from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.contacts = [
                        Contact(
                            c['name'], c['phone'], c['email'],
                            c.get('category', 'General'),
                            c.get('address', ''),
                            c.get('notes', ''),
                            c['id']
                        ) for c in data
                    ]
                print(f"✓ Loaded {len(self.contacts)} contacts")
            else:
                print("No existing contacts file. Starting fresh!")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.contacts = []

    def save_data(self):
        """Save contacts to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def create_backup(self):
        """Create a backup of contacts."""
        try:
            backup_name = f"contacts_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(backup_name, 'w') as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=2)
            print(f"✓ Backup created: {backup_name}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    def add_contact(self):
        """Add a new contact."""
        print("\n=== Add New Contact ===")

        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        phone = input("Phone: ").strip()
        if not Contact.validate_phone(phone):
            print("Invalid phone number format!")
            return

        email = input("Email: ").strip()
        if email and not Contact.validate_email(email):
            print("Invalid email format!")
            return

        # Show categories
        print("\nCategories:")
        for i, cat in enumerate(self.CATEGORIES, 1):
            print(f"{i}. {cat}")

        try:
            cat_choice = int(input("Select category (1-6): "))
            if 1 <= cat_choice <= len(self.CATEGORIES):
                category = self.CATEGORIES[cat_choice - 1]
            else:
                category = 'General'
        except ValueError:
            category = 'General'

        address = input("Address (optional): ").strip()
        notes = input("Notes (optional): ").strip()

        contact = Contact(name, phone, email, category, address, notes)
        self.contacts.append(contact)
        self.save_data()
        print(f"\n✓ Contact added successfully! (ID: {contact.id})")

    def view_all_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("\nNo contacts found!")
            return

        print(f"\n=== All Contacts ({len(self.contacts)} total) ===")
        print("-" * 100)
        print(f"{'Name':<20} | {'Phone':<15} | {'Email':<30} | {'Category':<12}")
        print("-" * 100)

        for contact in sorted(self.contacts, key=lambda x: x.name):
            print(f"{contact.name:<20} | {contact.phone:<15} | {contact.email:<30} | {contact.category:<12}")

    def view_contact_details(self, contact):
        """Display detailed contact information."""
        print("\n" + "="*60)
        print(f"Name:     {contact.name}")
        print(f"Phone:    {contact.phone}")
        print(f"Email:    {contact.email}")
        print(f"Category: {contact.category}")
        print(f"Address:  {contact.address if contact.address else 'N/A'}")
        print(f"Notes:    {contact.notes if contact.notes else 'N/A'}")
        print(f"Created:  {contact.created_date}")
        print(f"ID:       {contact.id}")
        print("="*60)

    def search_contacts(self):
        """Search for contacts."""
        print("\n=== Search Contacts ===")
        query = input("Enter search term (name, phone, or email): ").strip().lower()

        if not query:
            return

        results = [
            c for c in self.contacts
            if query in c.name.lower() or query in c.phone or query in c.email.lower()
        ]

        if not results:
            print("No contacts found!")
            return

        print(f"\nFound {len(results)} contact(s):")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact}")

        try:
            choice = int(input("\nEnter number to view details (0 to cancel): "))
            if 1 <= choice <= len(results):
                self.view_contact_details(results[choice - 1])
        except ValueError:
            pass

    def update_contact(self):
        """Update an existing contact."""
        self.search_contacts()

        contact_id = input("\nEnter contact ID to update (or 'cancel'): ").strip()

        if contact_id.lower() == 'cancel':
            return

        contact = None
        for c in self.contacts:
            if c.id == contact_id:
                contact = c
                break

        if not contact:
            print("Contact not found!")
            return

        print(f"\nUpdating: {contact.name}")
        print("(Press Enter to keep current value)")

        name = input(f"Name [{contact.name}]: ").strip()
        if name:
            contact.name = name

        phone = input(f"Phone [{contact.phone}]: ").strip()
        if phone and Contact.validate_phone(phone):
            contact.phone = phone
        elif phone:
            print("Invalid phone format, keeping original")

        email = input(f"Email [{contact.email}]: ").strip()
        if email and Contact.validate_email(email):
            contact.email = email
        elif email:
            print("Invalid email format, keeping original")

        address = input(f"Address [{contact.address}]: ").strip()
        if address:
            contact.address = address

        notes = input(f"Notes [{contact.notes}]: ").strip()
        if notes:
            contact.notes = notes

        self.save_data()
        print("✓ Contact updated!")

    def delete_contact(self):
        """Delete a contact."""
        self.search_contacts()

        contact_id = input("\nEnter contact ID to delete (or 'cancel'): ").strip()

        if contact_id.lower() == 'cancel':
            return

        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                print(f"\nDeleting: {contact.name}")
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    self.contacts.pop(i)
                    self.save_data()
                    print("✓ Contact deleted!")
                return

        print("Contact not found!")

    def view_by_category(self):
        """View contacts grouped by category."""
        if not self.contacts:
            print("\nNo contacts found!")
            return

        print("\n=== Contacts by Category ===")

        from collections import defaultdict
        categorized = defaultdict(list)

        for contact in self.contacts:
            categorized[contact.category].append(contact)

        for category in sorted(categorized.keys()):
            contacts = categorized[category]
            print(f"\n{category} ({len(contacts)}):")
            for contact in sorted(contacts, key=lambda x: x.name):
                print(f"  {contact.name:<20} | {contact.phone:<15} | {contact.email}")

    def export_to_csv(self):
        """Export contacts to CSV file."""
        if not self.contacts:
            print("\nNo contacts to export!")
            return

        filename = input("Enter CSV filename (or press Enter for 'contacts.csv'): ").strip()
        if not filename:
            filename = 'contacts.csv'

        if not filename.endswith('.csv'):
            filename += '.csv'

        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'category', 'address', 'notes'])
                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow({
                        'name': contact.name,
                        'phone': contact.phone,
                        'email': contact.email,
                        'category': contact.category,
                        'address': contact.address,
                        'notes': contact.notes
                    })
            print(f"✓ Exported {len(self.contacts)} contacts to {filename}")
        except Exception as e:
            print(f"Error exporting: {e}")

    def import_from_csv(self):
        """Import contacts from CSV file."""
        filename = input("Enter CSV filename to import: ").strip()

        if not os.path.exists(filename):
            print("File not found!")
            return

        try:
            count = 0
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('name') and row.get('phone'):
                        contact = Contact(
                            row['name'],
                            row['phone'],
                            row.get('email', ''),
                            row.get('category', 'General'),
                            row.get('address', ''),
                            row.get('notes', '')
                        )
                        self.contacts.append(contact)
                        count += 1

            self.save_data()
            print(f"✓ Imported {count} contacts from {filename}")
        except Exception as e:
            print(f"Error importing: {e}")

    def run(self):
        """Run the main application loop."""
        print("\n" + "="*60)
        print("              CONTACT MANAGER")
        print("="*60)

        while True:
            print("\n=== Main Menu ===")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contacts")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. View by Category")
            print("7. Export to CSV")
            print("8. Import from CSV")
            print("9. Create Backup")
            print("10. Exit")

            choice = input("\nEnter choice (1-10): ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_all_contacts()
            elif choice == '3':
                self.search_contacts()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                self.view_by_category()
            elif choice == '7':
                self.export_to_csv()
            elif choice == '8':
                self.import_from_csv()
            elif choice == '9':
                self.create_backup()
            elif choice == '10':
                print("\nThank you for using Contact Manager!")
                break
            else:
                print("\nInvalid choice! Please enter 1-10.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
