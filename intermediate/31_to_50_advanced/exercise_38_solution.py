# Exercise 38: Class with __str__ and __repr__ - SOLUTION
# Difficulty: Intermediate-
# Concepts: Special methods, __str__, __repr__, String representation

# SOLUTION
class Product:
    """Represents a product in an e-commerce system."""

    def __init__(self, name, price, quantity):
        """
        Initialize product.

        Args:
            name: Product name
            price: Product price
            quantity: Quantity in stock
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        User-friendly string representation.
        Called by print() and str()
        """
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"

    def __repr__(self):
        """
        Developer-friendly string representation.
        Should ideally allow recreating the object.
        """
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def sell(self, quantity):
        """
        Sell products.

        Args:
            quantity: Number of items to sell

        Returns:
            bool: True if successful
        """
        if quantity <= 0:
            print("Quantity must be positive!")
            return False

        if quantity > self.quantity:
            print(f"Insufficient stock! Only {self.quantity} available.")
            return False

        self.quantity -= quantity
        print(f"Sold {quantity} {self.name}(s). {self.quantity} remaining.")
        return True

    def restock(self, quantity):
        """
        Restock products.

        Args:
            quantity: Number of items to add

        Returns:
            bool: True if successful
        """
        if quantity <= 0:
            print("Quantity must be positive!")
            return False

        self.quantity += quantity
        print(f"Restocked {quantity} {self.name}(s). Total: {self.quantity}")
        return True

# Test the Product class
print("=== Testing Product Class ===")
laptop = Product("Laptop", 999.99, 5)

print(f"str(): {str(laptop)}")  # Calls __str__
print(f"repr(): {repr(laptop)}")  # Calls __repr__
print(f"print(): ", end="")
print(laptop)  # Calls __str__ by default

print("\n--- Selling ---")
laptop.sell(2)
print(laptop)

print("\n--- Restocking ---")
laptop.restock(10)
print(laptop)

print("\n--- Error Cases ---")
laptop.sell(100)  # Not enough stock
laptop.sell(-5)  # Invalid quantity

"""
EXPLANATION:
1. __str__ returns a string for end users - should be readable and informative
2. __repr__ returns a string for developers - should be unambiguous
3. print(obj) calls str(obj) which calls obj.__str__()
4. repr(obj) calls obj.__repr__()
5. In the interactive shell, typing just 'obj' shows repr(obj)
6. Good __repr__ should allow you to recreate the object: eval(repr(obj)) == obj

Key Concepts:
- __str__ and __repr__ are "magic methods" (dunder methods)
- __str__ is for end-user display
- __repr__ is for debugging and development
- If only __repr__ is defined, it's used for both
- Convention: __repr__ should look like a valid Python expression
"""

# Show the difference between str and repr
print("\n--- STR vs REPR ---")
products = [
    Product("Mouse", 29.99, 50),
    Product("Keyboard", 79.99, 30),
    Product("Monitor", 299.99, 15)
]

print("Using str (print):")
for product in products:
    print(product)

print("\nUsing repr (debugging):")
for product in products:
    print(repr(product))

# Demonstrating __repr__ usage for recreating objects
print("\n--- RECREATING OBJECTS FROM REPR ---")
laptop_repr = repr(laptop)
print(f"repr string: {laptop_repr}")
# You could use eval() to recreate: new_laptop = eval(laptop_repr)
# (Note: eval() should be used carefully - only with trusted input!)

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

class EnhancedProduct:
    """Enhanced product with value calculation and comparison."""

    def __init__(self, name, price, quantity):
        """Initialize product."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """User-friendly string."""
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock, Total value: ${self.total_value():.2f})"

    def __repr__(self):
        """Developer-friendly string."""
        return f"EnhancedProduct('{self.name}', {self.price}, {self.quantity})"

    def __eq__(self, other):
        """
        Compare products by name.
        Allows using == operator.
        """
        if not isinstance(other, EnhancedProduct):
            return False
        return self.name == other.name

    def sell(self, quantity):
        """Sell products."""
        if quantity <= 0:
            print("Quantity must be positive!")
            return False

        if quantity > self.quantity:
            print(f"Insufficient stock! Only {self.quantity} available.")
            return False

        self.quantity -= quantity
        print(f"Sold {quantity} {self.name}(s). {self.quantity} remaining.")
        return True

    def restock(self, quantity):
        """Restock products."""
        if quantity <= 0:
            print("Quantity must be positive!")
            return False

        self.quantity += quantity
        print(f"Restocked {quantity} {self.name}(s). Total: {self.quantity}")
        return True

    def total_value(self):
        """Calculate total inventory value."""
        return self.price * self.quantity

# Test enhanced product
print("\nTesting Enhanced Product:")
product1 = EnhancedProduct("Laptop", 999.99, 10)
product2 = EnhancedProduct("Laptop", 1099.99, 5)  # Same name, different price
product3 = EnhancedProduct("Desktop", 1299.99, 8)

print(product1)
print(f"Total value: ${product1.total_value():.2f}")

print("\nTesting equality (__eq__):")
print(f"product1 == product2: {product1 == product2}")  # True (same name)
print(f"product1 == product3: {product1 == product3}")  # False (different name)

# More magic methods example
print("\n--- MORE MAGIC METHODS ---")

class ComparableProduct(EnhancedProduct):
    """Product with comparison operators."""

    def __lt__(self, other):
        """Less than comparison based on price."""
        return self.price < other.price

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.price <= other.price

    def __gt__(self, other):
        """Greater than comparison."""
        return self.price > other.price

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.price >= other.price

p1 = ComparableProduct("Budget Laptop", 499.99, 10)
p2 = ComparableProduct("Premium Laptop", 1499.99, 5)

print(f"{p1.name} < {p2.name}: {p1 < p2}")  # True
print(f"{p1.name} > {p2.name}: {p1 > p2}")  # False

# This allows sorting
products_list = [p2, p1]
sorted_products = sorted(products_list)
print("\nSorted by price:")
for p in sorted_products:
    print(f"  {p.name}: ${p.price:.2f}")
