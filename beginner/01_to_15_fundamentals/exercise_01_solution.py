# Exercise 1: Temperature Converter - SOLUTION
# Difficulty: Beginner
# Concepts: Variables, Arithmetic operations, Input/Output, Type conversion

# SOLUTION
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get input from user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert and display result
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Temperature in Celsius: {celsius:.1f}°C")

"""
EXPLANATION:
1. We define a function fahrenheit_to_celsius() that takes a temperature in Fahrenheit
2. Inside the function, we apply the conversion formula: (F - 32) * 5/9
3. We use input() to get user input as a string, then convert it to float
4. We call our function with the user's input and store the result
5. We use an f-string to format and display the result with 1 decimal place

Key Concepts:
- float() converts strings to floating-point numbers
- Functions help organize code and make it reusable
- f-strings (f"...{variable}...") allow easy string formatting
- The :.1f format specifier shows 1 decimal place
"""

# Extension solution: Bidirectional converter
print("\n--- EXTENSION SOLUTION ---")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

choice = input("Convert (F)ahrenheit to Celsius or (C)elsius to Fahrenheit? ").upper()

if choice == 'F':
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temp)
    print(f"Temperature in Celsius: {result:.1f}°C")
elif choice == 'C':
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temp)
    print(f"Temperature in Fahrenheit: {result:.1f}°F")
else:
    print("Invalid choice!")
