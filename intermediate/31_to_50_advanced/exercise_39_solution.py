# Exercise 39: Basic Inheritance - SOLUTION
# Difficulty: Intermediate-
# Concepts: Inheritance, Parent class, Child class, super()

from datetime import datetime

# SOLUTION
class Vehicle:
    """Parent class representing a vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize vehicle.

        Args:
            make: Vehicle manufacturer
            model: Vehicle model
            year: Year of manufacture
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        """String representation."""
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        """Start the vehicle engine."""
        print("The vehicle engine starts...")

class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, make, model, year, num_doors):
        """
        Initialize car.

        Args:
            make: Car manufacturer
            model: Car model
            year: Year of manufacture
            num_doors: Number of doors
        """
        super().__init__(make, model, year)  # Call parent __init__
        self.num_doors = num_doors

    def __str__(self):
        """String representation for car."""
        return f"{self.year} {self.make} {self.model} ({self.num_doors} doors)"

    def start_engine(self):
        """Override start_engine for cars."""
        print("The car engine roars to life!")

class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""

    def __init__(self, make, model, year, has_sidecar):
        """
        Initialize motorcycle.

        Args:
            make: Motorcycle manufacturer
            model: Motorcycle model
            year: Year of manufacture
            has_sidecar: Boolean indicating if it has a sidecar
        """
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def __str__(self):
        """String representation for motorcycle."""
        sidecar_status = "with sidecar" if self.has_sidecar else "no sidecar"
        return f"{self.year} {self.make} {self.model} ({sidecar_status})"

    def start_engine(self):
        """Override start_engine for motorcycles."""
        print("The motorcycle engine rumbles!")

# Test the inheritance
print("=== Testing Inheritance ===")

car = Car("Toyota", "Camry", 2023, 4)
print(car)
car.start_engine()

print()

bike = Motorcycle("Harley-Davidson", "Street 750", 2022, False)
print(bike)
bike.start_engine()

print()

bike_with_sidecar = Motorcycle("Ural", "Gear-Up", 2021, True)
print(bike_with_sidecar)
bike_with_sidecar.start_engine()

"""
EXPLANATION:
1. Vehicle is the parent (base) class with common attributes
2. Car and Motorcycle are child (derived) classes that inherit from Vehicle
3. super().__init__() calls the parent class's __init__ method
4. Child classes add their own specific attributes (num_doors, has_sidecar)
5. Child classes can override parent methods (start_engine)
6. All vehicles have access to parent class attributes and methods

Key Concepts:
- Inheritance creates "is-a" relationships (Car is a Vehicle)
- super() provides access to parent class methods
- Child classes inherit all parent attributes and methods
- Child classes can add new attributes and methods
- Child classes can override (replace) parent methods
- This promotes code reuse and organization
"""

# Demonstrating inheritance hierarchy
print("\n--- INHERITANCE VERIFICATION ---")
print(f"Is car a Car? {isinstance(car, Car)}")
print(f"Is car a Vehicle? {isinstance(car, Vehicle)}")
print(f"Is car a Motorcycle? {isinstance(car, Motorcycle)}")

print(f"\nIs bike a Motorcycle? {isinstance(bike, Motorcycle)}")
print(f"Is bike a Vehicle? {isinstance(bike, Vehicle)}")

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

class VehicleWithAge(Vehicle):
    """Vehicle with age calculation."""

    def calculate_age(self):
        """Calculate vehicle age in years."""
        current_year = datetime.now().year
        age = current_year - self.year
        return age

    def get_info(self):
        """Get detailed vehicle information."""
        age = self.calculate_age()
        return f"{self} - {age} years old"

class EnhancedCar(VehicleWithAge):
    """Enhanced car with age calculation."""

    def __init__(self, make, model, year, num_doors):
        """Initialize enhanced car."""
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def __str__(self):
        """String representation."""
        return f"{self.year} {self.make} {self.model} ({self.num_doors} doors)"

    def start_engine(self):
        """Start car engine."""
        print("The car engine roars to life!")

class ElectricCar(EnhancedCar):
    """Electric car - inherits from EnhancedCar."""

    def __init__(self, make, model, year, num_doors, battery_capacity):
        """
        Initialize electric car.

        Args:
            make: Car manufacturer
            model: Car model
            year: Year of manufacture
            num_doors: Number of doors
            battery_capacity: Battery capacity in kWh
        """
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def __str__(self):
        """String representation."""
        return f"{self.year} {self.make} {self.model} ({self.num_doors} doors, {self.battery_capacity}kWh battery)"

    def start_engine(self):
        """Electric cars don't have traditional engines."""
        print("The electric motor hums to life silently!")

    def get_range(self):
        """Estimate range based on battery capacity (simplified)."""
        # Rough estimate: 3 miles per kWh
        estimated_range = self.battery_capacity * 3
        return estimated_range

# Test enhanced classes
print("\nTesting Enhanced Classes:")

regular_car = EnhancedCar("Honda", "Civic", 2018, 4)
print(regular_car.get_info())

electric_car = ElectricCar("Tesla", "Model 3", 2022, 4, 75)
print(electric_car)
print(f"Age: {electric_car.calculate_age()} years")
print(f"Estimated range: {electric_car.get_range()} miles")
electric_car.start_engine()

# Inheritance chain demonstration
print("\n--- INHERITANCE CHAIN ---")
print("ElectricCar inherits from EnhancedCar")
print("EnhancedCar inherits from VehicleWithAge")
print("VehicleWithAge inherits from Vehicle")
print(f"\nElectricCar's Method Resolution Order:")
print([cls.__name__ for cls in ElectricCar.__mro__])

# Method overriding demonstration
print("\n--- METHOD OVERRIDING ---")
vehicles = [
    EnhancedCar("Ford", "Focus", 2020, 4),
    ElectricCar("Nissan", "Leaf", 2023, 4, 62),
    VehicleWithAge("Generic", "Vehicle", 2015)
]

for vehicle in vehicles:
    print(f"\n{vehicle}")
    vehicle.start_engine()
