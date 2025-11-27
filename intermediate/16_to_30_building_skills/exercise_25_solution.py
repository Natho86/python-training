# Exercise 25: CSV File Handling - SOLUTION
# Difficulty: Intermediate-
# Concepts: CSV module, Reading/writing CSV, Data processing

# SOLUTION
import csv
import os

print("CSV FILE HANDLING DEMONSTRATION")
print("=" * 60)

# Ensure temp directory exists
if not os.path.exists('temp_files'):
    os.makedirs('temp_files')

# 1. WRITING CSV FILES
print("1. WRITING TO CSV FILE")
print("-" * 60)

# Data to write
students = [
    ['Name', 'Age', 'Grade', 'City'],  # Header
    ['Alice', 20, 'A', 'New York'],
    ['Bob', 22, 'B', 'Los Angeles'],
    ['Charlie', 21, 'A', 'Chicago'],
    ['Diana', 23, 'B', 'Boston'],
    ['Eve', 20, 'A', 'Seattle']
]

# Write to CSV
filename = 'temp_files/students.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)  # Write all rows at once

print(f"Created CSV file: {filename}")
print()

# 2. READING CSV FILES
print("2. READING CSV FILE")
print("-" * 60)

with open(filename, 'r', newline='') as file:
    reader = csv.reader(file)
    print("CSV Contents:")
    for row in reader:
        print(row)
print()

# 3. READING CSV AS DICTIONARIES
print("3. READING AS DICTIONARIES")
print("-" * 60)

with open(filename, 'r', newline='') as file:
    reader = csv.DictReader(file)
    print("Students as dictionaries:")
    for row in reader:
        print(row)
print()

# 4. FILTERING CSV DATA
print("4. FILTERING CSV DATA")
print("-" * 60)

def find_students_by_grade(filename, grade):
    """Find all students with a specific grade."""
    results = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Grade'] == grade:
                results.append(row)
    return results

# Find all A students
a_students = find_students_by_grade(filename, 'A')
print("Students with grade A:")
for student in a_students:
    print(f"  {student['Name']} from {student['City']}")
print()

# 5. APPENDING TO CSV
print("5. APPENDING NEW RECORDS")
print("-" * 60)

new_students = [
    ['Frank', 24, 'C', 'Miami'],
    ['Grace', 19, 'A', 'Denver']
]

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_students)

print("Added new students:")
for student in new_students:
    print(f"  {student[0]}")
print()

