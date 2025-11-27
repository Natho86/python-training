# Exercise 3: Simple Calculator - SOLUTION
# Difficulty: Beginner
# Concepts: Arithmetic operators, Control flow (if/elif/else), Functions

# SOLUTION
def calculate(num1, num2, operation):
    """Perform calculation based on the operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation!"

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Calculate and display result
result = calculate(num1, num2, operation)

if isinstance(result, str):  # Check if result is an error message
    print(result)
else:
    print(f"Result: {num1} {operation} {num2} = {result}")

"""
EXPLANATION:
1. We create a calculate() function that takes two numbers and an operation
2. We use if/elif/else to check which operation was selected
3. For division, we check if num2 is 0 to avoid a division error
4. We use isinstance() to check if the result is an error message (string) or a number
5. The function returns the calculated result or an error message

Key Concepts:
- if/elif/else allows checking multiple conditions sequentially
- Division by zero causes an error, so we check for it explicitly
- isinstance() checks the type of a variable
- Returning different types (numbers or strings) based on conditions
"""

# Extension solution: More operations
print("\n--- EXTENSION SOLUTION ---")

def advanced_calculate(num1, num2, operation):
    """Perform calculation with extended operations."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    elif operation == '**':
        return num1 ** num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Modulo by zero!"
        return num1 % num2
    elif operation == '//':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 // num2
    else:
        return "Invalid operation!"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /, **, %, //): ")

result = advanced_calculate(num1, num2, operation)

if isinstance(result, str):
    print(result)
else:
    print(f"Result: {num1} {operation} {num2} = {result}")
