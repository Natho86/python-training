# Exercise 17: Dictionary Merger
# Difficulty: Beginner+
# Concepts: Dictionaries, Dictionary methods, Merging data

"""
PROBLEM:
Create a program that merges two dictionaries together. If a key exists in both
dictionaries, the value from the second dictionary should take precedence.
Also implement a version that adds the values together for common keys.

EXAMPLE:
Input: dict1 = {'a': 1, 'b': 2, 'c': 3}
       dict2 = {'b': 20, 'c': 30, 'd': 4}
Output (replace): {'a': 1, 'b': 20, 'c': 30, 'd': 4}
Output (add): {'a': 1, 'b': 22, 'c': 33, 'd': 4}

HINTS:
1. You can use the .update() method or the ** unpacking operator
2. For adding values, iterate through keys and check if they exist in both
3. Consider using .get() method with a default value of 0

EXTENSION:
Create a function that can merge any number of dictionaries (using *args).
Handle cases where values might be different types (strings, numbers, lists).
"""

# Write your solution here