# Display updated file
print("Updated file contents:")
with open(filename, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
EXPLANATION:
1. csv module provides reader and writer for CSV files
2. csv.writer() creates a writer object for writing data
3. csv.reader() reads CSV and returns each row as a list
4. csv.DictReader() reads CSV and returns rows as dictionaries
5. Always use newline='' when opening CSV files
6. .writerow() writes one row, .writerows() writes multiple rows
7. DictReader uses first row as header/keys automatically

Key Concepts:
- CSV is a common format for tabular data
- csv module handles special cases (commas in data, quotes)
- DictReader makes data access more intuitive
- CSV files are human-readable text files
"""

# Alternative: Writing with DictWriter
print("\n--- USING DICTWRITER ---")

products = [
    {'Product': 'Laptop', 'Price': 999.99, 'Stock': 15},
    {'Product': 'Mouse', 'Price': 25.50, 'Stock': 50},
    {'Product': 'Keyboard', 'Price': 75.00, 'Stock': 30}
]

products_file = 'temp_files/products.csv'
with open(products_file, 'w', newline='') as file:
    fieldnames = ['Product', 'Price', 'Stock']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write header row
    writer.writerows(products)  # Write all data rows

print(f"Created products CSV with DictWriter")

# Read and display
with open(products_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    print("\nProducts:")
    for row in reader:
        print(f"  {row['Product']}: ${row['Price']} ({row['Stock']} in stock)")

# Extension solution: Student Database Manager
print("\n--- EXTENSION SOLUTION: DATABASE MANAGER ---")

class StudentDatabase:
    """Manage student records in CSV format."""

    def __init__(self, filename='temp_files/student_db.csv'):
        self.filename = filename
        self.fieldnames = ['ID', 'Name', 'Age', 'Grade', 'Email']
        self._initialize_file()

    def _initialize_file(self):
        """Create file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def add_student(self, student_id, name, age, grade, email):
        """Add a new student to the database."""
        # Validate data
        if not self._validate_student(student_id, name, age, grade, email):
            return False

        student = {
            'ID': student_id,
            'Name': name,
            'Age': age,
            'Grade': grade,
            'Email': email
        }

        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(student)

        print(f"Added student: {name}")
        return True

    def _validate_student(self, student_id, name, age, grade, email):
        """Validate student data."""
        if not student_id or not name:
            print("Error: ID and Name are required")
            return False
        if not isinstance(age, int) or age < 0:
            print("Error: Age must be a positive integer")
            return False
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            print("Error: Grade must be A, B, C, D, or F")
            return False
        if '@' not in email:
            print("Error: Invalid email format")
            return False
        return True

    def get_all_students(self):
        """Retrieve all students."""
        students = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students

    def find_student(self, student_id):
        """Find a student by ID."""
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == str(student_id):
                    return row
        return None

    def update_student(self, student_id, **kwargs):
        """Update student information."""
        students = self.get_all_students()
        updated = False

        for student in students:
            if student['ID'] == str(student_id):
                for key, value in kwargs.items():
                    if key in student:
                        student[key] = value
                updated = True
                break

        if updated:
            self._write_all_students(students)
            print(f"Updated student ID: {student_id}")
        else:
            print(f"Student ID {student_id} not found")

        return updated

    def delete_student(self, student_id):
        """Delete a student by ID."""
        students = self.get_all_students()
        original_count = len(students)

        students = [s for s in students if s['ID'] != str(student_id)]

        if len(students) < original_count:
            self._write_all_students(students)
            print(f"Deleted student ID: {student_id}")
            return True
        else:
            print(f"Student ID {student_id} not found")
            return False

    def _write_all_students(self, students):
        """Write all students to file (overwrites existing)."""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(students)

    def get_statistics(self):
        """Get database statistics."""
        students = self.get_all_students()

        if not students:
            return "No students in database"

        ages = [int(s['Age']) for s in students]
        grades = [s['Grade'] for s in students]

        stats = {
            'total_students': len(students),
            'average_age': sum(ages) / len(ages),
            'grade_distribution': {}
        }

        for grade in grades:
            stats['grade_distribution'][grade] = stats['grade_distribution'].get(grade, 0) + 1

        return stats

    def display_all(self):
        """Display all students in a formatted table."""
        students = self.get_all_students()

        if not students:
            print("No students in database")
            return

        # Print header
        print(f"\n{'ID':<10} {'Name':<20} {'Age':<5} {'Grade':<7} {'Email':<30}")
        print("-" * 75)

        # Print students
        for student in students:
            print(f"{student['ID']:<10} {student['Name']:<20} {student['Age']:<5} "
                  f"{student['Grade']:<7} {student['Email']:<30}")

# Test the database manager
db = StudentDatabase()

# Add students
db.add_student('001', 'Alice Johnson', 20, 'A', 'alice@email.com')
db.add_student('002', 'Bob Smith', 22, 'B', 'bob@email.com')
db.add_student('003', 'Charlie Brown', 21, 'A', 'charlie@email.com')

# Display all students
db.display_all()

# Find a student
print("\nFinding student 002:")
student = db.find_student('002')
if student:
    print(f"  Found: {student['Name']}, Grade: {student['Grade']}")

# Update a student
print("\nUpdating student 002:")
db.update_student('002', Grade='A', Age=23)

# Get statistics
print("\nDatabase Statistics:")
stats = db.get_statistics()
print(f"  Total Students: {stats['total_students']}")
print(f"  Average Age: {stats['average_age']:.1f}")
print(f"  Grade Distribution: {stats['grade_distribution']}")

# Delete a student
print("\nDeleting student 003:")
db.delete_student('003')

# Display final state
db.display_all()

# Advanced: CSV with different delimiters
print("\n--- DIFFERENT DELIMITERS ---")

# Tab-separated values (TSV)
tsv_file = 'temp_files/data.tsv'
with open(tsv_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['Name', 'Score', 'Time'])
    writer.writerow(['Alice', 95, '10:30'])
    writer.writerow(['Bob', 87, '11:45'])

print(f"Created TSV file: {tsv_file}")

# Read TSV
with open(tsv_file, 'r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    print("TSV Contents:")
    for row in reader:
        print(f"  {row}")

print("\n" + "=" * 60)
print("CSV files created in 'temp_files/' directory")
print("=" * 60)
