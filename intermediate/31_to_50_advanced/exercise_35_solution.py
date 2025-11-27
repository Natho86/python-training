# Exercise 35: Simple Timer Decorator - SOLUTION
# Difficulty: Intermediate-
# Concepts: Decorators, Functions, Time measurement

import time
from functools import wraps

# SOLUTION
def timer(func):
    """Decorator that measures function execution time."""
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.2f} seconds")
        return result
    return wrapper

# Test the decorator
@timer
def slow_function():
    """A function that takes 2 seconds."""
    time.sleep(2)
    return "Done!"

@timer
def calculate_sum(n):
    """Calculate sum of numbers from 1 to n."""
    total = sum(range(1, n + 1))
    return total

@timer
def quick_function():
    """A fast function."""
    return "Quick!"

print("Testing timer decorator:")
result1 = slow_function()
print(f"Result: {result1}\n")

result2 = calculate_sum(1000000)
print(f"Sum: {result2}\n")

result3 = quick_function()
print(f"Result: {result3}\n")

"""
EXPLANATION:
1. A decorator is a function that takes a function and returns a modified version
2. The @timer syntax is equivalent to: slow_function = timer(slow_function)
3. The wrapper function is what actually gets called when we call the decorated function
4. We use *args and **kwargs to accept any arguments the original function needs
5. time.time() returns the current time in seconds since epoch
6. @wraps(func) copies metadata (name, docstring) from original function

Key Concepts:
- Decorators modify function behavior without changing the function's code
- Wrapper functions allow us to add code before/after the original function
- *args and **kwargs make decorators work with any function signature
- @wraps preserves the original function's __name__ and __doc__
- Decorators are a form of "metaprogramming"
"""

# Show how decorators work without @ syntax
print("\n--- HOW DECORATORS WORK (without @ syntax) ---")

def greet(name):
    """Original greeting function."""
    return f"Hello, {name}!"

# Manually applying the decorator (equivalent to @timer)
greet_with_timer = timer(greet)
result = greet_with_timer("Alice")
print(result)

# Extension solution: Call counter decorator
print("\n--- EXTENSION SOLUTION ---")

def call_counter(func):
    """Decorator that counts how many times a function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call #{wrapper.count} to '{func.__name__}'")
        return func(*args, **kwargs)

    wrapper.count = 0  # Initialize counter attribute
    return wrapper

@call_counter
def say_hello(name):
    """Greet someone."""
    return f"Hello, {name}!"

print(say_hello("Alice"))
print(say_hello("Bob"))
print(say_hello("Charlie"))
print(f"\nTotal calls: {say_hello.count}")

# Bonus: Multiple decorators (stacking)
print("\n--- BONUS: STACKING DECORATORS ---")

def uppercase_decorator(func):
    """Decorator that converts result to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@call_counter
@uppercase_decorator
@timer
def get_message():
    """Get a message."""
    time.sleep(0.5)
    return "this will be uppercase"

# Decorators are applied bottom to top:
# 1. timer (innermost)
# 2. uppercase_decorator
# 3. call_counter (outermost)
print(get_message())

# More practical decorator examples
print("\n--- MORE DECORATOR EXAMPLES ---")

def debug(func):
    """Decorator that prints function calls and results."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    """Add two numbers."""
    return a + b

add(5, 3)
add(10, b=20)
