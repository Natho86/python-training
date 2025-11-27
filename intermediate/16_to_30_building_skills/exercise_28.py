# Exercise 28: Contact Book Project
# Difficulty: Intermediate-
# Concepts: Dictionaries, File I/O, CSV, Error handling, User input

"""
PROBLEM:
Create a contact book application that:
1. Stores contacts (name, phone, email, address) in a CSV file
2. Allows adding new contacts
3. Allows searching for contacts by name
4. Allows displaying all contacts
5. Allows deleting contacts
6. Handles errors gracefully (invalid input, file errors)

EXAMPLE:
Menu:
1. Add Contact
2. Search Contact
3. Display All
4. Delete Contact
5. Exit

Operations:
- Add: Alice, 555-1234, alice@email.com, 123 Main St
- Search: "Alice" -> Display Alice's info
- Display All -> Show all contacts in formatted table
- Delete: "Alice" -> Remove Alice from contacts

HINTS:
1. Use a dictionary to represent each contact
2. Store contacts in a CSV file for persistence
3. Create functions for each operation (add, search, display, delete)
4. Use try/except for file operations and user input
5. Use csv.DictReader and csv.DictWriter for easier CSV handling

EXTENSION:
Add edit functionality to update existing contacts.
Implement sorting (by name, by date added).
Add data validation (email format, phone format).
Create a backup system that saves to multiple files.
"""

# Write your solution here
