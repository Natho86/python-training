# Exercise 39: Basic Inheritance
# Difficulty: Intermediate-
# Concepts: Inheritance, Parent class, Child class, super()

"""
PROBLEM:
Create a Vehicle parent class with attributes: make, model, year
Then create two child classes:
1. Car - adds attribute: num_doors
2. Motorcycle - adds attribute: has_sidecar

Each class should have:
- __init__ method (using super() to call parent's __init__)
- __str__ method that provides appropriate description
- A start_engine() method

EXAMPLE:
car = Car("Toyota", "Camry", 2023, 4)
print(car)  # "2023 Toyota Camry (4 doors)"
car.start_engine()  # "The car engine roars to life!"

bike = Motorcycle("Harley-Davidson", "Street 750", 2022, False)
print(bike)  # "2022 Harley-Davidson Street 750 (no sidecar)"
bike.start_engine()  # "The motorcycle engine rumbles!"

HINTS:
1. Use class ChildClass(ParentClass): to inherit
2. Use super().__init__() to call parent's __init__ method
3. Child classes inherit all parent methods and can override them

EXTENSION:
Add a calculate_age() method to the Vehicle class that calculates the vehicle's age.
Then create an ElectricCar class that inherits from Car and adds battery_capacity attribute.
"""

# Write your solution here
