# Exercise 23: List Comprehensions Basics - SOLUTION
# Difficulty: Beginner+
# Concepts: List comprehensions, Filtering, Transformations

# SOLUTION
print("LIST COMPREHENSIONS DEMONSTRATION")
print("=" * 60)

# 1. Creating lists with comprehensions
print("1. BASIC LIST COMPREHENSIONS")

# Squares of numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares 1-10: {squares}")

# Cubes
cubes = [x**3 for x in range(1, 6)]
print(f"Cubes 1-5: {cubes}")

# String repetition
words = [f"Python{i}" for i in range(1, 6)]
print(f"Words: {words}")
print()

# 2. Filtering with comprehensions
print("2. FILTERING WITH CONDITIONS")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

# Even numbers only
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Odd numbers only
odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Numbers greater than 5
greater_than_5 = [x for x in numbers if x > 5]
print(f"Greater than 5: {greater_than_5}")
print()

# 3. Transforming and filtering combined
print("3. TRANSFORM AND FILTER")

# Double the even numbers
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]
print(f"Doubled evens: {doubled_evens}")

# Square odd numbers
squared_odds = [x**2 for x in numbers if x % 2 != 0]
print(f"Squared odds: {squared_odds}")
print()

# 4. Working with strings
print("4. STRING TRANSFORMATIONS")

words = ["hello", "world", "python", "programming"]
print(f"Original words: {words}")

# Uppercase all words
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# First letter of each word
first_letters = [word[0] for word in words]
print(f"First letters: {first_letters}")

# Words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")
print()

# 5. Creating tuples in comprehensions
print("5. CREATING TUPLES")

# Number and its square
num_and_square = [(x, x**2) for x in range(1, 6)]
print(f"(Number, Square): {num_and_square}")

# Number, square, and cube
num_powers = [(x, x**2, x**3) for x in range(1, 6)]
print(f"(Number, Square, Cube):")
for num, square, cube in num_powers:
    print(f"  {num}: {square}, {cube}")

"""
EXPLANATION:
1. List comprehensions create new lists in a single line
2. Basic syntax: [expression for item in iterable]
3. With filter: [expression for item in iterable if condition]
4. Expression can be any valid Python expression
5. Much more concise than equivalent for loops
6. Generally faster than traditional loops for simple operations

Key Concepts:
- Comprehensions are "Pythonic" - they're idiomatic Python
- They create new lists (don't modify originals)
- Can be more readable for simple transformations
- Should be kept simple - complex logic is better in regular loops
"""

# Comparison with traditional loops
print("\n--- COMPARISON: COMPREHENSION VS LOOP ---")

# Traditional loop
squares_loop = []
for x in range(1, 11):
    squares_loop.append(x**2)
print(f"Using loop: {squares_loop}")

# List comprehension (equivalent)
squares_comp = [x**2 for x in range(1, 11)]
print(f"Using comprehension: {squares_comp}")

print("\nThe comprehension is more concise and often faster!")

# Multiple conditions
print("\n--- MULTIPLE CONDITIONS ---")

# Numbers divisible by 2 AND 3
numbers = range(1, 31)
div_by_2_and_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Divisible by both 2 and 3: {div_by_2_and_3}")

# Numbers divisible by 2 OR 3
div_by_2_or_3 = [x for x in numbers if x % 2 == 0 or x % 3 == 0]
print(f"Divisible by 2 or 3: {div_by_2_or_3}")

# Extension solution: Nested comprehensions
print("\n--- EXTENSION SOLUTION: NESTED COMPREHENSIONS ---")

# Create a 2D matrix (multiplication table)
matrix = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table (5x5):")
for row in matrix:
    print(row)

# Flatten a 2D list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in nested_list for num in row]
print(f"\nNested: {nested_list}")
print(f"Flattened: {flattened}")

# Create coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"\nAll coordinates (0-2, 0-2): {coordinates}")

# Filter coordinates
filtered_coords = [(x, y) for x in range(5) for y in range(5) if x + y < 5]
print(f"Coords where x+y < 5: {filtered_coords}")

# Advanced examples
print("\n--- ADVANCED EXAMPLES ---")

# Conditional expression in comprehension (if-else)
numbers = range(-5, 6)
abs_or_square = [x if x >= 0 else x**2 for x in numbers]
print(f"Numbers: {list(numbers)}")
print(f"Positive->keep, Negative->square: {abs_or_square}")

# Working with dictionaries
print("\n--- DICTIONARY COMPREHENSIONS ---")

# Create dictionary from lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = {k: v for k, v in zip(keys, values)}
print(f"Dictionary from lists: {dictionary}")

# Square numbers as dictionary
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Filter dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"All scores: {scores}")
print(f"High scores (>=90): {high_scores}")

# Set comprehensions
print("\n--- SET COMPREHENSIONS ---")

# Create set of unique lengths
words = ["hello", "world", "python", "hi", "programming", "code"]
lengths = {len(word) for word in words}
print(f"Words: {words}")
print(f"Unique lengths: {lengths}")

# Performance comparison
print("\n--- PERFORMANCE COMPARISON ---")
import time

# Traditional loop
start = time.time()
result1 = []
for i in range(100000):
    if i % 2 == 0:
        result1.append(i ** 2)
loop_time = time.time() - start

# List comprehension
start = time.time()
result2 = [i ** 2 for i in range(100000) if i % 2 == 0]
comp_time = time.time() - start

print(f"Traditional loop time: {loop_time:.4f} seconds")
print(f"Comprehension time: {comp_time:.4f} seconds")
print(f"Comprehension is {loop_time/comp_time:.2f}x faster!")

# When NOT to use comprehensions
print("\n--- WHEN NOT TO USE COMPREHENSIONS ---")

# TOO COMPLEX - use regular loop instead
# Don't do this:
# result = [func1(func2(x)) if x > 0 else func3(x) if x < 0 else 0
#           for x in data if len(x) > 5 and x.startswith('a')]

# Better readability with regular loop:
# result = []
# for x in data:
#     if len(x) > 5 and x.startswith('a'):
#         if x > 0:
#             result.append(func1(func2(x)))
#         elif x < 0:
#             result.append(func3(x))
#         else:
#             result.append(0)

print("Rule of thumb: If comprehension spans multiple lines or is hard")
print("to read, use a regular loop instead!")

# Practical examples
print("\n--- PRACTICAL EXAMPLES ---")

# Extract data from records
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 95}
]

# Get all names
names = [student['name'] for student in students]
print(f"Student names: {names}")

# Get names of students with grade >= 90
top_students = [s['name'] for s in students if s['grade'] >= 90]
print(f"Top students: {top_students}")

# Create grade report
report = [f"{s['name']}: {s['grade']}" for s in students]
print("Grade report:")
for line in report:
    print(f"  {line}")
