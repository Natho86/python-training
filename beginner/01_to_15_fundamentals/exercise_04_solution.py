# Exercise 4: FizzBuzz - SOLUTION
# Difficulty: Beginner
# Concepts: Loops (for loop with range), Control flow, Modulo operator, Logical operators

# SOLUTION
def fizzbuzz(n):
    """Print FizzBuzz sequence from 1 to n."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run FizzBuzz for 1 to 100
fizzbuzz(100)

"""
EXPLANATION:
1. We use a for loop with range(1, n + 1) to iterate from 1 to n (inclusive)
2. We check conditions in order:
   - First: divisible by both 3 AND 5 (using the 'and' operator)
   - Second: divisible by 3 only
   - Third: divisible by 5 only
   - Otherwise: print the number itself
3. Order matters! We must check the "both" condition first

Key Concepts:
- for loops iterate over a sequence (in this case, a range of numbers)
- range(1, 101) generates numbers from 1 to 100 (the end is exclusive)
- Logical operator 'and' checks if both conditions are true
- Order of if/elif matters - first matching condition wins
- A number divisible by both 3 and 5 is divisible by 15
"""

# Alternative solution using modulo 15
print("\n--- ALTERNATIVE SOLUTION ---")

def fizzbuzz_v2(n):
    """Alternative FizzBuzz using modulo 15."""
    for i in range(1, n + 1):
        if i % 15 == 0:  # Divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz_v2(30)  # Print first 30 for demonstration

# Extension solution: Customizable FizzBuzz
print("\n--- EXTENSION SOLUTION ---")

def custom_fizzbuzz(start, end, num1, num2, word1, word2):
    """Customizable FizzBuzz with any numbers and words."""
    for i in range(start, end + 1):
        output = ""
        if i % num1 == 0:
            output += word1
        if i % num2 == 0:
            output += word2

        if output:
            print(output)
        else:
            print(i)

# Example: Numbers 1-50, replace multiples of 2 with "Beep" and 7 with "Boop"
custom_fizzbuzz(1, 50, 2, 7, "Beep", "Boop")
