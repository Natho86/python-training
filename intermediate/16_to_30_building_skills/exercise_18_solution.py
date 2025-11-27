# Exercise 18: Student Grade Manager - SOLUTION
# Difficulty: Beginner+
# Concepts: Dictionaries, Nested structures, Functions, Calculations

# SOLUTION
def calculate_average(grades):
    """Calculate average from a dictionary of grades."""
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def find_top_student(students):
    """Find the student with the highest average grade."""
    top_student = None
    top_average = 0

    for student, grades in students.items():
        avg = calculate_average(grades)
        if avg > top_average:
            top_average = avg
            top_student = student

    return top_student, top_average

# Test data
students = {
    'Alice': {'Math': 85, 'Science': 92, 'English': 78},
    'Bob': {'Math': 90, 'Science': 88, 'English': 95},
    'Charlie': {'Math': 78, 'Science': 85, 'English': 80}
}

print("Student Grade Report")
print("=" * 40)

# Display all averages
for student, grades in students.items():
    avg = calculate_average(grades)
    print(f"{student}'s average: {avg:.1f}")

# Find and display top student
top_name, top_avg = find_top_student(students)
print(f"\nTop student: {top_name} with average {top_avg:.1f}")

"""
EXPLANATION:
1. We use nested dictionaries: outer dict maps names to grade dicts
2. calculate_average() uses .values() to get all grades and computes mean
3. find_top_student() iterates through all students, tracking the best
4. We use .items() to iterate through both keys (names) and values (grades)
5. The :.1f format specifier displays floats with 1 decimal place

Key Concepts:
- Nested dictionaries allow hierarchical data storage
- .values() returns all values in a dictionary
- sum() works on any iterable of numbers
- Tracking max values requires maintaining state during iteration
"""

# Alternative using max() with key function
print("\n--- ALTERNATIVE SOLUTION ---")

def get_student_averages(students):
    """Return dictionary of student names and their averages."""
    return {name: calculate_average(grades) for name, grades in students.items()}

averages = get_student_averages(students)
print("\nAll averages:", averages)

# Find top student using max()
top_student_name = max(averages, key=averages.get)
print(f"Top student (using max): {top_student_name} with {averages[top_student_name]:.1f}")

# Extension solution: Full grade management system
print("\n--- EXTENSION SOLUTION ---")

class GradeManager:
    """Complete grade management system."""

    def __init__(self):
        self.students = {}

    def add_student(self, name, grades=None):
        """Add a new student or update existing."""
        if grades is None:
            grades = {}
        self.students[name] = grades
        print(f"Added/Updated: {name}")

    def update_grade(self, name, subject, grade):
        """Update a specific subject grade for a student."""
        if name in self.students:
            self.students[name][subject] = grade
            print(f"Updated {name}'s {subject} grade to {grade}")
        else:
            print(f"Student {name} not found!")

    def get_average(self, name):
        """Get average for a specific student."""
        if name in self.students:
            return calculate_average(self.students[name])
        return None

    def get_letter_grade(self, numeric_grade):
        """Convert numeric grade to letter grade."""
        if numeric_grade >= 90:
            return 'A'
        elif numeric_grade >= 80:
            return 'B'
        elif numeric_grade >= 70:
            return 'C'
        elif numeric_grade >= 60:
            return 'D'
        else:
            return 'F'

    def generate_report_card(self, name):
        """Generate detailed report card for a student."""
        if name not in self.students:
            return f"Student {name} not found!"

        grades = self.students[name]
        report = f"\n{'='*50}\n"
        report += f"REPORT CARD: {name}\n"
        report += f"{'='*50}\n"

        for subject, grade in grades.items():
            letter = self.get_letter_grade(grade)
            report += f"{subject:15} {grade:3} ({letter})\n"

        avg = self.get_average(name)
        avg_letter = self.get_letter_grade(avg)
        report += f"{'-'*50}\n"
        report += f"{'Average':15} {avg:.1f} ({avg_letter})\n"
        report += f"{'='*50}\n"

        return report

    def find_extremes(self):
        """Find highest and lowest grades across all subjects."""
        all_grades = []
        for grades in self.students.values():
            all_grades.extend(grades.values())

        if not all_grades:
            return None, None

        return max(all_grades), min(all_grades)

    def display_summary(self):
        """Display complete summary of all students."""
        print("\n" + "="*50)
        print("COMPLETE GRADE SUMMARY")
        print("="*50)

        averages = []
        for name, grades in self.students.items():
            avg = calculate_average(grades)
            averages.append((name, avg))
            print(f"{name:15} Average: {avg:.1f} ({self.get_letter_grade(avg)})")

        # Find top student
        if averages:
            top = max(averages, key=lambda x: x[1])
            print(f"\nTop Performer: {top[0]} ({top[1]:.1f})")

        # Find grade extremes
        highest, lowest = self.find_extremes()
        if highest and lowest:
            print(f"\nHighest Grade: {highest}")
            print(f"Lowest Grade: {lowest}")

# Test the complete system
manager = GradeManager()

# Add students with initial grades
manager.students = students

# Add a new student
manager.add_student('Diana', {'Math': 95, 'Science': 98, 'English': 92})

# Update a grade
manager.update_grade('Alice', 'Math', 90)

# Generate report card
print(manager.generate_report_card('Bob'))

# Display complete summary
manager.display_summary()
