# Exercise 26: Basic Error Handling - SOLUTION
# Difficulty: Intermediate-
# Concepts: try/except blocks, Exception types, Error handling

# SOLUTION
print("ERROR HANDLING DEMONSTRATION")
print("=" * 60)

# 1. HANDLING DIVISION BY ZERO
print("1. DIVISION BY ZERO")
print("-" * 60)

def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print()

# 2. HANDLING INVALID INPUT
print("2. HANDLING INVALID INPUT")
print("-" * 60)

def get_integer_input(prompt):
    """Get integer input with error handling."""
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        return "Error: Please enter a valid integer"

# Simulating input without actual user interaction
def convert_to_int(value):
    """Convert string to integer with error handling."""
    try:
        return int(value)
    except ValueError:
        return f"Error: '{value}' is not a valid integer"

print(f"Convert '42': {convert_to_int('42')}")
print(f"Convert 'abc': {convert_to_int('abc')}")
print(f"Convert '3.14': {convert_to_int('3.14')}")
print()

# 3. HANDLING FILE NOT FOUND
print("3. HANDLING FILE NOT FOUND")
print("-" * 60)

def read_file_safe(filename):
    """Read file with error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"

print(read_file_safe('nonexistent.txt'))
print()

# 4. MULTIPLE EXCEPT BLOCKS
print("4. MULTIPLE EXCEPT BLOCKS")
print("-" * 60)

def process_data(data, index):
    """Process data with multiple error handlers."""
    try:
        value = int(data[index])
        result = 100 / value
        return f"Result: {result}"
    except IndexError:
        return "Error: Index out of range"
    except ValueError:
        return "Error: Cannot convert to integer"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception as e:
        return f"Unexpected error: {e}"

# Test different error scenarios
test_data = ['10', '20', 'abc', '0']
print(f"Process index 0: {process_data(test_data, 0)}")
print(f"Process index 2: {process_data(test_data, 2)}")
print(f"Process index 3: {process_data(test_data, 3)}")
print(f"Process index 10: {process_data(test_data, 10)}")
print()

# 5. TRY/EXCEPT/ELSE/FINALLY
print("5. TRY/EXCEPT/ELSE/FINALLY")
print("-" * 60)

def divide_with_finally(a, b):
    """Demonstrate try/except/else/finally."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Error occurred: Division by zero")
        return None
    except TypeError:
        print("  Error occurred: Invalid type")
        return None
    else:
        print("  Success: No errors occurred")
        return result
    finally:
        print("  Cleanup: This always executes")

print("Dividing 10 by 2:")
result = divide_with_finally(10, 2)
print(f"Result: {result}\n")

print("Dividing 10 by 0:")
result = divide_with_finally(10, 0)
print(f"Result: {result}\n")

"""
EXPLANATION:
1. try block contains code that might raise an exception
2. except block catches and handles specific exceptions
3. Multiple except blocks can handle different error types
4. else block runs if no exception occurred
5. finally block always runs (for cleanup), even if there's a return
6. Exceptions can be caught by type: ValueError, ZeroDivisionError, etc.
7. Generic Exception catches all exceptions (use as last resort)

Key Concepts:
- Error handling prevents program crashes
- Specific exceptions should be caught before generic ones
- finally is useful for cleanup (closing files, connections)
- Don't catch all exceptions unless you have a good reason
- Provide helpful error messages to users
"""

# Common exception types
print("\n--- COMMON EXCEPTION TYPES ---")
print("""
Common Built-in Exceptions:
- ValueError: Invalid value for operation
- TypeError: Invalid type for operation
- ZeroDivisionError: Division by zero
- IndexError: Index out of range
- KeyError: Dictionary key not found
- FileNotFoundError: File doesn't exist
- AttributeError: Invalid attribute reference
- NameError: Variable not defined
- IOError: Input/output operation failed
""")

# Extension solution: Robust calculator
print("\n--- EXTENSION SOLUTION: ROBUST CALCULATOR ---")

class SafeCalculator:
    """Calculator with comprehensive error handling."""

    def calculate(self, expression):
        """
        Evaluate a mathematical expression safely.

        Args:
            expression: String like "10 + 5" or "20 / 4"

        Returns:
            Result or error message
        """
        try:
            # Parse the expression
            parts = expression.strip().split()

            if len(parts) != 3:
                return "Error: Invalid format. Use: number operator number"

            num1_str, operator, num2_str = parts

            # Convert to numbers
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                return "Error: Invalid number format"

            # Perform operation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "Error: Cannot divide by zero"
                result = num1 / num2
            elif operator == '%':
                if num2 == 0:
                    return "Error: Cannot modulo by zero"
                result = num1 % num2
            elif operator == '**':
                if num1 == 0 and num2 < 0:
                    return "Error: 0 cannot be raised to negative power"
                result = num1 ** num2
            else:
                return f"Error: Unknown operator '{operator}'"

            return result

        except Exception as e:
            return f"Unexpected error: {str(e)}"

    def calculate_batch(self, expressions):
        """Calculate multiple expressions."""
        results = []
        for expr in expressions:
            result = self.calculate(expr)
            results.append(f"{expr} = {result}")
        return results

