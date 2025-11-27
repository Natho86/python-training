# Python Debugging Tips and Common Errors

A guide to understanding, preventing, and fixing common Python errors.

## Table of Contents
- [Debugging Strategies](#debugging-strategies)
- [Common Errors and Solutions](#common-errors-and-solutions)
- [Reading Error Messages](#reading-error-messages)
- [Debugging Tools](#debugging-tools)
- [Best Practices](#best-practices)

---

## Debugging Strategies

### 1. Read the Error Message
Python's error messages are helpful! They tell you:
- **What** went wrong
- **Where** it happened (file and line number)
- **Why** it happened (error type)

### 2. Print Debugging
The simplest and most effective debugging method:

```python
# Print variable values
print(f"x = {x}")

# Print type information
print(f"Type of x: {type(x)}")

# Print at different stages
print("Before calculation")
result = complex_calculation()
print(f"After calculation: {result}")
```

### 3. Divide and Conquer
If you have a bug:
1. Comment out half the code
2. See if the error still occurs
3. Narrow down the problematic section
4. Repeat until you find the exact line

### 4. Rubber Duck Debugging
Explain your code line-by-line to a rubber duck (or any object). Often, you'll realize the problem while explaining it!

### 5. Use the Python Debugger (pdb)
```python
import pdb

x = 10
pdb.set_trace()  # Execution will pause here
y = x * 2
```

---

## Common Errors and Solutions

### 1. SyntaxError: invalid syntax

**What it means**: Python can't understand your code's structure.

**Common causes**:
```python
# Missing colon
if x > 5
    print("Greater")

# FIX:
if x > 5:
    print("Greater")

# Mismatched parentheses
result = (10 + 20
print(result)

# FIX:
result = (10 + 20)
print(result)

# Missing quotes
name = "Alice
print(name)

# FIX:
name = "Alice"
print(name)
```

**How to fix**:
- Check for missing colons after if, for, while, def, class
- Count your parentheses, brackets, and quotes
- Look at the line BEFORE the error (Python often reports the line after)

---

### 2. IndentationError

**What it means**: Your code indentation is inconsistent.

**Common causes**:
```python
# Mixing tabs and spaces
def my_function():
    x = 10
        return x  # Too much indentation

# FIX:
def my_function():
    x = 10
    return x

# Missing indentation
def greet():
print("Hello")

# FIX:
def greet():
    print("Hello")
```

**How to fix**:
- Use 4 spaces for indentation (recommended)
- Don't mix tabs and spaces
- Make sure all code inside blocks is indented

---

### 3. NameError: name 'x' is not defined

**What it means**: You're using a variable that doesn't exist.

**Common causes**:
```python
# Typo in variable name
name = "Alice"
print(nane)  # Typo

# FIX:
name = "Alice"
print(name)

# Using variable before defining it
print(age)
age = 30

# FIX:
age = 30
print(age)

# Variable out of scope
def my_function():
    x = 10

print(x)  # x doesn't exist here

# FIX:
def my_function():
    x = 10
    return x

result = my_function()
print(result)
```

**How to fix**:
- Check spelling carefully
- Make sure variables are defined before use
- Check variable scope (local vs global)

---

### 4. TypeError

**What it means**: Operation not supported for this type.

**Common causes**:
```python
# Can't concatenate different types
age = 30
print("Age: " + age)  # Can't add string and int

# FIX:
age = 30
print("Age: " + str(age))
# or
print(f"Age: {age}")

# Can't use wrong type in operation
result = "5" + 3

# FIX:
result = int("5") + 3
# or
result = "5" + str(3)

# Calling non-function
x = 10
x()  # x is not a function

# FIX: Make sure you're calling actual functions
```

**How to fix**:
- Check types with type(variable)
- Convert types explicitly (int(), str(), float())
- Make sure you're calling functions, not variables

---

### 5. IndexError: list index out of range

**What it means**: Trying to access an index that doesn't exist.

**Common causes**:
```python
numbers = [1, 2, 3]
print(numbers[3])  # Index 3 doesn't exist (only 0, 1, 2)

# FIX:
numbers = [1, 2, 3]
print(numbers[2])  # Last element is at index len-1

# Empty list
my_list = []
print(my_list[0])  # No elements!

# FIX:
my_list = []
if my_list:
    print(my_list[0])
else:
    print("List is empty")
```

**How to fix**:
- Remember: lists are 0-indexed
- Last element is at index len(list) - 1
- Check if list is empty before accessing
- Use len() to check list length

---

### 6. KeyError

**What it means**: Dictionary key doesn't exist.

**Common causes**:
```python
person = {"name": "Alice", "age": 30}
print(person["city"])  # Key 'city' doesn't exist

# FIX 1: Check if key exists
if "city" in person:
    print(person["city"])
else:
    print("City not found")

# FIX 2: Use .get() with default
print(person.get("city", "Unknown"))
```

**How to fix**:
- Use `key in dictionary` to check first
- Use `dictionary.get(key, default)` for safe access
- Use try/except to handle missing keys

---

### 7. ValueError

**What it means**: Correct type but inappropriate value.

**Common causes**:
```python
# Converting non-numeric string
age = int("abc")  # Can't convert "abc" to int

# FIX:
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a number!")

# Searching for value not in list
numbers = [1, 2, 3]
numbers.index(5)  # 5 not in list

# FIX:
if 5 in numbers:
    index = numbers.index(5)
else:
    print("Value not found")
```

**How to fix**:
- Validate input before conversion
- Use try/except for conversions
- Check if value exists before searching

---

### 8. AttributeError

**What it means**: Object doesn't have that attribute/method.

**Common causes**:
```python
# Typo in method name
text = "hello"
text.uppper()  # Typo: should be upper()

# FIX:
text.upper()

# Calling list method on string
text = "hello"
text.append("!")  # append() is for lists, not strings

# FIX:
text = text + "!"
# or
text_list = list(text)
text_list.append("!")
```

**How to fix**:
- Check spelling of methods
- Use dir(object) to see available methods
- Make sure you're using the right type

---

### 9. ZeroDivisionError

**What it means**: Division by zero.

**Common causes**:
```python
result = 10 / 0

# FIX:
denominator = 0
if denominator != 0:
    result = 10 / denominator
else:
    print("Cannot divide by zero")

# Or use try/except
try:
    result = 10 / denominator
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = None
```

---

### 10. FileNotFoundError

**What it means**: Trying to open a file that doesn't exist.

**Common causes**:
```python
with open("nonexistent.txt", "r") as f:
    content = f.read()

# FIX:
import os

filename = "data.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        content = f.read()
else:
    print(f"File {filename} not found")
```

---

## Reading Error Messages

### Anatomy of a Traceback

```
Traceback (most recent call last):
  File "my_script.py", line 10, in <module>
    result = divide(10, 0)
  File "my_script.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero
```

**Read from bottom to top**:
1. **Error type**: ZeroDivisionError
2. **Error message**: division by zero
3. **Where it happened**: line 5, in divide function
4. **Call chain**: shows how you got there (line 10 called divide)

---

## Debugging Tools

### 1. Print Statements
```python
def calculate(x, y):
    print(f"DEBUG: x={x}, y={y}, type(x)={type(x)}")
    result = x + y
    print(f"DEBUG: result={result}")
    return result
```

### 2. Assert Statements
```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero!"
    return a / b
```

### 3. Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("This is info")
logger.warning("This is a warning")
logger.error("This is an error")
```

### 4. Using dir() and help()
```python
# See all methods and attributes
dir(my_list)

# Get documentation
help(str.upper)
```

---

## Best Practices

### 1. Write Small Functions
Easier to test and debug:
```python
# Hard to debug
def process_data(data):
    # 100 lines of code...
    pass

# Easy to debug
def validate_data(data):
    # Check if data is valid
    pass

def transform_data(data):
    # Transform the data
    pass

def save_data(data):
    # Save the data
    pass
```

### 2. Use Meaningful Variable Names
```python
# Bad
d = {"n": "Alice", "a": 30}

# Good
person = {"name": "Alice", "age": 30}
```

### 3. Add Comments for Complex Logic
```python
# Calculate compound interest: A = P(1 + r/n)^(nt)
amount = principal * (1 + rate/periods) ** (periods * years)
```

### 4. Test Edge Cases
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test normal case
assert divide(10, 2) == 5

# Test edge cases
try:
    divide(10, 0)
    assert False, "Should have raised ValueError"
except ValueError:
    pass  # Expected
```

### 5. Use Try/Except for Expected Errors
```python
# User input might not be valid
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input! Using default age of 0")
    age = 0
```

---

## Quick Debugging Checklist

When you encounter an error:

- [ ] Read the error message completely
- [ ] Note the file name and line number
- [ ] Look at the line mentioned in the error
- [ ] Check the line BEFORE the error too
- [ ] Print variable values around the error
- [ ] Check variable types with type()
- [ ] Verify variable scope (local vs global)
- [ ] Check for typos in variable and function names
- [ ] Verify correct indentation
- [ ] Count parentheses, brackets, and quotes
- [ ] Test with simpler input
- [ ] Google the error message if still stuck

---

Remember: Debugging is a skill that improves with practice. Every error you fix makes you a better programmer!
