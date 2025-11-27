# Exercise 34: Map, Filter, and Reduce - SOLUTION
# Difficulty: Intermediate-
# Concepts: Map, Filter, Reduce, Functional programming

from functools import reduce

# SOLUTION
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Map - square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original numbers: {numbers}")
print(f"After map (squared): {squared}")

# Step 2: Filter - keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, squared))
print(f"After filter (evens only): {evens}")

# Step 3: Reduce - calculate product
product = reduce(lambda x, y: x * y, evens)
print(f"After reduce (product): {product:,}")

# All in one chained operation
print("\n--- CHAINED OPERATION ---")
result = reduce(
    lambda x, y: x * y,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x ** 2, numbers)
    )
)
print(f"Chained result: {result:,}")

"""
EXPLANATION:
1. map(function, iterable) applies function to each element and returns a map object
2. Convert map object to list with list() to see the results
3. filter(function, iterable) keeps elements where function returns True
4. reduce(function, iterable) applies function cumulatively to reduce to single value
5. reduce takes two arguments at a time: reduce(lambda x, y: x * y, [1,2,3,4])
   - First: 1 * 2 = 2
   - Then: 2 * 3 = 6
   - Then: 6 * 4 = 24

Key Concepts:
- map() transforms each element
- filter() selects elements based on a condition
- reduce() combines all elements into a single value
- These can be chained together for data processing pipelines
- Lambda functions work perfectly with these functions
"""

# More examples
print("\n--- MORE EXAMPLES ---")

# Map: Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Filter: Get names longer than 4 characters
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(f"\nNames: {names}")
print(f"Names longer than 4 chars: {long_names}")

# Reduce: Find maximum value
numbers = [45, 23, 67, 12, 89, 34]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"\nNumbers: {numbers}")
print(f"Maximum: {maximum}")

# Reduce: Concatenate strings
words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"\nWords: {words}")
print(f"Sentence: {sentence}")

# Extension solution: Price processing pipeline
print("\n--- EXTENSION SOLUTION ---")

def process_prices(price_strings):
    """
    Process a list of price strings.

    Steps:
    1. Convert strings like "$12.99" to floats
    2. Filter out prices above $50
    3. Calculate total
    """
    # Map: Convert strings to floats
    prices = map(lambda s: float(s.replace('$', '')), price_strings)

    # Filter: Keep prices $50 or less
    affordable = filter(lambda p: p <= 50, prices)

    # Reduce: Calculate total
    total = reduce(lambda x, y: x + y, affordable, 0)  # 0 is initial value

    return total

price_list = ["$12.99", "$45.50", "$67.00", "$23.75", "$89.99", "$15.00", "$32.50"]
total = process_prices(price_list)
print(f"Price list: {price_list}")
print(f"Total of prices $50 or less: ${total:.2f}")

# Show the breakdown
print("\nBreakdown:")
prices_float = [float(p.replace('$', '')) for p in price_list]
affordable_prices = [p for p in prices_float if p <= 50]
print(f"Affordable prices: ${', $'.join(f'{p:.2f}' for p in affordable_prices)}")

# Alternative using list comprehensions (often more Pythonic)
print("\n--- ALTERNATIVE: List Comprehensions ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map alternative
squared_lc = [x ** 2 for x in numbers]
print(f"Squared (list comprehension): {squared_lc}")

# Filter alternative
evens_lc = [x for x in squared_lc if x % 2 == 0]
print(f"Evens (list comprehension): {evens_lc}")

# Reduce still needed for product
product_lc = reduce(lambda x, y: x * y, evens_lc)
print(f"Product: {product_lc:,}")
