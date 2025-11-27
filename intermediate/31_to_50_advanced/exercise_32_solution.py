# Exercise 32: Function with **kwargs - SOLUTION
# Difficulty: Intermediate-
# Concepts: **kwargs, Keyword arguments, Dictionaries

# SOLUTION
def build_profile(first_name, last_name, **kwargs):
    """
    Build a user profile dictionary.

    Args:
        first_name: User's first name
        last_name: User's last name
        **kwargs: Any additional profile information
    """
    profile = {
        'first_name': first_name,
        'last_name': last_name
    }
    # Add all additional keyword arguments to the profile
    profile.update(kwargs)
    return profile

# Test cases
print("Testing build_profile:")
profile1 = build_profile("John", "Doe", location="New York", age=30, job="Developer")
print(f"Profile 1: {profile1}")

profile2 = build_profile("Jane", "Smith", email="jane@example.com", hobby="Photography")
print(f"Profile 2: {profile2}")

profile3 = build_profile("Alice", "Johnson")  # No extra kwargs
print(f"Profile 3: {profile3}")

"""
EXPLANATION:
1. The function has two required parameters: first_name and last_name
2. **kwargs collects all additional keyword arguments into a dictionary
3. We create a base profile dictionary with the required fields
4. We use .update(kwargs) to add all keyword arguments to the profile
5. This allows the function to accept any number of additional fields

Key Concepts:
- **kwargs collects keyword arguments into a dictionary
- The name 'kwargs' is convention (keyword arguments)
- You can combine regular parameters with **kwargs
- dict.update() merges one dictionary into another
- This pattern creates very flexible functions
"""

# Alternative solution without .update()
print("\n--- ALTERNATIVE SOLUTION ---")

def build_profile_alt(first_name, last_name, **kwargs):
    """Alternative implementation using dictionary unpacking."""
    return {
        'first_name': first_name,
        'last_name': last_name,
        **kwargs  # Dictionary unpacking
    }

profile = build_profile_alt("Bob", "Wilson", city="Boston", age=25)
print(f"Alternative profile: {profile}")

# Extension solution: Create car description
print("\n--- EXTENSION SOLUTION ---")

def create_car(make, model, **features):
    """
    Create a formatted car description.

    Args:
        make: Car manufacturer
        model: Car model
        **features: Optional features (color, year, transmission, etc.)
    """
    car_info = f"{make} {model}"

    if features:
        car_info += " with the following features:"
        for feature, value in features.items():
            # Convert feature name from snake_case to Title Case
            feature_name = feature.replace('_', ' ').title()
            car_info += f"\n  - {feature_name}: {value}"
    else:
        car_info += " (no additional features specified)"

    return car_info

print("\nCar 1:")
print(create_car("Toyota", "Camry", color="Blue", year=2023, transmission="Automatic"))

print("\nCar 2:")
print(create_car("Tesla", "Model 3", color="Red", year=2024,
                 autopilot=True, range="358 miles"))

print("\nCar 3:")
print(create_car("Honda", "Civic"))

# Bonus: Combining *args and **kwargs
print("\n--- BONUS: *args and **kwargs together ---")

def make_pizza(size, *toppings, **details):
    """
    Make a pizza with any toppings and additional details.

    Args:
        size: Size of pizza (small, medium, large)
        *toppings: Any number of toppings
        **details: Additional details (crust_type, sauce, etc.)
    """
    pizza = f"{size.capitalize()} pizza"

    if toppings:
        pizza += " with " + ", ".join(toppings)

    if details:
        pizza += " ("
        details_list = [f"{k}={v}" for k, v in details.items()]
        pizza += ", ".join(details_list)
        pizza += ")"

    return pizza

print(make_pizza("large", "pepperoni", "mushrooms", "olives",
                 crust_type="thin", sauce="marinara"))
print(make_pizza("medium", "cheese", delivery=True))
