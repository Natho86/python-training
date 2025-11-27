# Exercise 36: Create a Simple Class
# Difficulty: Intermediate-
# Concepts: Classes, Objects, Methods, Attributes, __init__

"""
PROBLEM:
Create a Book class that represents a book with the following:
- Attributes: title, author, pages, current_page (starts at 0)
- Methods:
  - read(pages): advances current_page by the given number of pages
  - progress(): returns a string showing reading progress as a percentage
  - is_finished(): returns True if the book is completely read

EXAMPLE:
book = Book("1984", "George Orwell", 328)
print(book.progress())  # "0% complete"

book.read(100)
print(book.progress())  # "30% complete"

book.read(228)
print(book.is_finished())  # True

HINTS:
1. Use __init__ method to initialize attributes when creating an object
2. self refers to the instance of the class
3. Methods are functions defined inside a class that take self as first parameter

EXTENSION:
Add a __str__ method that returns a nicely formatted string representation of the book,
and add a bookmark feature that remembers a specific page number.
"""

# Write your solution here
