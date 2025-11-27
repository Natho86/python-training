# Exercise 49: Library Book Management System - SOLUTION
# Difficulty: Intermediate
# Concepts: OOP, JSON, datetime, Collections, File I/O, Multiple classes

import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter

# SOLUTION

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn, total_copies=1):
        """
        Initialize book.

        Args:
            title: Book title
            author: Book author
            isbn: ISBN number
            total_copies: Number of copies available
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.times_borrowed = 0

    def borrow(self):
        """Borrow a copy if available."""
        if self.available_copies > 0:
            self.available_copies -= 1
            self.times_borrowed += 1
            return True
        return False

    def return_copy(self):
        """Return a borrowed copy."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'times_borrowed': self.times_borrowed
        }

    def __str__(self):
        """String representation."""
        status = f"{self.available_copies}/{self.total_copies} available"
        return f"'{self.title}' by {self.author} ({status})"

class Member:
    """Represents a library member."""

    def __init__(self, name, member_id):
        """
        Initialize member.

        Args:
            name: Member name
            member_id: Unique member ID
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}  # {isbn: borrow_date}
        self.history = []  # List of (isbn, borrow_date, return_date) tuples

    def borrow_book(self, isbn):
        """Record borrowing a book."""
        if isbn in self.borrowed_books:
            return False
        self.borrowed_books[isbn] = datetime.now().isoformat()
        return True

    def return_book(self, isbn):
        """Record returning a book."""
        if isbn not in self.borrowed_books:
            return False

        borrow_date = self.borrowed_books[isbn]
        return_date = datetime.now().isoformat()
        self.history.append((isbn, borrow_date, return_date))
        del self.borrowed_books[isbn]
        return True

    def get_borrowed_count(self):
        """Get number of currently borrowed books."""
        return len(self.borrowed_books)

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': self.borrowed_books,
            'history': self.history
        }

    def __str__(self):
        """String representation."""
        return f"Member #{self.member_id}: {self.name} ({self.get_borrowed_count()} books borrowed)"

class Library:
    """Manages library books and members."""

    LOAN_PERIOD_DAYS = 14
    LATE_FEE_PER_DAY = 1.00

    def __init__(self, name, filename="library_data.json"):
        """
        Initialize library.

        Args:
            name: Library name
            filename: JSON file for persistence
        """
        self.name = name
        self.filename = filename
        self.books = {}  # {isbn: Book}
        self.members = {}  # {member_id: Member}
        self.next_member_id = 1
        self.load_data()

    def add_book(self, title, author, isbn, copies=1):
        """
        Add a book to the library.

        Args:
            title: Book title
            author: Author name
            isbn: ISBN number
            copies: Number of copies
        """
        if isbn in self.books:
            # Add more copies to existing book
            self.books[isbn].total_copies += copies
            self.books[isbn].available_copies += copies
            print(f"Added {copies} more copies of '{title}'")
        else:
            # Add new book
            book = Book(title, author, isbn, copies)
            self.books[isbn] = book
            print(f"Added new book: {book}")
        self.save_data()

    def remove_book(self, isbn):
        """Remove a book from the library."""
        if isbn in self.books:
            book = self.books.pop(isbn)
            print(f"Removed book: {book.title}")
            self.save_data()
            return True
        print(f"Book with ISBN {isbn} not found")
        return False

    def register_member(self, name):
        """
        Register a new member.

        Args:
            name: Member name

        Returns:
            int: New member ID
        """
        member = Member(name, self.next_member_id)
        self.members[self.next_member_id] = member
        print(f"Registered new member: {member}")
        self.next_member_id += 1
        self.save_data()
        return member.member_id

    def borrow_book(self, member_id, isbn):
        """
        Process book borrowing.

        Args:
            member_id: Member ID
            isbn: Book ISBN

        Returns:
            bool: True if successful
        """
        # Validate member
        if member_id not in self.members:
            print(f"Member {member_id} not found")
            return False

        # Validate book
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        # Check if book is available
        if not book.borrow():
            print(f"'{book.title}' is not available")
            return False

        # Record borrowing
        if not member.borrow_book(isbn):
            book.return_copy()  # Rollback
            print(f"{member.name} already has this book")
            return False

        due_date = datetime.now() + timedelta(days=self.LOAN_PERIOD_DAYS)
        print(f"✓ {member.name} borrowed '{book.title}'")
        print(f"  Due date: {due_date.strftime('%Y-%m-%d')}")

        self.save_data()
        return True

    def return_book(self, member_id, isbn):
        """
        Process book return and calculate late fees.

        Args:
            member_id: Member ID
            isbn: Book ISBN

        Returns:
            float: Late fee amount
        """
        # Validate member
        if member_id not in self.members:
            print(f"Member {member_id} not found")
            return 0

        # Validate book
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found")
            return 0

        member = self.members[member_id]
        book = self.books[isbn]

        # Check if member has this book
        if isbn not in member.borrowed_books:
            print(f"{member.name} doesn't have '{book.title}'")
            return 0

        # Calculate late fee
        borrow_date_str = member.borrowed_books[isbn]
        borrow_date = datetime.fromisoformat(borrow_date_str)
        due_date = borrow_date + timedelta(days=self.LOAN_PERIOD_DAYS)
        return_date = datetime.now()

        days_late = (return_date - due_date).days
        late_fee = max(0, days_late * self.LATE_FEE_PER_DAY)

        # Process return
        member.return_book(isbn)
        book.return_copy()

        print(f"✓ {member.name} returned '{book.title}'")
        if late_fee > 0:
            print(f"  ⚠️  {days_late} days late - Late fee: ${late_fee:.2f}")
        else:
            print(f"  Returned on time!")

        self.save_data()
        return late_fee

    def search_books(self, query):
        """
        Search books by title or author.

        Args:
            query: Search query

        Returns:
            list: Matching books
        """
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or
                query in book.author.lower()):
                results.append(book)
        return results

    def get_member_borrowed_books(self, member_id):
        """Get list of books currently borrowed by member."""
        if member_id not in self.members:
            return []

        member = self.members[member_id]
        borrowed = []

        for isbn, borrow_date_str in member.borrowed_books.items():
            if isbn in self.books:
                book = self.books[isbn]
                borrow_date = datetime.fromisoformat(borrow_date_str)
                due_date = borrow_date + timedelta(days=self.LOAN_PERIOD_DAYS)
                days_until_due = (due_date - datetime.now()).days

                borrowed.append({
                    'book': book,
                    'borrow_date': borrow_date,
                    'due_date': due_date,
                    'days_until_due': days_until_due
                })

        return borrowed

    def show_statistics(self):
        """Display library statistics."""
        print(f"\n{'='*60}")
        print(f"{self.name} - STATISTICS")
        print(f"{'='*60}")

        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books

        print(f"\nBooks:")
        print(f"  Unique titles: {len(self.books)}")
        print(f"  Total copies: {total_books}")
        print(f"  Available: {available_books}")
        print(f"  Borrowed: {borrowed_books}")

        print(f"\nMembers:")
        print(f"  Total members: {len(self.members)}")
        active_members = sum(1 for m in self.members.values()
                           if m.get_borrowed_count() > 0)
        print(f"  Active members: {active_members}")

        # Most borrowed books
        if self.books:
            print(f"\nMost borrowed books:")
            sorted_books = sorted(self.books.values(),
                                key=lambda b: b.times_borrowed,
                                reverse=True)
            for i, book in enumerate(sorted_books[:5], 1):
                print(f"  {i}. {book.title} ({book.times_borrowed} times)")

        print(f"{'='*60}\n")

    def save_data(self):
        """Save library data to JSON."""
        data = {
            'name': self.name,
            'next_member_id': self.next_member_id,
            'books': [book.to_dict() for book in self.books.values()],
            'members': [member.to_dict() for member in self.members.values()]
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        """Load library data from JSON."""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)

            self.name = data.get('name', self.name)
            self.next_member_id = data.get('next_member_id', 1)

            # Load books
            for book_data in data.get('books', []):
                book = Book(
                    book_data['title'],
                    book_data['author'],
                    book_data['isbn'],
                    book_data['total_copies']
                )
                book.available_copies = book_data['available_copies']
                book.times_borrowed = book_data.get('times_borrowed', 0)
                self.books[book.isbn] = book

            # Load members
            for member_data in data.get('members', []):
                member = Member(
                    member_data['name'],
                    member_data['member_id']
                )
                member.borrowed_books = member_data.get('borrowed_books', {})
                member.history = member_data.get('history', [])
                self.members[member.member_id] = member

            print(f"Loaded library data: {len(self.books)} books, {len(self.members)} members")

        except FileNotFoundError:
            print(f"No existing library data found. Starting fresh.")

# Test the library system
print("="*60)
print("LIBRARY MANAGEMENT SYSTEM DEMO")
print("="*60)

# Create library
library = Library("City Public Library", "demo_library.json")

# Add books
print("\n--- Adding Books ---")
library.add_book("1984", "George Orwell", "978-0451524935", 3)
library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 2)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 2)
library.add_book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1)

# Register members
print("\n--- Registering Members ---")
alice_id = library.register_member("Alice Smith")
bob_id = library.register_member("Bob Johnson")
charlie_id = library.register_member("Charlie Brown")

# Borrow books
print("\n--- Borrowing Books ---")
library.borrow_book(alice_id, "978-0451524935")
library.borrow_book(alice_id, "978-0060935467")
library.borrow_book(bob_id, "978-0743273565")

# Show borrowed books
print(f"\n--- {library.members[alice_id].name}'s Borrowed Books ---")
for item in library.get_member_borrowed_books(alice_id):
    book = item['book']
    days = item['days_until_due']
    status = "OVERDUE" if days < 0 else f"{days} days remaining"
    print(f"  • {book.title} - Due: {item['due_date'].strftime('%Y-%m-%d')} ({status})")

# Search books
print("\n--- Searching Books ---")
results = library.search_books("the")
print(f"Search results for 'the':")
for book in results:
    print(f"  • {book}")

# Return books
print("\n--- Returning Books ---")
library.return_book(alice_id, "978-0451524935")

# Show statistics
library.show_statistics()

# Display all books
print("--- Library Catalog ---")
for book in library.books.values():
    print(f"  • {book}")

# Display all members
print(f"\n--- Members ---")
for member in library.members.values():
    print(f"  • {member}")

"""
EXPLANATION:
1. Three classes handle different concerns: Book, Member, Library
2. Library class coordinates between books and members
3. datetime tracks borrow/due/return dates
4. Late fees calculated based on days overdue
5. JSON persistence saves entire library state
6. Search functionality finds books by title/author
7. Statistics provide overview of library activity

Key Concepts:
- Multiple classes working together (composition)
- Each class has single responsibility
- Data persistence with JSON
- Business logic (late fees, loan periods)
- Error handling and validation
- User-friendly output and feedback
- Complete CRUD operations (Create, Read, Update, Delete)
"""

print("\n" + "="*60)
print("Library system demonstration complete!")
print("="*60)