# Test the calculator
calc = SafeCalculator()

test_expressions = [
    "10 + 5",
    "20 - 8",
    "6 * 7",
    "15 / 3",
    "10 / 0",
    "abc + 5",
    "10",
    "10 ^ 2",
    "2 ** 8",
]

print("Calculator Results:")
for expr in test_expressions:
    result = calc.calculate(expr)
    print(f"  {expr:15} = {result}")

# File reader with fallback locations
print("\n--- FILE READER WITH FALLBACKS ---")

def read_file_with_fallbacks(filename, fallback_paths=None):
    """Try to read file from multiple locations."""
    if fallback_paths is None:
        fallback_paths = []

    paths_to_try = [filename] + fallback_paths

    for path in paths_to_try:
        try:
            with open(path, 'r') as file:
                content = file.read()
                print(f"Successfully read from: {path}")
                return content
        except FileNotFoundError:
            print(f"Not found: {path}")
            continue
        except PermissionError:
            print(f"No permission: {path}")
            continue

    return "Error: File not found in any location"

# Test with fallback locations
fallbacks = [
    'temp_files/config.txt',
    '/etc/config.txt',
    'backup/config.txt'
]
result = read_file_with_fallbacks('config.txt', fallbacks)

# Custom exception messages
print("\n--- CUSTOM EXCEPTION MESSAGES ---")

def withdraw_money(balance, amount):
    """Withdraw money with detailed error messages."""
    try:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > balance:
            raise ValueError(
                f"Insufficient funds. Balance: ${balance:.2f}, "
                f"Requested: ${amount:.2f}"
            )

        new_balance = balance - amount
        return f"Success! Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}"

    except TypeError as e:
        return f"Type Error: {str(e)}"
    except ValueError as e:
        return f"Value Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Test withdrawal function
print("\nTesting withdrawals:")
print(withdraw_money(100.00, 30.00))
print(withdraw_money(100.00, 150.00))
print(withdraw_money(100.00, -50.00))
print(withdraw_money(100.00, "fifty"))

# Nested try-except blocks
print("\n--- NESTED TRY-EXCEPT ---")

def process_user_data(data):
    """Process data with nested error handling."""
    try:
        # Outer try: handle overall operation
        print(f"Processing: {data}")

        try:
            # Inner try: handle specific operation
            result = int(data) * 2
            return f"Result: {result}"
        except ValueError:
            # Handle conversion error
            print("  Warning: Could not convert to integer, trying float")

            try:
                result = float(data) * 2
                return f"Result: {result}"
            except ValueError:
                return "Error: Not a valid number"

    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Test nested error handling
test_values = ['10', '3.14', 'abc', None]
print("\nNested error handling:")
for value in test_values:
    print(process_user_data(value))

# Best practices
print("\n--- ERROR HANDLING BEST PRACTICES ---")
print("""
1. Be Specific: Catch specific exceptions, not generic ones
2. Don't Silence Errors: Log or handle errors appropriately
3. Use Finally for Cleanup: Always clean up resources
4. Provide Context: Give users helpful error messages
5. Don't Overuse: Not all code needs try-except
6. Fail Fast: Catch errors close to where they occur
7. Document Exceptions: Note what exceptions a function can raise

Example of good error handling:
try:
    risky_operation()
except SpecificError as e:
    log_error(e)
    handle_gracefully()
finally:
    cleanup_resources()
""")

# Logging errors
print("\n--- ERROR LOGGING ---")

import datetime

def log_error(error_type, message, filename='temp_files/error.log'):
    """Log errors to a file."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {error_type}: {message}\n"

    try:
        with open(filename, 'a') as log_file:
            log_file.write(log_entry)
        return True
    except Exception as e:
        print(f"Could not write to log: {e}")
        return False

def safe_operation(value):
    """Perform operation with error logging."""
    try:
        result = 100 / int(value)
        return result
    except ZeroDivisionError as e:
        log_error("ZeroDivisionError", f"Attempted to divide by zero: {value}")
        return "Error logged: Division by zero"
    except ValueError as e:
        log_error("ValueError", f"Invalid value: {value}")
        return "Error logged: Invalid value"
    except Exception as e:
        log_error("Exception", f"Unexpected error: {str(e)}")
        return "Error logged: Unexpected error"

# Test with error logging
import os
if not os.path.exists('temp_files'):
    os.makedirs('temp_files')

print("Testing operations with error logging:")
print(safe_operation(10))
print(safe_operation(0))
print(safe_operation("abc"))

print("\nErrors have been logged to: temp_files/error.log")
