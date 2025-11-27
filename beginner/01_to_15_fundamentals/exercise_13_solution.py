# Exercise 13: Multiplication Table Generator - SOLUTION
# Difficulty: Beginner
# Concepts: Nested loops, Arithmetic operations, String formatting

# SOLUTION
def multiplication_table(number):
    """Generate multiplication table for a given number."""
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i:2} = {result}")

# Test single number table
multiplication_table(5)

print("\n" + "="*40 + "\n")

def full_multiplication_table(size=10):
    """Generate a full multiplication table."""
    # Print header row
    print("    ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()  # New line

    # Print separator
    print("    " + "-" * (size * 4))

    # Print each row
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i*j:4}", end="")
        print()  # New line after each row

# Generate full table
full_multiplication_table(10)

"""
EXPLANATION:
1. For single number: loop through 1-10 and multiply by the number
2. For full table: use nested loops (outer loop for rows, inner for columns)
3. String formatting:
   - {i:2} means print i with minimum width of 2 characters
   - {i:4} means minimum width of 4 characters (for alignment)
   - end="" prevents print from adding a newline
4. We build the table row by row, printing each cell

Key Concepts:
- Nested loops: a loop inside another loop
- Outer loop runs once, inner loop runs completely each time
- String formatting {:N} creates fixed-width columns for alignment
- end="" in print() changes what's printed at the end (default is newline)
- Building formatted tables requires careful spacing
"""

# Extension solution: Customizable range
print("\n" + "="*40)
print("--- EXTENSION SOLUTION ---\n")

def custom_multiplication_table(start, end):
    """Generate multiplication table for custom range."""
    size = end - start + 1

    # Print header row
    print("     ", end="")
    for i in range(start, end + 1):
        print(f"{i:5}", end="")
    print()

    # Print separator
    print("     " + "-" * (size * 5))

    # Print each row
    for i in range(start, end + 1):
        print(f"{i:3} |", end="")
        for j in range(start, end + 1):
            print(f"{i*j:5}", end="")
        print()

# Example: 5x5 table from 5-9
print("Multiplication table (5-9 x 5-9):")
custom_multiplication_table(5, 9)

print("\nMultiplication table (11-15 x 11-15):")
custom_multiplication_table(11, 15)
