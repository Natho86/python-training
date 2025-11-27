# Exercise 38: Class with __str__ and __repr__
# Difficulty: Intermediate-
# Concepts: Special methods, __str__, __repr__, String representation

"""
PROBLEM:
Create a Product class for an e-commerce system with:
- Attributes: name, price, quantity
- __str__ method: returns user-friendly string (e.g., "Laptop - $999.99 (5 in stock)")
- __repr__ method: returns developer-friendly string (e.g., "Product('Laptop', 999.99, 5)")
- Methods:
  - sell(quantity): reduces stock if available
  - restock(quantity): adds to stock

EXAMPLE:
product = Product("Laptop", 999.99, 5)
print(product)  # Uses __str__: "Laptop - $999.99 (5 in stock)"
print(repr(product))  # Uses __repr__: "Product('Laptop', 999.99, 5)"

product.sell(2)
print(product)  # "Laptop - $999.99 (3 in stock)"

HINTS:
1. __str__ is for end users (readable)
2. __repr__ is for developers (should be unambiguous and ideally recreate object)
3. If __str__ is not defined, Python falls back to __repr__

EXTENSION:
Add a total_value() method that returns the total inventory value (price * quantity),
and implement __eq__ to compare products by name.
"""

# Write your solution here
