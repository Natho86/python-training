# Exercise 31: Flexible Sum Function with *args - SOLUTION
# Difficulty: Intermediate-
# Concepts: *args, Variable arguments, Functions

# SOLUTION
def flexible_sum(*args):
    """Sum any number of numeric arguments."""
    return sum(args)

# Test cases
print("Testing flexible_sum:")
print(f"flexible_sum(1, 2, 3) = {flexible_sum(1, 2, 3)}")
print(f"flexible_sum(10, 20, 30, 40, 50) = {flexible_sum(10, 20, 30, 40, 50)}")
print(f"flexible_sum(5) = {flexible_sum(5)}")
print(f"flexible_sum(1.5, 2.5, 3.0) = {flexible_sum(1.5, 2.5, 3.0)}")
print(f"flexible_sum() = {flexible_sum()}")  # Empty call returns 0

"""
EXPLANATION:
1. The *args syntax in the function parameter allows accepting any number of arguments
2. Inside the function, args is a tuple containing all passed arguments
3. We use the built-in sum() function to add all numbers in the tuple
4. This works with 0, 1, or many arguments
5. sum() returns 0 for an empty tuple, which is mathematically correct

Key Concepts:
- *args collects all positional arguments into a tuple
- The name 'args' is convention; you could use *numbers or *values
- args can be iterated like any tuple
- This pattern is useful for creating flexible, reusable functions
"""

# Alternative solution using manual iteration
print("\n--- ALTERNATIVE SOLUTION ---")

def flexible_sum_manual(*args):
    """Sum any number of arguments using manual iteration."""
    total = 0
    for num in args:
        total += num
    return total

print(f"flexible_sum_manual(1, 2, 3, 4, 5) = {flexible_sum_manual(1, 2, 3, 4, 5)}")

# Extension solution: Flexible operations
print("\n--- EXTENSION SOLUTION ---")

def flexible_operation(operation, *args):
    """
    Perform an operation on any number of arguments.

    Args:
        operation: '+', '*', 'min', or 'max'
        *args: Numbers to operate on
    """
    if not args:
        return None

    if operation == '+':
        return sum(args)
    elif operation == '*':
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == 'min':
        return min(args)
    elif operation == 'max':
        return max(args)
    else:
        return f"Unknown operation: {operation}"

print(f"flexible_operation('+', 1, 2, 3, 4) = {flexible_operation('+', 1, 2, 3, 4)}")
print(f"flexible_operation('*', 2, 3, 4) = {flexible_operation('*', 2, 3, 4)}")
print(f"flexible_operation('min', 5, 2, 8, 1) = {flexible_operation('min', 5, 2, 8, 1)}")
print(f"flexible_operation('max', 5, 2, 8, 1) = {flexible_operation('max', 5, 2, 8, 1)}")
