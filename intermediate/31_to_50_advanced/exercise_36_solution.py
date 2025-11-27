# Exercise 36: Create a Simple Class - SOLUTION
# Difficulty: Intermediate-
# Concepts: Classes, Objects, Methods, Attributes, __init__

# SOLUTION
class Book:
    """Represents a book with reading progress tracking."""

    def __init__(self, title, author, pages):
        """
        Initialize a book.

        Args:
            title: Book title
            author: Book author
            pages: Total number of pages
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, num_pages):
        """
        Read a number of pages.

        Args:
            num_pages: Number of pages to read
        """
        self.current_page += num_pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        print(f"Read {num_pages} pages. Now on page {self.current_page}")

    def progress(self):
        """Return reading progress as a percentage string."""
        percentage = (self.current_page / self.pages) * 100
        return f"{percentage:.0f}% complete"

    def is_finished(self):
        """Check if book is completely read."""
        return self.current_page >= self.pages

# Test the Book class
print("=== Testing Book Class ===")
book = Book("1984", "George Orwell", 328)
print(f"Created: {book.title} by {book.author} ({book.pages} pages)")
print(f"Progress: {book.progress()}")

book.read(100)
print(f"Progress: {book.progress()}")

book.read(100)
print(f"Progress: {book.progress()}")

book.read(128)
print(f"Finished? {book.is_finished()}")

# Try reading past the end
book.read(50)
print(f"Progress: {book.progress()}")

"""
EXPLANATION:
1. class defines a blueprint for creating objects
2. __init__ is the constructor method called when creating a new instance
3. self refers to the specific instance of the class
4. Attributes (self.title, self.author) store data specific to each instance
5. Methods are functions that belong to the class and operate on its data
6. We create an instance with: book = Book("Title", "Author", 300)

Key Concepts:
- Classes group related data (attributes) and behavior (methods)
- __init__ initializes object state when created
- self is automatically passed to all instance methods
- Each instance has its own separate attributes
- Methods can modify instance state (self.current_page += num_pages)
"""

# Extension solution: Enhanced Book class
print("\n--- EXTENSION SOLUTION ---")

class EnhancedBook:
    """Enhanced book class with __str__ and bookmark features."""

    def __init__(self, title, author, pages):
        """Initialize book."""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.bookmark = None

    def __str__(self):
        """Return string representation of the book."""
        status = "Finished" if self.is_finished() else f"Page {self.current_page}/{self.pages}"
        bookmark_info = f" [Bookmark: page {self.bookmark}]" if self.bookmark else ""
        return f"'{self.title}' by {self.author} - {status}{bookmark_info}"

    def read(self, num_pages):
        """Read pages."""
        self.current_page = min(self.current_page + num_pages, self.pages)
        print(f"Read {num_pages} pages. Now on page {self.current_page}")

    def progress(self):
        """Return progress percentage."""
        percentage = (self.current_page / self.pages) * 100
        return f"{percentage:.0f}% complete"

    def is_finished(self):
        """Check if finished."""
        return self.current_page >= self.pages

    def set_bookmark(self, page=None):
        """
        Set a bookmark at a specific page.

        Args:
            page: Page number to bookmark (if None, uses current_page)
        """
        if page is None:
            page = self.current_page

        if 0 <= page <= self.pages:
            self.bookmark = page
            print(f"Bookmark set at page {page}")
        else:
            print(f"Invalid page number. Book has {self.pages} pages.")

    def go_to_bookmark(self):
        """Jump to bookmarked page."""
        if self.bookmark is not None:
            self.current_page = self.bookmark
            print(f"Jumped to bookmark at page {self.bookmark}")
        else:
            print("No bookmark set!")

# Test enhanced book
print("\nTesting Enhanced Book:")
book2 = EnhancedBook("The Hobbit", "J.R.R. Tolkien", 310)
print(book2)  # Calls __str__ automatically

book2.read(150)
book2.set_bookmark()  # Bookmark current page
print(book2)

book2.read(100)
print(f"Current: {book2}")

book2.go_to_bookmark()  # Go back to bookmark
print(book2)

# Multiple instances demonstration
print("\n--- MULTIPLE INSTANCES ---")
book1 = EnhancedBook("Python Crash Course", "Eric Matthes", 544)
book2 = EnhancedBook("Clean Code", "Robert Martin", 464)

book1.read(200)
book2.read(100)

print(f"Book 1: {book1}")
print(f"Book 2: {book2}")
print("\nEach instance has independent state!")
