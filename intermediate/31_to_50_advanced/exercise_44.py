# Exercise 44: Working with JSON Data
# Difficulty: Intermediate-
# Concepts: JSON module, Serialization, Deserialization, File I/O

"""
PROBLEM:
Create a program that:
1. Creates a Python dictionary with nested data (users with multiple fields)
2. Saves it to a JSON file
3. Reads the JSON file back into Python
4. Modifies the data and saves it again
5. Pretty-prints JSON with indentation

EXAMPLE:
Original data:
{
    "users": [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "Bob", "age": 25, "email": "bob@example.com"}
    ]
}

After modification:
- Add new user
- Update existing user's age
- Save back to file

HINTS:
1. json.dumps() converts Python to JSON string
2. json.loads() converts JSON string to Python
3. json.dump() writes directly to file
4. json.load() reads directly from file
5. Use indent parameter for pretty printing

EXTENSION:
Create a simple contact management system that saves contacts to JSON,
with functions to add, update, delete, and search contacts.
"""

# Write your solution here
