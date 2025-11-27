# Exercise 2: Even or Odd Checker - SOLUTION
# Difficulty: Beginner
# Concepts: Control flow (if/else), Modulo operator, Comparison operators

# SOLUTION
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Get input from user
number = int(input("Enter a number: "))

# Check and display result
if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")

"""
EXPLANATION:
1. We define a function is_even() that returns True if a number is even, False otherwise
2. The modulo operator (%) returns the remainder after division
3. If number % 2 equals 0, the number is even (no remainder)
4. We use an if/else statement to print the appropriate message

Key Concepts:
- The modulo operator (%) is useful for checking divisibility
- Comparison operator == checks for equality
- Boolean values (True/False) are returned from comparisons
- if/else allows us to execute different code based on conditions
"""

# Extension solution: Check multiple numbers
print("\n--- EXTENSION SOLUTION ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 23, 28]
even_count = 0
odd_count = 0

print(f"Checking numbers: {numbers}")

for num in numbers:
    if is_even(num):
        even_count += 1
        print(f"{num} is even")
    else:
        odd_count += 1
        print(f"{num} is odd")

print(f"\nSummary: {even_count} even numbers, {odd_count} odd numbers")
