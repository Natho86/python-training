# Exercise 11: Grade Calculator - SOLUTION
# Difficulty: Beginner
# Concepts: Lists, Functions, Arithmetic operations, Control flow

# SOLUTION
def get_letter_grade(average):
    """Convert numeric average to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_grades(scores):
    """Calculate average, letter grade, and min/max scores."""
    if not scores:
        return None, None, None, None

    average = sum(scores) / len(scores)
    letter_grade = get_letter_grade(average)
    highest = max(scores)
    lowest = min(scores)

    return average, letter_grade, highest, lowest

# Test with example
test_scores = [85, 92, 78, 90, 88]

average, letter, highest, lowest = calculate_grades(test_scores)

print(f"Scores: {test_scores}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")

"""
EXPLANATION:
1. We create a separate function to convert numeric grade to letter grade
2. We use if/elif/else with comparison operators to determine the grade tier
3. sum(scores) adds all numbers in the list
4. len(scores) gives us the count of scores
5. max() and min() find the highest and lowest values
6. We return multiple values as a tuple

Key Concepts:
- Breaking code into smaller functions makes it more organized
- sum(), max(), and min() are built-in functions that work on lists
- if/elif/else checks conditions in order (first match wins)
- The >= operator means "greater than or equal to"
- Formatting with :.1f shows one decimal place
"""

# Test with multiple students
print("\n--- MULTIPLE STUDENTS ---")

students = {
    "Alice": [95, 88, 92, 90],
    "Bob": [78, 82, 75, 80],
    "Charlie": [65, 70, 68, 72],
    "Diana": [58, 62, 55, 60]
}

for name, scores in students.items():
    avg, grade, high, low = calculate_grades(scores)
    print(f"\n{name}:")
    print(f"  Average: {avg:.1f} ({grade})")
    print(f"  Range: {low}-{high}")

# Extension solution: Weighted grades and GPA
print("\n--- EXTENSION SOLUTION ---")

def calculate_weighted_grade(tests, homework, final_exam):
    """Calculate weighted grade (tests 40%, homework 30%, final 30%)."""
    test_avg = sum(tests) / len(tests) if tests else 0
    hw_avg = sum(homework) / len(homework) if homework else 0

    weighted_avg = (test_avg * 0.4) + (hw_avg * 0.3) + (final_exam * 0.3)
    return weighted_avg

def grade_to_gpa(letter_grade):
    """Convert letter grade to GPA (4.0 scale)."""
    gpa_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return gpa_map.get(letter_grade, 0.0)

# Test weighted grades
student_tests = [85, 90, 88]
student_homework = [95, 92, 90, 88]
student_final = 92

weighted_avg = calculate_weighted_grade(student_tests, student_homework, student_final)
letter = get_letter_grade(weighted_avg)
gpa = grade_to_gpa(letter)

print("\nWeighted Grade Calculation:")
print(f"Tests (40%): {sum(student_tests)/len(student_tests):.1f}")
print(f"Homework (30%): {sum(student_homework)/len(student_homework):.1f}")
print(f"Final Exam (30%): {student_final}")
print(f"Weighted Average: {weighted_avg:.1f}")
print(f"Letter Grade: {letter}")
print(f"GPA: {gpa:.1f}")
