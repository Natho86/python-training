# Exercise 49: Library Book Management System
# Difficulty: Intermediate
# Concepts: OOP, JSON, datetime, Collections, File I/O, Multiple classes

"""
PROBLEM:
Create a comprehensive library management system with:

Classes:
1. Book - represents a book (title, author, ISBN, available copies)
2. Member - represents a library member (name, member_id, borrowed books)
3. Library - manages books and members

Features:
- Add/remove books from library
- Register members
- Borrow and return books
- Track due dates (14 days from borrow date)
- Calculate late fees ($1 per day overdue)
- Search books by title or author
- View member borrowing history
- Save/load library state from JSON

EXAMPLE:
library = Library("City Library")

# Add books
library.add_book("1984", "George Orwell", "978-0451524935", copies=3)

# Register member
library.register_member("Alice Smith")

# Borrow book
library.borrow_book(member_id=1, isbn="978-0451524935")

# Return book (calculate late fee if overdue)
library.return_book(member_id=1, isbn="978-0451524935")

# Statistics
library.show_statistics()

HINTS:
1. Use separate classes for Book, Member, and Library
2. Library should have lists of books and members
3. Use datetime for tracking borrow/return dates
4. Calculate days overdue: (return_date - due_date).days
5. Save complete library state to JSON

EXTENSION:
Add reservation system where members can reserve borrowed books.
Add book categories and search/filter by category.
Generate detailed reports (most borrowed books, active members, etc.)
"""

# Write your solution here
