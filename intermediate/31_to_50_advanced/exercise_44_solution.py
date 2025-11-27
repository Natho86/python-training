# Exercise 44: Working with JSON Data - SOLUTION
# Difficulty: Intermediate-
# Concepts: JSON module, Serialization, Deserialization, File I/O

import json

# SOLUTION
print("=== JSON Basics ===")

# Create Python data structure
data = {
    "users": [
        {"name": "Alice", "age": 30, "email": "alice@example.com", "active": True},
        {"name": "Bob", "age": 25, "email": "bob@example.com", "active": True}
    ],
    "metadata": {
        "version": "1.0",
        "created": "2024-11-27"
    }
}

print("Original Python data:")
print(data)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print("\nJSON string (with indentation):")
print(json_string)

# Save to file
filename = "users.json"
with open(filename, 'w') as f:
    json.dump(data, f, indent=2)
print(f"\nSaved to {filename}")

# Read from file
with open(filename, 'r') as f:
    loaded_data = json.load(f)
print("\nLoaded from file:")
print(loaded_data)

# Modify data
print("\n--- Modifying Data ---")
loaded_data["users"].append({
    "name": "Charlie",
    "age": 35,
    "email": "charlie@example.com",
    "active": True
})
loaded_data["users"][0]["age"] = 31  # Update Alice's age

print("Modified data:")
print(json.dumps(loaded_data, indent=2))

# Save modified data
with open(filename, 'w') as f:
    json.dump(loaded_data, f, indent=2)
print(f"\nSaved modified data to {filename}")

"""
EXPLANATION:
1. json.dumps(obj) - Converts Python object to JSON string (serialize)
2. json.loads(str) - Converts JSON string to Python object (deserialize)
3. json.dump(obj, file) - Writes Python object as JSON to file
4. json.load(file) - Reads JSON from file into Python object
5. indent parameter adds whitespace for readability
6. Python dicts become JSON objects, lists become JSON arrays

Key Concepts:
- JSON is a text format for data exchange
- JSON supports: objects (dicts), arrays (lists), strings, numbers, booleans, null
- JSON doesn't support: functions, dates (use strings), sets (use lists)
- Always use 'w' mode for writing, 'r' mode for reading
- JSON is human-readable and language-independent
"""

# Type conversions
print("\n--- JSON TYPE CONVERSIONS ---")
print("Python -> JSON:")
print("  dict -> object")
print("  list/tuple -> array")
print("  str -> string")
print("  int/float -> number")
print("  True/False -> true/false")
print("  None -> null")

# Demonstrate type conversion
python_data = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "none": None,
    "list": [1, 2, 3],
    "nested": {"key": "value"}
}

json_output = json.dumps(python_data, indent=2)
print(f"\nPython data as JSON:\n{json_output}")

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

class ContactManager:
    """Manage contacts with JSON persistence."""

    def __init__(self, filename="contacts.json"):
        """Initialize contact manager."""
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file."""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        """Save contacts to JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        contact = {
            "id": len(self.contacts) + 1,
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Added contact: {name}")

    def update_contact(self, contact_id, **kwargs):
        """Update contact by ID."""
        for contact in self.contacts:
            if contact["id"] == contact_id:
                contact.update(kwargs)
                self.save_contacts()
                print(f"Updated contact {contact_id}")
                return True
        print(f"Contact {contact_id} not found")
        return False

    def delete_contact(self, contact_id):
        """Delete contact by ID."""
        for i, contact in enumerate(self.contacts):
            if contact["id"] == contact_id:
                deleted = self.contacts.pop(i)
                self.save_contacts()
                print(f"Deleted contact: {deleted['name']}")
                return True
        print(f"Contact {contact_id} not found")
        return False

    def search_contacts(self, query):
        """Search contacts by name or email."""
        query = query.lower()
        results = [c for c in self.contacts
                  if query in c["name"].lower() or query in c["email"].lower()]
        return results

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n=== Contact List ===")
        for contact in self.contacts:
            print(f"ID: {contact['id']}")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print()

# Test contact manager
print("\nTesting Contact Manager:")
manager = ContactManager()

# Add contacts
manager.add_contact("Alice Smith", "555-0001", "alice@example.com")
manager.add_contact("Bob Jones", "555-0002", "bob@example.com")
manager.add_contact("Charlie Brown", "555-0003", "charlie@example.com")

# List contacts
manager.list_contacts()

# Search contacts
print("Search for 'alice':")
results = manager.search_contacts("alice")
for contact in results:
    print(f"  Found: {contact['name']} - {contact['email']}")

# Update contact
manager.update_contact(1, phone="555-1111")

# Delete contact
manager.delete_contact(2)

# List updated contacts
manager.list_contacts()

# More JSON examples
print("\n--- MORE JSON EXAMPLES ---")

# Working with complex nested data
blog_post = {
    "title": "Introduction to Python",
    "author": {
        "name": "Jane Doe",
        "email": "jane@example.com"
    },
    "tags": ["python", "programming", "tutorial"],
    "published": True,
    "views": 1250,
    "comments": [
        {"user": "user1", "text": "Great post!", "likes": 5},
        {"user": "user2", "text": "Very helpful", "likes": 3}
    ]
}

print("Complex nested JSON:")
print(json.dumps(blog_post, indent=2))

# Accessing nested data
print(f"\nBlog title: {blog_post['title']}")
print(f"Author: {blog_post['author']['name']}")
print(f"Tags: {', '.join(blog_post['tags'])}")
print(f"Comments: {len(blog_post['comments'])}")

# Custom JSON encoding for dates
print("\n--- HANDLING DATES IN JSON ---")
from datetime import datetime

data_with_date = {
    "event": "Python Workshop",
    "date": datetime.now().isoformat(),  # Convert to ISO format string
    "participants": 25
}

json_str = json.dumps(data_with_date, indent=2)
print("Data with date:")
print(json_str)

# Loading back and parsing date
loaded = json.loads(json_str)
date_obj = datetime.fromisoformat(loaded["date"])
print(f"\nParsed date: {date_obj.strftime('%Y-%m-%d %H:%M:%S')}")

# Configuration file example
print("\n--- CONFIGURATION FILE EXAMPLE ---")

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "features": {
        "dark_mode": True,
        "notifications": True,
        "analytics": False
    },
    "max_users": 100
}

# Save configuration
with open("config.json", 'w') as f:
    json.dump(config, f, indent=2)

print("Configuration saved to config.json")
print(json.dumps(config, indent=2))

# Pretty print with custom formatting
print("\n--- CUSTOM JSON FORMATTING ---")

# Compact JSON (no spaces)
compact = json.dumps(data, separators=(',', ':'))
print(f"Compact JSON: {compact[:100]}...")

# Sorted keys
sorted_json = json.dumps(data, indent=2, sort_keys=True)
print(f"\nWith sorted keys:\n{sorted_json}")
