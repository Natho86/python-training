# Exercise 9: Password Validator - SOLUTION
# Difficulty: Beginner
# Concepts: Strings, String methods, Control flow, Logical operators

# SOLUTION
def validate_password(password):
    """Validate password based on requirements."""
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    # Check for uppercase, lowercase, and digit
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    # Validate all requirements
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"

    return True, "Valid password!"

# Test with examples
test_passwords = [
    "Pass123",
    "password123",
    "Password123",
    "SHORT1",
    "NoDigitsHere",
    "MyP@ssw0rd"
]

for pwd in test_passwords:
    is_valid, message = validate_password(pwd)
    status = "✓" if is_valid else "✗"
    print(f"{status} '{pwd}': {message}")

"""
EXPLANATION:
1. We check the length first using len()
2. We initialize boolean flags for each requirement
3. We loop through each character in the password
4. We use .isupper(), .islower(), and .isdigit() to check character types
5. After the loop, we check if all requirements are met
6. We return a tuple with (True/False, message) for feedback

Key Concepts:
- len() returns the length of a string
- Boolean flags track whether conditions have been met
- .isupper() checks if a character is uppercase
- .islower() checks if a character is lowercase
- .isdigit() checks if a character is a digit
- Returning tuples allows returning multiple values
"""

# Alternative solution using any()
print("\n--- ALTERNATIVE SOLUTION ---")

def validate_password_v2(password):
    """Validate password using any() function."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit"

    return True, "Valid password!"

print("\nUsing any() function:")
for pwd in test_passwords[:3]:
    is_valid, message = validate_password_v2(pwd)
    print(f"'{pwd}': {message}")

# Extension solution: Advanced validation
print("\n--- EXTENSION SOLUTION ---")

def validate_password_advanced(password):
    """Advanced password validation with special characters."""
    errors = []

    # Length check
    if len(password) < 8:
        errors.append("Must be at least 8 characters long")

    # Character type checks
    if not any(c.isupper() for c in password):
        errors.append("Must contain at least one uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Must contain at least one lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Must contain at least one digit")

    # Special character check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        errors.append("Must contain at least one special character (!@#$%, etc.)")

    # Check for repeated characters (more than 2 in a row)
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            errors.append("Cannot have more than 2 repeated characters in a row")
            break

    if errors:
        return False, "Invalid - " + "; ".join(errors)
    else:
        return True, "Valid password!"

# Test advanced validation
advanced_tests = ["Password123!", "Pass111word", "MyP@ssw0rd", "weak"]
print("\nAdvanced validation:")
for pwd in advanced_tests:
    is_valid, message = validate_password_advanced(pwd)
    status = "✓" if is_valid else "✗"
    print(f"{status} '{pwd}'")
    print(f"  {message}")
