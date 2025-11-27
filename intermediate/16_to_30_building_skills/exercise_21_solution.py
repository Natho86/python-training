# Exercise 21: String Formatting Master - SOLUTION
# Difficulty: Beginner+
# Concepts: String formatting, f-strings, .format() method

# SOLUTION
print("STRING FORMATTING TECHNIQUES")
print("=" * 60)

# 1. Basic f-string formatting
name = "Alice"
age = 25
balance = 1234.567

print("1. BASIC F-STRING FORMATTING")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Balance: ${balance:.2f}")  # 2 decimal places
print()

# 2. Number formatting
print("2. NUMBER FORMATTING")
large_number = 1234567.89
print(f"Default: {large_number}")
print(f"2 decimals: {large_number:.2f}")
print(f"With comma separator: {large_number:,.2f}")
print(f"In scientific notation: {large_number:.2e}")
print()

# 3. Text alignment
print("3. TEXT ALIGNMENT")
print(f"{'Left':<20}|")     # Left aligned, 20 characters
print(f"{'Center':^20}|")   # Center aligned
print(f"{'Right':>20}|")    # Right aligned
print()

# 4. Creating formatted tables
print("4. FORMATTED TABLE")
users = [
    ("Alice", 25, 1234.57),
    ("Bob", 30, 5678.90),
    ("Charlie", 28, 9012.34)
]

# Table header
print(f"{'Name':<15} {'Age':>5} {'Balance':>12}")
print("-" * 35)

# Table rows
for user_name, user_age, user_balance in users:
    print(f"{user_name:<15} {user_age:>5} ${user_balance:>10,.2f}")

"""
EXPLANATION:
1. f-strings (f"...{var}...") are the modern way to format strings
2. Format specifiers come after a colon in braces: {value:format}
3. Common format specifiers:
   - .2f: floating point with 2 decimals
   - ,: thousands separator
   - <N: left align in N characters
   - >N: right align in N characters
   - ^N: center align in N characters
4. f-strings are evaluated at runtime and very efficient

Key Concepts:
- f-strings are clearer and faster than .format() or % formatting
- Format specifiers control appearance without changing the value
- Alignment helps create readable tables and reports
- Combining specifiers: {value:>10,.2f} means right-align, 10 chars, comma separator, 2 decimals
"""

# Alternative using .format() method
print("\n--- ALTERNATIVE USING .format() ---")

template = "Name: {}, Age: {}, Balance: ${:.2f}"
print(template.format(name, age, balance))

# Named placeholders
template2 = "Name: {n}, Age: {a}, Balance: ${b:.2f}"
print(template2.format(n=name, a=age, b=balance))

# Old-style % formatting (legacy)
print("\n--- LEGACY % FORMATTING ---")
print("Name: %s, Age: %d, Balance: $%.2f" % (name, age, balance))

# Advanced formatting examples
print("\n--- ADVANCED FORMATTING ---")

# Percentage formatting
score = 0.875
print(f"Score: {score:.1%}")  # Displays as percentage

# Padding with zeros
number = 42
print(f"Order number: {number:05d}")  # Pad with zeros to 5 digits

# Binary, octal, hexadecimal
value = 255
print(f"Decimal: {value}")
print(f"Binary: {value:b}")
print(f"Octal: {value:o}")
print(f"Hex: {value:x}")
print(f"Hex (uppercase): {value:X}")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"\nCurrent date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H:%M:%S}")
print(f"Full: {now:%Y-%m-%d %H:%M:%S}")

# Extension solution: Receipt generator
print("\n--- EXTENSION SOLUTION: RECEIPT GENERATOR ---")

def generate_receipt(items, store_name="Python Store", tax_rate=0.08):
    """
    Generate a formatted receipt.

    Args:
        items: List of tuples (item_name, quantity, price)
        store_name: Name of the store
        tax_rate: Tax rate as decimal (0.08 = 8%)
    """
    width = 50
    receipt = []

    # Header
    receipt.append("=" * width)
    receipt.append(f"{store_name:^{width}}")
    receipt.append("=" * width)
    receipt.append(f"{'Date:':<10} {datetime.now():%Y-%m-%d %H:%M:%S}")
    receipt.append("-" * width)
    receipt.append("")

    # Column headers
    receipt.append(f"{'Item':<25} {'Qty':>5} {'Price':>8} {'Total':>10}")
    receipt.append("-" * width)

    # Items
    subtotal = 0
    for item_name, quantity, price in items:
        total = quantity * price
        subtotal += total
        receipt.append(f"{item_name:<25} {quantity:>5} ${price:>7.2f} ${total:>9.2f}")

    # Calculations
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt.append("-" * width)
    receipt.append(f"{'Subtotal:':<40} ${subtotal:>8,.2f}")
    receipt.append(f"{'Tax (' + f'{tax_rate:.1%}' + '):':<40} ${tax:>8,.2f}")
    receipt.append("=" * width)
    receipt.append(f"{'TOTAL:':<40} ${total:>8,.2f}")
    receipt.append("=" * width)
    receipt.append("")
    receipt.append(f"{'Thank you for your purchase!':^{width}}")
    receipt.append("=" * width)

    return "\n".join(receipt)

# Test the receipt generator
shopping_items = [
    ("Python Programming Book", 2, 49.99),
    ("Wireless Mouse", 1, 25.50),
    ("USB Cable", 3, 8.99),
    ("Laptop Stand", 1, 45.00),
    ("Notebook Set", 2, 12.75)
]

receipt = generate_receipt(shopping_items, "Tech Haven", 0.0825)
print(receipt)

# Dynamic width formatting
print("\n--- DYNAMIC WIDTH FORMATTING ---")

def format_table(data, headers):
    """Create a dynamically sized table."""
    # Calculate column widths
    col_widths = [len(h) for h in headers]

    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Create format strings
    header_format = " | ".join(f"{{:<{w}}}" for w in col_widths)
    separator = "-+-".join("-" * w for w in col_widths)

    # Print table
    print(header_format.format(*headers))
    print(separator)
    for row in data:
        print(header_format.format(*[str(cell) for cell in row]))

# Test dynamic table
table_data = [
    ["Alice", "Engineer", "$95,000"],
    ["Bob", "Designer", "$75,000"],
    ["Charlie", "Manager", "$110,000"]
]
table_headers = ["Name", "Position", "Salary"]

print("\nDynamic Table:")
format_table(table_data, table_headers)

# Multiline f-strings
print("\n--- MULTILINE F-STRINGS ---")

product_name = "Laptop"
product_price = 999.99
product_stock = 15

info = f"""
Product Information
-------------------
Name:     {product_name}
Price:    ${product_price:,.2f}
In Stock: {product_stock} units
Status:   {'Available' if product_stock > 0 else 'Out of Stock'}
"""

print(info)

# Expression evaluation in f-strings
print("--- EXPRESSIONS IN F-STRINGS ---")
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")
print(f"Is {x} greater than {y}? {x > y}")
print(f"Doubled: {x * 2}")

# Calling functions in f-strings
def discount(price, percent):
    return price * (1 - percent / 100)

original = 100
discount_percent = 20
print(f"\nOriginal: ${original:.2f}")
print(f"After {discount_percent}% discount: ${discount(original, discount_percent):.2f}")
