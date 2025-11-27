# Exercise 28: Contact Book Project - SOLUTION
# Difficulty: Intermediate-
# Concepts: Dictionaries, File I/O, CSV, Error handling, User input

# SOLUTION
import csv
import os
from datetime import datetime

class ContactBook:
    """A simple contact book application with CSV storage."""

    def __init__(self, filename='temp_files/contacts.csv'):
        self.filename = filename
        self.fieldnames = ['name', 'phone', 'email', 'address', 'date_added']
        self._initialize_file()

    def _initialize_file(self):
        """Create CSV file with headers if it doesn't exist."""
        # Ensure directory exists
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Create file with headers if needed
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
            print(f"Created new contact book: {self.filename}\n")

    def add_contact(self, name, phone, email, address):
        """Add a new contact to the contact book."""
        try:
            # Validate input
            if not name or not phone:
                return "Error: Name and phone are required"

            # Check for duplicate
            if self._contact_exists(name):
                return f"Error: Contact '{name}' already exists"

            # Create contact
            contact = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address,
                'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            # Append to file
            with open(self.filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writerow(contact)

            return f"Successfully added contact: {name}"

        except Exception as e:
            return f"Error adding contact: {str(e)}"

    def _contact_exists(self, name):
        """Check if a contact already exists."""
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['name'].lower() == name.lower():
                        return True
            return False
        except Exception:
            return False

    def search_contact(self, name):
        """Search for a contact by name (case-insensitive)."""
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                results = []
                for row in reader:
                    if name.lower() in row['name'].lower():
                        results.append(row)

                if results:
                    return results
                else:
                    return None

        except Exception as e:
            return f"Error searching: {str(e)}"

    def display_all_contacts(self):
        """Display all contacts in a formatted table."""
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                contacts = list(reader)

                if not contacts:
                    return "No contacts found"

                return contacts

        except Exception as e:
            return f"Error displaying contacts: {str(e)}"

    def delete_contact(self, name):
        """Delete a contact by name."""
        try:
            # Read all contacts
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                contacts = list(reader)

            # Filter out the contact to delete
            original_count = len(contacts)
            contacts = [c for c in contacts if c['name'].lower() != name.lower()]

            if len(contacts) == original_count:
                return f"Contact '{name}' not found"

            # Write back remaining contacts
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(contacts)

            return f"Successfully deleted contact: {name}"

        except Exception as e:
            return f"Error deleting contact: {str(e)}"

    def format_contact_table(self, contacts):
        """Format contacts as a readable table."""
        if isinstance(contacts, str):
            return contacts

        if not contacts:
            return "No contacts to display"

        # Create table
        output = "\n" + "=" * 100 + "\n"
        output += f"{'Name':<20} {'Phone':<15} {'Email':<30} {'Address':<20}\n"
        output += "-" * 100 + "\n"

        for contact in contacts:
            name = contact['name'][:19]
            phone = contact['phone'][:14]
            email = contact['email'][:29]
            address = contact['address'][:19]
            output += f"{name:<20} {phone:<15} {email:<30} {address:<20}\n"

        output += "=" * 100 + "\n"
        return output

    def get_contact_count(self):
        """Get the total number of contacts."""
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                return len(list(reader))
        except Exception:
            return 0


# Demonstration of the contact book
print("CONTACT BOOK APPLICATION")
print("=" * 60)

# Create contact book
book = ContactBook()

# Add some contacts
print("Adding contacts...")
print(book.add_contact("Alice Johnson", "555-1234", "alice@email.com", "123 Main St"))
print(book.add_contact("Bob Smith", "555-5678", "bob@email.com", "456 Oak Ave"))
print(book.add_contact("Charlie Brown", "555-9012", "charlie@email.com", "789 Pine Rd"))
print(book.add_contact("Diana Prince", "555-3456", "diana@email.com", "321 Elm St"))
print()

# Try to add duplicate
print("Trying to add duplicate:")
print(book.add_contact("Alice Johnson", "555-9999", "alice2@email.com", "999 Test St"))
print()

# Display all contacts
print("All Contacts:")
all_contacts = book.display_all_contacts()
print(book.format_contact_table(all_contacts))

# Search for contacts
print("\nSearching for 'Alice':")
results = book.search_contact("Alice")
if results:
    print(book.format_contact_table(results))
else:
    print("No results found")

# Search with partial match
print("\nSearching for 'brown' (case-insensitive):")
results = book.search_contact("brown")
if results:
    print(book.format_contact_table(results))

# Delete a contact
print("\nDeleting 'Bob Smith':")
print(book.delete_contact("Bob Smith"))
print()

# Display all after deletion
print("Contacts after deletion:")
all_contacts = book.display_all_contacts()
print(book.format_contact_table(all_contacts))

# Show contact count
print(f"\nTotal contacts: {book.get_contact_count()}")

"""
EXPLANATION:
1. ContactBook class manages all contact operations
2. Uses CSV file for persistent storage
3. Each contact is a dictionary with name, phone, email, address
4. DictReader/DictWriter make CSV handling easier
5. All operations include error handling with try/except
6. _initialize_file creates the CSV file if it doesn't exist
7. _contact_exists prevents duplicates
8. Search is case-insensitive and allows partial matches
9. Delete rewrites the entire file without the deleted contact

Key Concepts:
- Class encapsulates all contact book functionality
- CSV provides simple persistent storage
- Error handling makes the application robust
- Private methods (starting with _) are internal helpers
- Formatting methods separate data from presentation
"""

# Extension solution: Enhanced contact book
print("\n--- EXTENSION SOLUTION: ENHANCED FEATURES ---")

class EnhancedContactBook(ContactBook):
    """Contact book with additional features."""

    def edit_contact(self, name, **kwargs):
        """Edit an existing contact."""
        try:
            # Read all contacts
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                contacts = list(reader)

            # Find and update the contact
            found = False
            for contact in contacts:
                if contact['name'].lower() == name.lower():
                    for key, value in kwargs.items():
                        if key in contact and value is not None:
                            contact[key] = value
                    found = True
                    break

            if not found:
                return f"Contact '{name}' not found"

            # Write back all contacts
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(contacts)

            return f"Successfully updated contact: {name}"

        except Exception as e:
            return f"Error editing contact: {str(e)}"

    def sort_contacts(self, sort_by='name', reverse=False):
        """Get contacts sorted by specified field."""
        try:
            contacts = self.display_all_contacts()
            if isinstance(contacts, str) or not contacts:
                return contacts

            sorted_contacts = sorted(
                contacts,
                key=lambda x: x.get(sort_by, '').lower(),
                reverse=reverse
            )
            return sorted_contacts

        except Exception as e:
            return f"Error sorting: {str(e)}"

    def validate_email(self, email):
        """Validate email format."""
        if not email:
            return True  # Email is optional

        if '@' not in email:
            return False

        if email.count('@') != 1:
            return False

        local, domain = email.split('@')
        if not local or not domain:
            return False

        if '.' not in domain:
            return False

        return True

    def validate_phone(self, phone):
        """Validate phone format (simple validation)."""
        # Remove common separators
        digits = ''.join(c for c in phone if c.isdigit())

        # Check if we have reasonable number of digits (7-15)
        if 7 <= len(digits) <= 15:
            return True
        return False

    def add_contact_validated(self, name, phone, email, address):
        """Add contact with validation."""
        # Validate email
        if email and not self.validate_email(email):
            return f"Error: Invalid email format: {email}"

        # Validate phone
        if not self.validate_phone(phone):
            return f"Error: Invalid phone format: {phone}"

        # Call parent method to add
        return self.add_contact(name, phone, email, address)

    def backup_contacts(self, backup_filename=None):
        """Create a backup of the contacts file."""
        if backup_filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f"temp_files/contacts_backup_{timestamp}.csv"

        try:
            with open(self.filename, 'r') as src:
                with open(backup_filename, 'w') as dst:
                    dst.write(src.read())

            return f"Backup created: {backup_filename}"

        except Exception as e:
            return f"Error creating backup: {str(e)}"

    def import_from_backup(self, backup_filename):
        """Import contacts from a backup file."""
        try:
            if not os.path.exists(backup_filename):
                return f"Error: Backup file not found: {backup_filename}"

            with open(backup_filename, 'r') as src:
                with open(self.filename, 'w') as dst:
                    dst.write(src.read())

            return f"Contacts imported from: {backup_filename}"

        except Exception as e:
            return f"Error importing backup: {str(e)}"


# Test enhanced features
print("\nCreating enhanced contact book...")
enhanced_book = EnhancedContactBook('temp_files/enhanced_contacts.csv')

# Add contacts with validation
print("\nAdding contacts with validation:")
print(enhanced_book.add_contact_validated("Eve Adams", "555-7890", "eve@email.com", "111 First St"))
print(enhanced_book.add_contact_validated("Frank Miller", "123", "invalid-email", "222 Second St"))
print(enhanced_book.add_contact_validated("Grace Lee", "555-4321", "grace@email.com", "333 Third St"))

# Edit a contact
print("\nEditing contact 'Eve Adams':")
print(enhanced_book.edit_contact("Eve Adams", phone="555-9999", email="eve.adams@email.com"))

# Sort contacts
print("\nContacts sorted by name:")
sorted_contacts = enhanced_book.sort_contacts(sort_by='name')
print(enhanced_book.format_contact_table(sorted_contacts))

# Create backup
print("\nCreating backup:")
print(enhanced_book.backup_contacts())

# Interactive menu example
print("\n--- INTERACTIVE MENU EXAMPLE ---")

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("CONTACT BOOK MENU")
    print("=" * 40)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Sort Contacts")
    print("7. Backup Contacts")
    print("8. Exit")
    print("=" * 40)

def run_contact_book():
    """Run the contact book application (demo version)."""
    book = EnhancedContactBook('temp_files/demo_contacts.csv')

    # Pre-populate with sample data for demo
    book.add_contact("Demo User 1", "555-0001", "demo1@email.com", "Demo Address 1")
    book.add_contact("Demo User 2", "555-0002", "demo2@email.com", "Demo Address 2")

    print("\nContact Book Application (Demo Mode)")
    print("This is a demonstration - in interactive mode, you would enter choices.")
    print("\nSimulating user interactions:\n")

    # Simulate some operations
    operations = [
        ("Display All", lambda: book.display_all_contacts()),
        ("Search 'Demo'", lambda: book.search_contact("Demo")),
        ("Add New", lambda: book.add_contact("New User", "555-1111", "new@email.com", "New Address")),
        ("Delete 'Demo User 2'", lambda: book.delete_contact("Demo User 2")),
    ]

    for operation_name, operation in operations:
        print(f"\nOperation: {operation_name}")
        print("-" * 40)
        result = operation()
        if isinstance(result, list):
            print(book.format_contact_table(result))
        else:
            print(result)

    print(f"\n\nFinal contact count: {book.get_contact_count()}")

# Run the demo
run_contact_book()

print("\n" + "=" * 60)
print("Contact book files created in 'temp_files/' directory")
print("=" * 60)
