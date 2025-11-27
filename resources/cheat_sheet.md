# Python Quick Reference Cheat Sheet

A comprehensive reference for Python syntax, methods, and common patterns covered in this training.

## Table of Contents
- [Basic Syntax](#basic-syntax)
- [Data Types](#data-types)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Data Structures](#data-structures)
- [File Operations](#file-operations)
- [Object-Oriented Programming](#object-oriented-programming)
- [Common Modules](#common-modules)
- [List Comprehensions](#list-comprehensions)
- [Error Handling](#error-handling)

---

## Basic Syntax

### Variables and Assignment
```python
x = 10                  # Integer
name = "Alice"          # String
price = 19.99          # Float
is_active = True       # Boolean
```

### Comments
```python
# Single line comment

"""
Multi-line comment
or docstring
"""
```

### Print Output
```python
print("Hello")                    # Basic print
print(f"Value: {x}")             # f-string formatting
print("Name:", name)             # Multiple values
print(f"Price: ${price:.2f}")    # Format with 2 decimals
```

### Input
```python
name = input("Enter name: ")      # Returns string
age = int(input("Enter age: "))   # Convert to int
```

---

## Data Types

### Type Conversion
```python
int("42")          # String to integer
float("3.14")      # String to float
str(42)            # Integer to string
bool(1)            # To boolean (0 = False, else = True)
```

### Type Checking
```python
type(x)            # Get type of variable
isinstance(x, int) # Check if x is an integer
```

---

## Control Flow

### If/Elif/Else
```python
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Less")
```

### Comparison Operators
```python
==  # Equal
!=  # Not equal
<   # Less than
>   # Greater than
<=  # Less than or equal
>=  # Greater than or equal
```

### Logical Operators
```python
and  # Both conditions true
or   # At least one condition true
not  # Negate condition

if x > 5 and x < 10:
    print("Between 5 and 10")
```

---

## Functions

### Basic Function
```python
def greet(name):
    """Function with parameter and return value."""
    return f"Hello, {name}!"

result = greet("Alice")
```

### Default Parameters
```python
def greet(name="Guest"):
    return f"Hello, {name}!"

greet()          # Uses default: "Guest"
greet("Alice")   # Uses "Alice"
```

### Multiple Return Values
```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])
```

### *args and **kwargs
```python
def sum_all(*args):
    """Accept any number of arguments."""
    return sum(args)

def print_info(**kwargs):
    """Accept any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

sum_all(1, 2, 3, 4)                    # 10
print_info(name="Alice", age=30)        # name: Alice, age: 30
```

### Lambda Functions
```python
square = lambda x: x ** 2
add = lambda a, b: a + b

square(5)        # 25
add(3, 4)        # 7
```

---

## Data Structures

### Lists
```python
# Creating
numbers = [1, 2, 3, 4, 5]
empty = []

# Accessing
numbers[0]       # First element (1)
numbers[-1]      # Last element (5)
numbers[1:3]     # Slice: [2, 3]
numbers[:3]      # First 3: [1, 2, 3]
numbers[3:]      # From index 3: [4, 5]

# Modifying
numbers.append(6)        # Add to end
numbers.insert(0, 0)     # Insert at index
numbers.remove(3)        # Remove first occurrence
numbers.pop()            # Remove and return last
numbers.pop(0)           # Remove and return at index
numbers.clear()          # Remove all

# Useful Methods
len(numbers)             # Length
numbers.index(3)         # Find index of value
numbers.count(2)         # Count occurrences
numbers.sort()           # Sort in place
numbers.reverse()        # Reverse in place
sorted(numbers)          # Return sorted copy
numbers.copy()           # Create a copy

# Checking
3 in numbers             # True if 3 in list
```

### Tuples (Immutable)
```python
point = (10, 20)
x, y = point             # Unpacking

# Tuple methods
point.count(10)          # Count occurrences
point.index(20)          # Find index
```

### Dictionaries
```python
# Creating
person = {"name": "Alice", "age": 30}
empty = {}

# Accessing
person["name"]           # Get value (raises KeyError if not found)
person.get("name")       # Get value (returns None if not found)
person.get("city", "Unknown")  # Get with default value

# Modifying
person["age"] = 31       # Update
person["city"] = "NYC"   # Add new key
del person["age"]        # Delete key

# Useful Methods
person.keys()            # Get all keys
person.values()          # Get all values
person.items()           # Get (key, value) pairs
person.update({"age": 32})  # Update multiple

# Checking
"name" in person         # True if key exists
```

### Sets (Unique Values)
```python
# Creating
numbers = {1, 2, 3, 4, 5}
empty = set()

# Operations
numbers.add(6)           # Add element
numbers.remove(3)        # Remove (raises error if not found)
numbers.discard(3)       # Remove (no error if not found)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

a | b                    # Union: {1, 2, 3, 4, 5}
a & b                    # Intersection: {3}
a - b                    # Difference: {1, 2}
a ^ b                    # Symmetric difference: {1, 2, 4, 5}
```

---

## File Operations

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read lines into list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Writing Files
```python
# Write (overwrites existing)
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")
```

### CSV Files
```python
import csv

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
```

### JSON Files
```python
import json

# Reading JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Writing JSON
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## Object-Oriented Programming

### Basic Class
```python
class Person:
    """A simple Person class."""

    def __init__(self, name, age):
        """Constructor."""
        self.name = name
        self.age = age

    def greet(self):
        """Instance method."""
        return f"Hello, I'm {self.name}"

    def __str__(self):
        """String representation."""
        return f"Person({self.name}, {self.age})"

# Creating objects
person = Person("Alice", 30)
print(person.greet())
print(person)
```

### Inheritance
```python
class Student(Person):
    """Student inherits from Person."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

student = Student("Bob", 20, "S12345")
print(student.greet())  # Inherited method
print(student.study())  # New method
```

### Static Methods
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)  # No instance needed
```

---

## Common Modules

### datetime
```python
from datetime import datetime, timedelta

now = datetime.now()
today = datetime.today()
specific = datetime(2024, 12, 25)

# Formatting
now.strftime("%Y-%m-%d")      # "2024-11-27"
now.strftime("%B %d, %Y")     # "November 27, 2024"

# Parsing
date = datetime.strptime("2024-11-27", "%Y-%m-%d")

# Arithmetic
tomorrow = now + timedelta(days=1)
week_ago = now - timedelta(weeks=1)
```

### random
```python
import random

random.randint(1, 100)        # Random integer from 1-100
random.random()               # Random float from 0.0-1.0
random.choice([1, 2, 3])      # Random element from list
random.shuffle(my_list)       # Shuffle list in place
random.sample([1, 2, 3], 2)   # Random sample of 2 elements
```

### math
```python
import math

math.sqrt(16)                 # Square root: 4.0
math.ceil(3.2)                # Round up: 4
math.floor(3.8)               # Round down: 3
math.pi                       # 3.141592...
math.pow(2, 3)                # 2^3 = 8.0
```

### collections
```python
from collections import Counter, defaultdict, namedtuple

# Counter
counts = Counter([1, 2, 2, 3, 3, 3])
counts.most_common(2)         # [(3, 3), (2, 2)]

# defaultdict
d = defaultdict(int)          # Default value is 0
d["key"] += 1                 # No KeyError

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)
```

---

## List Comprehensions

### Basic List Comprehension
```python
# Create list of squares
squares = [x**2 for x in range(10)]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Transform strings
upper = [s.upper() for s in ["a", "b", "c"]]
```

### Dictionary Comprehension
```python
# Create dictionary
squares_dict = {x: x**2 for x in range(5)}

# Filter dictionary
filtered = {k: v for k, v in my_dict.items() if v > 10}
```

### Set Comprehension
```python
unique_squares = {x**2 for x in [1, 2, 2, 3, 3]}
```

---

## Error Handling

### Try/Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")
```

### Raising Exceptions
```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Useful Built-in Functions

```python
len(iterable)              # Length
min(iterable)              # Minimum value
max(iterable)              # Maximum value
sum(iterable)              # Sum of all elements
sorted(iterable)           # Return sorted list
reversed(iterable)         # Reverse iterator
enumerate(iterable)        # Get (index, value) pairs
zip(iter1, iter2)          # Combine iterables
any(iterable)              # True if any element is True
all(iterable)              # True if all elements are True
range(start, stop, step)   # Generate sequence
map(func, iterable)        # Apply function to all
filter(func, iterable)     # Filter elements
```

---

## String Methods

```python
s = "  Hello World  "

s.lower()                  # "  hello world  "
s.upper()                  # "  HELLO WORLD  "
s.strip()                  # "Hello World"
s.split()                  # ["Hello", "World"]
s.replace("World", "Python")  # "  Hello Python  "
s.startswith("  Hello")    # True
s.endswith("World  ")      # True
s.find("World")            # Index of substring (or -1)
s.count("l")               # Count occurrences
"_".join(["a", "b"])       # "a_b"
s.isdigit()                # Check if all digits
s.isalpha()                # Check if all letters
s.isalnum()                # Check if alphanumeric
```

---

## Loop Patterns

### For Loop
```python
# Iterate over list
for item in my_list:
    print(item)

# Iterate with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# Iterate over range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    response = input("Continue? (y/n): ")
    if response == "n":
        break
```

### Loop Control
```python
for i in range(10):
    if i == 3:
        continue  # Skip to next iteration
    if i == 7:
        break     # Exit loop
    print(i)
```

---

This cheat sheet covers the most common Python patterns you'll use. Keep it handy for quick reference!
