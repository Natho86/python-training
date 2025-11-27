# Exercise 46: Data Analysis Tool
# Difficulty: Intermediate
# Concepts: File I/O, Data processing, Statistics, Functions, Collections

"""
PROBLEM:
Create a data analysis tool that reads a CSV file containing sales data and provides:
1. Total sales and average sale amount
2. Sales by category (grouped)
3. Top 5 best-selling products
4. Sales trends by month
5. Export summary report to a text file

Sample CSV format:
date,product,category,quantity,price
2024-01-15,Laptop,Electronics,2,999.99
2024-01-16,Book,Books,5,15.99
...

The tool should:
- Read and parse CSV data
- Calculate various statistics
- Group and aggregate data
- Generate a formatted report

EXAMPLE OUTPUT:
=== Sales Analysis Report ===
Total Sales: $50,000.00
Average Sale: $125.50
Number of Transactions: 398

Top 5 Products:
1. Laptop: $19,999.80
2. Phone: $15,999.00
...

Sales by Category:
Electronics: $30,000.00 (60%)
Books: $12,000.00 (24%)
...

HINTS:
1. Use csv module or read file and split lines manually
2. Use Counter from collections for counting
3. Use defaultdict to group data by category
4. Create helper functions for each analysis type
5. Format currency with f-strings: f"${amount:.2f}"

EXTENSION:
Add visualization by creating ASCII bar charts for sales by category.
Add filtering by date range and export to JSON format.
"""

# Write your solution here
