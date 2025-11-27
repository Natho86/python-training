# Exercise 7: List Sum and Average - SOLUTION
# Difficulty: Beginner
# Concepts: Lists, For loops, Arithmetic operations, Functions

# SOLUTION
def calculate_sum_and_average(numbers):
    """Calculate sum and average of a list of numbers."""
    if not numbers:
        return 0, 0

    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)

    return total, average

# Test with example
test_list = [10, 20, 30, 40, 50]
sum_result, avg_result = calculate_sum_and_average(test_list)

print(f"List: {test_list}")
print(f"Sum: {sum_result}")
print(f"Average: {avg_result}")

"""
EXPLANATION:
1. We initialize total to 0
2. We loop through each number and add it to total using +=
3. len(numbers) gives us the count of elements in the list
4. Average is calculated by dividing the sum by the count
5. We return both values as a tuple (can return multiple values)

Key Concepts:
- Accumulator pattern: starting with 0 and adding to it in a loop
- len() function returns the number of elements in a list
- Functions can return multiple values separated by commas
- Multiple return values can be unpacked into separate variables
"""

# Alternative using built-in sum()
print("\n--- USING BUILT-IN sum() ---")
test_list2 = [5, 15, 25, 35]
total = sum(test_list2)
average = total / len(test_list2)
print(f"List: {test_list2}")
print(f"Sum: {total}")
print(f"Average: {average}")

# Extension solution: Median and Mode
print("\n--- EXTENSION SOLUTION ---")

def calculate_statistics(numbers):
    """Calculate sum, average, median, and mode."""
    if not numbers:
        return None, None, None, None

    # Sum and Average
    total = sum(numbers)
    average = total / len(numbers)

    # Median (middle value when sorted)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:  # Even number of elements
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:  # Odd number of elements
        median = sorted_nums[n//2]

    # Mode (most frequent value)
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    mode = max(frequency, key=frequency.get)

    return total, average, median, mode

# Test extended version
test_list = [10, 20, 30, 20, 40, 50, 20, 30]
total, avg, median, mode = calculate_statistics(test_list)

print(f"List: {test_list}")
print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Median: {median}")
print(f"Mode: {mode}")
