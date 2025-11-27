# Exercise 27: Custom Exceptions
# Difficulty: Intermediate-
# Concepts: Raising exceptions, Custom exceptions, Exception classes

"""
PROBLEM:
Create custom exceptions for specific error scenarios:
1. Create a custom exception class
2. Raise exceptions with custom messages
3. Use custom exceptions in a validation system
4. Chain exceptions (exception from another exception)

EXAMPLE:
Custom exception: InvalidAgeError
Usage: Validate user age (must be 0-120)

Input: age = -5
Output: InvalidAgeError: Age cannot be negative: -5

Input: age = 150
Output: InvalidAgeError: Age cannot exceed 120: 150

HINTS:
1. Custom exceptions inherit from Exception class
2. Use raise keyword to throw exceptions
3. Add __init__ and __str__ methods for custom behavior
4. Can include additional attributes in custom exceptions
5. Use specific exceptions for specific error types

EXTENSION:
Create a user registration system with multiple custom exceptions.
Implement exception hierarchy (base exception with specific subclasses).
Add validation methods that raise appropriate custom exceptions.
"""

# Write your solution here
