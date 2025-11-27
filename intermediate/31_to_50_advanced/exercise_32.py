# Exercise 32: Function with **kwargs
# Difficulty: Intermediate-
# Concepts: **kwargs, Keyword arguments, Dictionaries

"""
PROBLEM:
Create a function called build_profile() that accepts a first name and last name,
and any number of additional keyword arguments representing user information.
Return a dictionary containing all the profile information.

EXAMPLE:
Input: build_profile("John", "Doe", location="New York", age=30, job="Developer")
Output: {
    'first_name': 'John',
    'last_name': 'Doe',
    'location': 'New York',
    'age': 30,
    'job': 'Developer'
}

Input: build_profile("Jane", "Smith", email="jane@example.com", hobby="Photography")
Output: {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'email': 'jane@example.com',
    'hobby': 'Photography'
}

HINTS:
1. Use **kwargs to accept any number of keyword arguments
2. **kwargs collects keyword arguments into a dictionary
3. You can combine regular parameters with **kwargs

EXTENSION:
Create a create_car() function that takes make and model as required arguments,
then any optional features (color, year, transmission, etc.) and returns a formatted
string describing the car.
"""

# Write your solution here
