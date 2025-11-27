# Exercise 33: Lambda Functions and Sorting
# Difficulty: Intermediate-
# Concepts: Lambda functions, Sorting, Anonymous functions

"""
PROBLEM:
You have a list of student dictionaries. Use lambda functions to sort the students
by different criteria:
1. Sort by name (alphabetically)
2. Sort by grade (highest to lowest)
3. Sort by age (youngest to oldest)

Students list:
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Charlie', 'age': 21, 'grade': 78},
    {'name': 'Diana', 'age': 19, 'grade': 95}
]

EXAMPLE:
Input: Sort by grade (highest first)
Output: [
    {'name': 'Diana', 'age': 19, 'grade': 95},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Charlie', 'age': 21, 'grade': 78}
]

HINTS:
1. Use the sorted() function with the key parameter
2. Lambda functions are perfect for simple sorting keys: lambda x: x['field']
3. Use reverse=True for descending order

EXTENSION:
Create a function that sorts students by multiple criteria: first by grade (descending),
then by name (alphabetically) for students with the same grade.
"""

# Write your solution here
