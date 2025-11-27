# Exercise 29: Data Analysis with Lists and Dictionaries
# Difficulty: Intermediate-
# Concepts: Data structures, List comprehensions, Data aggregation, Statistics

"""
PROBLEM:
Create a program that analyzes sales data using lists and dictionaries:
1. Store sales records (product, quantity, price, date)
2. Calculate total revenue
3. Find best-selling products
4. Calculate average sale amount
5. Group sales by date or product
6. Generate summary reports

EXAMPLE:
Sales Data:
[
    {'product': 'Laptop', 'quantity': 2, 'price': 999.99, 'date': '2024-01-15'},
    {'product': 'Mouse', 'quantity': 5, 'price': 25.50, 'date': '2024-01-15'},
    {'product': 'Laptop', 'quantity': 1, 'price': 999.99, 'date': '2024-01-16'},
]

Output:
Total Revenue: $3,026.48
Best Selling Product: Laptop (3 units)
Average Sale: $1,008.83
Sales by Product:
  Laptop: $2,999.97
  Mouse: $127.50

HINTS:
1. Use list of dictionaries to store sales records
2. Use list comprehensions to filter and transform data
3. Use sum() with generator expressions for totals
4. Use dictionaries to group data by categories
5. Create functions for each analysis task

EXTENSION:
Add date-based filtering (sales in a date range).
Calculate profit margins if you have cost data.
Find products that never sold (if you have inventory list).
Generate top N products by revenue or quantity.
"""

# Write your solution here
