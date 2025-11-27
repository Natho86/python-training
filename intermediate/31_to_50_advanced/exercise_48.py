# Exercise 48: Custom Module Creation
# Difficulty: Intermediate
# Concepts: Modules, Imports, Code organization, Reusability

"""
PROBLEM:
Create a custom module called 'text_utils.py' with useful text processing functions:
1. word_count(text) - Count words in text
2. char_frequency(text) - Return character frequency dictionary
3. reverse_words(text) - Reverse order of words
4. title_case(text) - Convert to title case
5. remove_punctuation(text) - Remove all punctuation

Then create a main program that imports and uses these functions.

Also create a 'math_utils.py' module with:
1. is_prime(n) - Check if number is prime
2. factorial(n) - Calculate factorial
3. fibonacci(n) - Generate first n Fibonacci numbers
4. gcd(a, b) - Calculate greatest common divisor

EXAMPLE:
# In your main program:
from text_utils import word_count, reverse_words
from math_utils import is_prime, fibonacci

text = "Hello World Python"
print(word_count(text))  # 3
print(reverse_words(text))  # "Python World Hello"
print(is_prime(17))  # True
print(fibonacci(5))  # [0, 1, 1, 2, 3]

HINTS:
1. Create separate .py files for each module
2. Use def to define functions in the module
3. Import with: from module import function
4. Modules should have docstrings explaining their purpose
5. Test your modules with a separate test file

EXTENSION:
Add a 'data_utils.py' module with functions for data validation (email, phone, URL).
Create a package structure with __init__.py file.
"""

# Write your solution here
