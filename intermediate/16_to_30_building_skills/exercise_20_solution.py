# Exercise 20: Set Operations - SOLUTION
# Difficulty: Beginner+
# Concepts: Sets, Set operations, Unique elements

# SOLUTION
print("SET OPERATIONS DEMONSTRATION")
print("=" * 50)

# Test data
list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [4, 5, 6, 7, 8, 5, 6]

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print()

# 1. Remove duplicates
set1 = set(list1)
set2 = set(list2)

print("1. REMOVE DUPLICATES")
print(f"Set 1 (unique elements): {set1}")
print(f"Set 2 (unique elements): {set2}")
print()

# 2. Find common elements (intersection)
common = set1 & set2  # or set1.intersection(set2)
print("2. COMMON ELEMENTS (Intersection)")
print(f"Elements in both: {common}")
print()

# 3. Find unique to each set (difference)
only_in_set1 = set1 - set2  # or set1.difference(set2)
only_in_set2 = set2 - set1  # or set2.difference(set1)
print("3. UNIQUE ELEMENTS (Difference)")
print(f"Only in list1: {only_in_set1}")
print(f"Only in list2: {only_in_set2}")
print()

# 4. Combine without duplicates (union)
all_elements = set1 | set2  # or set1.union(set2)
print("4. ALL UNIQUE ELEMENTS (Union)")
print(f"Combined unique: {all_elements}")
print()

# 5. Symmetric difference (in either but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print("5. SYMMETRIC DIFFERENCE")
print(f"In either but not both: {sym_diff}")

"""
EXPLANATION:
1. set() creates a set, automatically removing duplicates
2. Sets support mathematical operations:
   - & or .intersection(): elements in both sets
   - | or .union(): elements in either set
   - - or .difference(): elements in first but not second
   - ^ or .symmetric_difference(): elements in either but not both
3. Sets are unordered and only contain unique elements
4. Sets are faster for membership testing than lists

Key Concepts:
- Sets use curly braces {} or set() constructor
- Sets are mutable but can only contain immutable elements
- Set operations are very efficient (O(1) for membership tests)
- Useful for removing duplicates and finding relationships between collections
"""

# Alternative using methods instead of operators
print("\n--- ALTERNATIVE USING METHODS ---")

intersection = set1.intersection(set2)
union = set1.union(set2)
diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
sym_diff_method = set1.symmetric_difference(set2)

print(f"Intersection: {intersection}")
print(f"Union: {union}")
print(f"Set1 - Set2: {diff1}")
print(f"Set2 - Set1: {diff2}")
print(f"Symmetric Difference: {sym_diff_method}")

# Extension solution: Student course enrollment
print("\n--- EXTENSION SOLUTION ---")

# Student enrollment data
python_students = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
java_students = {'Bob', 'Charlie', 'Frank', 'Grace'}
web_students = {'Alice', 'Charlie', 'Eve', 'Henry', 'Grace'}

print("Course Enrollments:")
print(f"Python: {python_students}")
print(f"Java: {java_students}")
print(f"Web Dev: {web_students}")
print()

# Students in multiple courses
python_and_java = python_students & java_students
print(f"Taking both Python and Java: {python_and_java}")

python_and_web = python_students & web_students
print(f"Taking both Python and Web: {python_and_web}")

all_three = python_students & java_students & web_students
print(f"Taking all three courses: {all_three}")

# Students taking at least one course
all_students = python_students | java_students | web_students
print(f"\nTotal unique students: {len(all_students)}")
print(f"Students: {all_students}")

# Students taking only one course
only_python = python_students - java_students - web_students
only_java = java_students - python_students - web_students
only_web = web_students - python_students - java_students

print(f"\nOnly Python: {only_python}")
print(f"Only Java: {only_java}")
print(f"Only Web: {only_web}")

# Subset and superset operations
print("\n--- SUBSET/SUPERSET OPERATIONS ---")

def analyze_set_relationship(set_a, set_b, name_a="Set A", name_b="Set B"):
    """Analyze the relationship between two sets."""
    print(f"\nAnalyzing: {name_a} vs {name_b}")
    print(f"{name_a}: {set_a}")
    print(f"{name_b}: {set_b}")

    if set_a == set_b:
        print("The sets are equal")
    elif set_a < set_b:  # proper subset
        print(f"{name_a} is a proper subset of {name_b}")
    elif set_a > set_b:  # proper superset
        print(f"{name_a} is a proper superset of {name_b}")
    elif set_a <= set_b:  # subset
        print(f"{name_a} is a subset of {name_b}")
    elif set_a >= set_b:  # superset
        print(f"{name_a} is a superset of {name_b}")
    elif set_a.isdisjoint(set_b):
        print("The sets are disjoint (no common elements)")
    else:
        print("The sets have some overlap but neither is a subset")

# Test subset relationships
basic_python = {'Alice', 'Bob'}
analyze_set_relationship(basic_python, python_students, "Basic Python", "All Python")

# Disjoint sets
freshmen = {'Ian', 'Jane', 'Kyle'}
analyze_set_relationship(freshmen, python_students, "Freshmen", "Python Students")

# Practical example: Access control
print("\n--- PRACTICAL EXAMPLE: ACCESS CONTROL ---")

admins = {'alice', 'bob'}
editors = {'alice', 'bob', 'charlie', 'diana'}
viewers = {'alice', 'bob', 'charlie', 'diana', 'eve', 'frank'}

def check_permissions(user, action):
    """Check if user has permission for action."""
    user = user.lower()

    if action == 'admin':
        return user in admins
    elif action == 'edit':
        return user in editors
    elif action == 'view':
        return user in viewers
    return False

# Test users
test_users = ['Alice', 'Charlie', 'Eve', 'George']
for user in test_users:
    can_admin = check_permissions(user, 'admin')
    can_edit = check_permissions(user, 'edit')
    can_view = check_permissions(user, 'view')

    print(f"\n{user}:")
    print(f"  Admin: {can_admin}")
    print(f"  Edit: {can_edit}")
    print(f"  View: {can_view}")

# Find users with elevated privileges
elevated = editors - viewers.symmetric_difference(editors)
print(f"\nUsers with edit access: {editors}")
print(f"Admin users: {admins}")

# More set operations
print("\n--- ADDITIONAL SET METHODS ---")

# Add and remove elements
my_set = {1, 2, 3}
print(f"Original: {my_set}")

my_set.add(4)
print(f"After add(4): {my_set}")

my_set.update([5, 6, 7])
print(f"After update([5,6,7]): {my_set}")

my_set.remove(3)  # Raises error if not present
print(f"After remove(3): {my_set}")

my_set.discard(10)  # No error if not present
print(f"After discard(10): {my_set}")

popped = my_set.pop()  # Remove and return arbitrary element
print(f"Popped: {popped}, Remaining: {my_set}")
