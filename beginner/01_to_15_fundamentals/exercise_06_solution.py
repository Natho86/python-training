# Exercise 6: List Maximum Finder - SOLUTION
# Difficulty: Beginner
# Concepts: Lists, For loops, Variables, Comparison operators

# SOLUTION
def find_maximum(numbers):
    """Find the maximum value in a list."""
    if not numbers:  # Check if list is empty
        return None

    max_value = numbers[0]  # Start with first element

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

# Test with examples
test_list1 = [3, 7, 2, 9, 1, 5]
test_list2 = [-5, -2, -10, -1]

print(f"List: {test_list1}")
print(f"The maximum value is: {find_maximum(test_list1)}")

print(f"\nList: {test_list2}")
print(f"The maximum value is: {find_maximum(test_list2)}")

"""
EXPLANATION:
1. We first check if the list is empty to avoid errors
2. We initialize max_value with the first element of the list (numbers[0])
3. We loop through each number in the list
4. If we find a number greater than max_value, we update max_value
5. After checking all numbers, max_value contains the largest number

Key Concepts:
- Lists can be indexed with [0], [1], etc. (starting from 0)
- for num in numbers iterates through each element
- We must handle edge cases like empty lists
- Starting with the first element ensures our comparison works with negative numbers
"""

# Extension solution: Find min, max, and their positions
print("\n--- EXTENSION SOLUTION ---")

def find_max_min_with_positions(numbers):
    """Find max, min values and their positions."""
    if not numbers:
        return None, None, None, None

    max_value = numbers[0]
    min_value = numbers[0]
    max_index = 0
    min_index = 0

    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

    return max_value, max_index, min_value, min_index

# Test the extended version
test_list = [3, 7, 2, 9, 1, 5, 9, 0]
max_val, max_idx, min_val, min_idx = find_max_min_with_positions(test_list)

print(f"List: {test_list}")
print(f"Maximum: {max_val} at index {max_idx}")
print(f"Minimum: {min_val} at index {min_idx}")
