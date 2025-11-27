# Exercise 33: Lambda Functions and Sorting - SOLUTION
# Difficulty: Intermediate-
# Concepts: Lambda functions, Sorting, Anonymous functions

# SOLUTION
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Charlie', 'age': 21, 'grade': 78},
    {'name': 'Diana', 'age': 19, 'grade': 95}
]

# Sort by name (alphabetically)
sorted_by_name = sorted(students, key=lambda x: x['name'])
print("Sorted by name:")
for student in sorted_by_name:
    print(f"  {student}")

# Sort by grade (highest to lowest)
sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("\nSorted by grade (highest first):")
for student in sorted_by_grade:
    print(f"  {student}")

# Sort by age (youngest to oldest)
sorted_by_age = sorted(students, key=lambda x: x['age'])
print("\nSorted by age (youngest first):")
for student in sorted_by_age:
    print(f"  {student}")

"""
EXPLANATION:
1. Lambda functions are anonymous (unnamed) functions defined inline
2. Syntax: lambda parameters: expression
3. sorted() returns a new sorted list (original unchanged)
4. The key parameter tells sorted() what to sort by
5. lambda x: x['name'] means "for each student x, use x['name'] as the sort key"
6. reverse=True sorts in descending order (highest first)

Key Concepts:
- Lambda functions are one-line functions without a name
- Perfect for simple operations like extracting a value
- sorted(list, key=function) sorts using the result of function
- Lambda is more concise than defining a full function
- Original list is not modified by sorted()
"""

# Alternative solution using regular functions
print("\n--- ALTERNATIVE SOLUTION (using regular functions) ---")

def get_grade(student):
    """Extract grade from student dictionary."""
    return student['grade']

sorted_by_grade_alt = sorted(students, key=get_grade, reverse=True)
print("Sorted by grade using regular function:")
for student in sorted_by_grade_alt:
    print(f"  {student['name']}: {student['grade']}")

# Extension solution: Multi-criteria sorting
print("\n--- EXTENSION SOLUTION ---")

def sort_by_grade_then_name(students_list):
    """
    Sort students by grade (descending), then by name (ascending).

    For students with the same grade, sort alphabetically by name.
    """
    # Return tuple: negative grade (for descending), then name (for ascending)
    return sorted(students_list, key=lambda x: (-x['grade'], x['name']))

# Add more students to demonstrate
extended_students = students + [
    {'name': 'Eve', 'age': 20, 'grade': 92},  # Same grade as Bob
    {'name': 'Frank', 'age': 21, 'grade': 78}  # Same grade as Charlie
]

sorted_multi = sort_by_grade_then_name(extended_students)
print("\nSorted by grade (desc), then name (asc):")
for student in sorted_multi:
    print(f"  {student['name']}: {student['grade']}")

# More lambda examples
print("\n--- MORE LAMBDA EXAMPLES ---")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Lambda add: {add(5, 3)}")

# Lambda with conditional
is_adult = lambda age: "Adult" if age >= 18 else "Minor"
print(f"Age 20: {is_adult(20)}")
print(f"Age 15: {is_adult(15)}")

# Lambda for filtering (returns boolean)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda for mapping (transforms each element)
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")
