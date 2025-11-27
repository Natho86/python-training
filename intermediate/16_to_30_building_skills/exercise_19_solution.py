# Exercise 19: Tuple Unpacking and Swapping - SOLUTION
# Difficulty: Beginner+
# Concepts: Tuples, Tuple unpacking, Multiple assignment

# SOLUTION
print("1. TUPLE UNPACKING")
print("-" * 40)

# Basic tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Coordinates: {coordinates}")
print(f"Unpacked: x={x}, y={y}, z={z}")

print("\n2. VARIABLE SWAPPING")
print("-" * 40)

# Traditional swap (with temp variable)
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")

temp = a
a = b
b = temp
print(f"After swap (traditional): a={a}, b={b}")

# Python tuple swap (no temp needed)
a = 5
b = 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap (tuple unpacking): a={a}, b={b}")

print("\n3. RETURNING MULTIPLE VALUES")
print("-" * 40)

def get_user_info():
    """Return multiple values as a tuple."""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city  # Implicitly creates a tuple

# Unpack the returned tuple
user_name, user_age, user_city = get_user_info()
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")

# Or capture as tuple
user_info = get_user_info()
print(f"\nAs tuple: {user_info}")

print("\n4. TUPLE UNPACKING WITH ENUMERATE")
print("-" * 40)

fruits = ['apple', 'banana', 'cherry', 'date']

# Using enumerate with tuple unpacking
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# With custom start index
print("\nWith start index 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")

"""
EXPLANATION:
1. Tuple unpacking assigns values from a tuple to variables in order
2. Swapping with tuples works because right side is evaluated first
3. Functions returning multiple values actually return a single tuple
4. enumerate() yields (index, value) tuples that can be unpacked
5. Tuples are immutable, but unpacking extracts their values

Key Concepts:
- Tuples use parentheses () but unpacking doesn't require them
- Multiple return values are automatically packed into a tuple
- Unpacking must have same number of variables as tuple elements
- This makes Python code more concise and readable
"""

# Alternative demonstrations
print("\n--- ADDITIONAL EXAMPLES ---")

# Unpacking in function parameters
def calculate_distance(point1, point2):
    """Calculate distance between two 2D points."""
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

p1 = (0, 0)
p2 = (3, 4)
dist = calculate_distance(p1, p2)
print(f"\nDistance between {p1} and {p2}: {dist}")

# Unpacking with _ for ignored values
print("\n--- IGNORING VALUES ---")
data = ('Alice', 25, 'Engineer', 'New York', 'USA')
name, age, *_, country = data
print(f"Name: {name}, Age: {age}, Country: {country}")

# Extension solution: Statistics function
print("\n--- EXTENSION SOLUTION ---")

def calculate_statistics(numbers):
    """
    Calculate min, max, and average of a list.

    Returns:
        tuple: (min_value, max_value, average)
    """
    if not numbers:
        return None, None, None

    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum(numbers) / len(numbers)

    return min_val, max_val, avg_val

# Test statistics function
test_numbers = [45, 23, 78, 12, 90, 34, 67]
minimum, maximum, average = calculate_statistics(test_numbers)

print(f"\nNumbers: {test_numbers}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average:.2f}")

# Extended unpacking with *
print("\n--- EXTENDED UNPACKING ---")

scores = (85, 90, 78, 92, 88, 95, 76)

# Get first, last, and all middle values
first, *middle, last = scores
print(f"First score: {first}")
print(f"Middle scores: {middle}")
print(f"Last score: {last}")

# Get first two and rest
first, second, *rest = scores
print(f"\nFirst: {first}, Second: {second}")
print(f"Rest: {rest}")

# Practical example: parsing CSV-like data
print("\n--- PRACTICAL EXAMPLE ---")

def parse_log_entry(entry):
    """Parse a log entry and return important parts."""
    timestamp, level, *message_parts = entry.split('|')
    message = '|'.join(message_parts)
    return timestamp, level, message

log = "2024-01-15 10:30:45|ERROR|Database connection failed|Retrying in 5s"
time, level, msg = parse_log_entry(log)

print(f"Timestamp: {time}")
print(f"Level: {level}")
print(f"Message: {msg}")

# Tuple as dictionary keys (tuples are hashable)
print("\n--- TUPLES AS DICT KEYS ---")

# Store game board positions
board = {
    (0, 0): 'X',
    (0, 1): 'O',
    (1, 0): 'X',
    (1, 1): 'O',
    (2, 2): 'X'
}

print("Tic-tac-toe board positions:")
for position, mark in board.items():
    row, col = position
    print(f"Position ({row}, {col}): {mark}")
