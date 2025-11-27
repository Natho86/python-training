# Exercise 35: Simple Timer Decorator
# Difficulty: Intermediate-
# Concepts: Decorators, Functions, Time measurement

"""
PROBLEM:
Create a decorator called timer that measures and prints how long a function takes to execute.
The decorator should print the function name and execution time in seconds.

EXAMPLE:
@timer
def slow_function():
    time.sleep(2)
    return "Done!"

Output when calling slow_function():
Function 'slow_function' took 2.00 seconds
Done!

HINTS:
1. A decorator is a function that takes a function as input and returns a new function
2. Use time.time() to get the current time before and after execution
3. Use functools.wraps to preserve the original function's metadata

EXTENSION:
Create a decorator that counts how many times a function has been called and prints
the count each time the function is invoked.
"""

# Write your solution here
