# Exercise 34: Map, Filter, and Reduce
# Difficulty: Intermediate-
# Concepts: Map, Filter, Reduce, Functional programming

"""
PROBLEM:
Given a list of numbers, use map(), filter(), and reduce() to:
1. Square all numbers using map()
2. Filter out odd numbers using filter()
3. Calculate the product of all remaining numbers using reduce()

Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

EXAMPLE:
Step 1 - Map (square): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Step 2 - Filter (evens only): [4, 16, 36, 64, 100]
Step 3 - Reduce (product): 4 * 16 * 36 * 64 * 100 = 14,745,600

HINTS:
1. map(function, iterable) applies function to each element
2. filter(function, iterable) keeps elements where function returns True
3. reduce() is in the functools module: from functools import reduce
4. You can chain these operations together

EXTENSION:
Create a data processing pipeline that takes a list of strings (prices like "$12.99"),
converts them to floats, filters out prices above $50, and calculates the total.
"""

# Write your solution here
