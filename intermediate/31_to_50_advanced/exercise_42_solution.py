# Exercise 42: Math Module and Calculations - SOLUTION
# Difficulty: Intermediate-
# Concepts: math module, Mathematical functions, Constants

import math

# SOLUTION
print("=== Math Module Examples ===")

# Circle calculations
def circle_area(radius):
    """Calculate area of circle."""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of circle."""
    return 2 * math.pi * radius

radius = 5
area = circle_area(radius)
circumference = circle_circumference(radius)

print(f"\nCircle with radius {radius}:")
print(f"  Area: {area:.2f}")
print(f"  Circumference: {circumference:.2f}")
print(f"  Pi constant: {math.pi}")

# Distance between two points
def distance(x1, y1, x2, y2):
    """Calculate distance between two points using Pythagorean theorem."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

dist = distance(0, 0, 3, 4)
print(f"\nDistance between (0,0) and (3,4): {dist}")

dist2 = distance(1, 2, 4, 6)
print(f"Distance between (1,2) and (4,6): {dist2:.2f}")

# Rounding methods
print("\n--- Rounding Methods ---")
number = 4.7
print(f"Number: {number}")
print(f"  Floor (round down): {math.floor(number)}")
print(f"  Ceil (round up): {math.ceil(number)}")
print(f"  Round (nearest): {round(number)}")

number2 = -4.3
print(f"\nNumber: {number2}")
print(f"  Floor: {math.floor(number2)}")  # -5 (towards -infinity)
print(f"  Ceil: {math.ceil(number2)}")    # -4 (towards +infinity)
print(f"  Round: {round(number2)}")       # -4

# Powers and roots
print("\n--- Powers and Roots ---")
print(f"2^8 = {math.pow(2, 8)}")
print(f"2^8 = {2**8} (using ** operator)")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Square root of 2: {math.sqrt(2):.4f}")
print(f"Cube root of 27: {27 ** (1/3):.2f}")

# Logarithms
print("\n--- Logarithms ---")
print(f"log(100) base 10: {math.log10(100)}")
print(f"log(8) base 2: {math.log2(8)}")
print(f"Natural log of e: {math.log(math.e)}")

# Trigonometry (requires radians)
print("\n--- Trigonometry ---")
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(f"Angle: {angle_degrees}° = {angle_radians:.4f} radians")
print(f"  sin(45°): {math.sin(angle_radians):.4f}")
print(f"  cos(45°): {math.cos(angle_radians):.4f}")
print(f"  tan(45°): {math.tan(angle_radians):.4f}")

# Other useful functions
print("\n--- Other Math Functions ---")
print(f"Absolute value of -10: {math.fabs(-10)}")
print(f"Factorial of 5: {math.factorial(5)}")  # 5! = 5*4*3*2*1
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")  # Greatest common divisor

"""
EXPLANATION:
1. math module provides mathematical functions and constants
2. math.pi and math.e are mathematical constants
3. math.sqrt() calculates square root
4. math.floor() rounds down to nearest integer
5. math.ceil() rounds up to nearest integer
6. math.pow(x, y) calculates x^y (prefer ** operator)
7. Trigonometric functions use radians, not degrees
8. math.radians() and math.degrees() convert between them

Key Concepts:
- math module is part of Python standard library
- More accurate than manual calculations for special functions
- Always returns float, even for integer-like results
- For complex numbers, use cmath module
"""

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

def sphere_volume(radius):
    """Calculate volume of sphere: (4/3)πr³"""
    return (4/3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    """Calculate surface area of sphere: 4πr²"""
    return 4 * math.pi * radius ** 2

def cylinder_volume(radius, height):
    """Calculate volume of cylinder: πr²h"""
    return math.pi * radius ** 2 * height

def cone_volume(radius, height):
    """Calculate volume of cone: (1/3)πr²h"""
    return (1/3) * math.pi * radius ** 2 * height

def cube_volume(side):
    """Calculate volume of cube: s³"""
    return side ** 3

# Test 3D shape calculations
print("\n3D Shape Volumes:")
print(f"Sphere (r=3): {sphere_volume(3):.2f}")
print(f"Sphere surface area (r=3): {sphere_surface_area(3):.2f}")
print(f"Cylinder (r=2, h=5): {cylinder_volume(2, 5):.2f}")
print(f"Cone (r=3, h=4): {cone_volume(3, 4):.2f}")
print(f"Cube (s=4): {cube_volume(4):.2f}")

# Angle conversions
print("\n--- Angle Conversions ---")

def angle_info(degrees):
    """Show angle in both degrees and radians with trig values."""
    radians = math.radians(degrees)
    print(f"\n{degrees}° = {radians:.4f} radians")
    print(f"  sin: {math.sin(radians):.4f}")
    print(f"  cos: {math.cos(radians):.4f}")
    print(f"  tan: {math.tan(radians):.4f}")

angle_info(0)
angle_info(30)
angle_info(45)
angle_info(60)
angle_info(90)

# Convert radians back to degrees
print(f"\nπ radians = {math.degrees(math.pi)}°")
print(f"π/2 radians = {math.degrees(math.pi/2)}°")

# Practical examples
print("\n--- PRACTICAL EXAMPLES ---")

# Calculate hypotenuse of right triangle
def hypotenuse(a, b):
    """Calculate hypotenuse using Pythagorean theorem."""
    return math.sqrt(a**2 + b**2)

print(f"\nRight triangle with sides 3 and 4:")
print(f"Hypotenuse: {hypotenuse(3, 4)}")

# Calculate compound interest
def compound_interest(principal, rate, time, compounds_per_year=12):
    """
    Calculate compound interest.

    Args:
        principal: Initial amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time in years
        compounds_per_year: Number of times interest compounds per year

    Returns:
        Final amount
    """
    amount = principal * math.pow(1 + rate/compounds_per_year,
                                  compounds_per_year * time)
    return amount

principal = 1000
rate = 0.05  # 5%
time = 10
final = compound_interest(principal, rate, time)
print(f"\nCompound Interest:")
print(f"Principal: ${principal}")
print(f"Rate: {rate*100}% per year")
print(f"Time: {time} years")
print(f"Final amount: ${final:.2f}")
print(f"Interest earned: ${final - principal:.2f}")

# BMI calculator
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 70  # kg
height = 1.75  # meters
bmi = calculate_bmi(weight, height)
print(f"\nBMI Calculator:")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")
print(f"Category: {bmi_category(bmi)}")

# Statistics functions
print("\n--- STATISTICAL CALCULATIONS ---")

numbers = [2, 4, 6, 8, 10]

def mean(numbers):
    """Calculate arithmetic mean (average)."""
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    """Calculate standard deviation."""
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

print(f"Numbers: {numbers}")
print(f"Mean: {mean(numbers):.2f}")
print(f"Standard deviation: {standard_deviation(numbers):.2f}")
