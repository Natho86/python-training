# Exercise 48: Custom Module Creation - SOLUTION
# Difficulty: Intermediate
# Concepts: Modules, Imports, Code organization, Reusability

"""
This solution demonstrates creating custom modules.
We'll create the module files inline, then show how to use them.
"""

# First, let's create the text_utils module content
text_utils_code = '''
"""
text_utils.py - Text processing utilities

This module provides various text manipulation functions.
"""

def word_count(text):
    """
    Count words in text.

    Args:
        text: Input string

    Returns:
        int: Number of words
    """
    if not text:
        return 0
    return len(text.split())

def char_frequency(text):
    """
    Calculate character frequency.

    Args:
        text: Input string

    Returns:
        dict: Character frequency dictionary
    """
    freq = {}
    for char in text.lower():
        if char.isalnum():  # Only count letters and numbers
            freq[char] = freq.get(char, 0) + 1
    return freq

def reverse_words(text):
    """
    Reverse the order of words in text.

    Args:
        text: Input string

    Returns:
        str: Text with reversed word order
    """
    words = text.split()
    return ' '.join(reversed(words))

def title_case(text):
    """
    Convert text to title case (first letter of each word capitalized).

    Args:
        text: Input string

    Returns:
        str: Text in title case
    """
    return ' '.join(word.capitalize() for word in text.split())

def remove_punctuation(text):
    """
    Remove all punctuation from text.

    Args:
        text: Input string

    Returns:
        str: Text without punctuation
    """
    import string
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def longest_word(text):
    """
    Find the longest word in text.

    Args:
        text: Input string

    Returns:
        str: Longest word
    """
    words = text.split()
    return max(words, key=len) if words else ""

def word_frequency(text):
    """
    Calculate word frequency.

    Args:
        text: Input string

    Returns:
        dict: Word frequency dictionary
    """
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
'''

# Create math_utils module content
math_utils_code = '''
"""
math_utils.py - Mathematical utility functions

This module provides various mathematical operations.
"""

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def factorial(n):
    """
    Calculate factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        int: n! (factorial of n)
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """
    Generate first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate

    Returns:
        list: First n Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def gcd(a, b):
    """
    Calculate greatest common divisor using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        int: Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """
    Calculate least common multiple.

    Args:
        a: First integer
        b: Second integer

    Returns:
        int: Least common multiple
    """
    return abs(a * b) // gcd(a, b)

def is_perfect_square(n):
    """
    Check if number is a perfect square.

    Args:
        n: Integer to check

    Returns:
        bool: True if perfect square
    """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def prime_factors(n):
    """
    Find prime factors of n.

    Args:
        n: Integer to factorize

    Returns:
        list: Prime factors
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
'''

# Create the module files
print("Creating custom modules...")

with open('text_utils.py', 'w') as f:
    f.write(text_utils_code)
print("✓ Created text_utils.py")

with open('math_utils.py', 'w') as f:
    f.write(math_utils_code)
print("✓ Created math_utils.py")

# Now demonstrate using the modules
print("\n" + "="*60)
print("DEMONSTRATING MODULE USAGE")
print("="*60)

# Import from our custom modules
from text_utils import (word_count, char_frequency, reverse_words,
                       title_case, remove_punctuation, longest_word,
                       word_frequency)

from math_utils import (is_prime, factorial, fibonacci, gcd,
                       lcm, is_perfect_square, prime_factors)

# Test text_utils functions
print("\n--- TEXT UTILITIES ---")

text = "Hello World! Python is awesome, Python rocks!"
print(f"Text: {text}")
print(f"Word count: {word_count(text)}")
print(f"Longest word: {longest_word(text)}")
print(f"Reversed words: {reverse_words(text)}")
print(f"Title case: {title_case(text.lower())}")
print(f"Without punctuation: {remove_punctuation(text)}")

print(f"\nCharacter frequency:")
for char, freq in sorted(char_frequency(text).items()):
    print(f"  '{char}': {freq}")

print(f"\nWord frequency:")
for word, freq in word_frequency(text).items():
    print(f"  '{word}': {freq}")

# Test math_utils functions
print("\n--- MATH UTILITIES ---")

print(f"\nPrime numbers from 1-20:")
primes = [n for n in range(1, 21) if is_prime(n)]
print(f"  {primes}")

print(f"\nFactorials:")
for n in range(6):
    print(f"  {n}! = {factorial(n)}")

print(f"\nFirst 10 Fibonacci numbers:")
print(f"  {fibonacci(10)}")

print(f"\nGCD and LCM:")
print(f"  GCD(48, 18) = {gcd(48, 18)}")
print(f"  LCM(48, 18) = {lcm(48, 18)}")

print(f"\nPerfect squares from 1-20:")
squares = [n for n in range(1, 21) if is_perfect_square(n)]
print(f"  {squares}")

print(f"\nPrime factorization:")
for n in [12, 24, 60, 100]:
    factors = prime_factors(n)
    print(f"  {n} = {' × '.join(map(str, factors))}")

"""
EXPLANATION:
1. Modules are Python files with functions and variables
2. Import with: from module import function
3. Modules promote code reusability and organization
4. Each module has a docstring explaining its purpose
5. Functions in modules should have clear documentation
6. Modules can import other modules
7. Module code runs when imported (use if __name__ == "__main__" to prevent)

Key Concepts:
- Modules organize code into logical units
- Functions in modules can be imported selectively
- Modules create namespaces (avoid naming conflicts)
- Good modules are focused and single-purpose
- Docstrings make modules self-documenting
"""

# Extension solution - data validation module
print("\n--- EXTENSION SOLUTION ---")

data_utils_code = '''
"""
data_utils.py - Data validation utilities

This module provides validation functions for common data types.
"""

import re

def is_valid_email(email):
    """
    Validate email address format.

    Args:
        email: Email string to validate

    Returns:
        bool: True if valid email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    """
    Validate US phone number format.

    Args:
        phone: Phone number string

    Returns:
        bool: True if valid phone format
    """
    # Remove common separators
    cleaned = re.sub(r'[\\s\\-\\(\\)\\.]', '', phone)
    # Check if 10 or 11 digits (with or without country code)
    return len(cleaned) in [10, 11] and cleaned.isdigit()

def is_valid_url(url):
    """
    Validate URL format.

    Args:
        url: URL string to validate

    Returns:
        bool: True if valid URL format
    """
    pattern = r'^https?:\\/\\/([\\w\\-]+\\.)+[\\w\\-]+(\\/[\\w\\-._~:/?#\\[\\]@!$&\'()*+,;=]*)?$'
    return bool(re.match(pattern, url))

def is_valid_zipcode(zipcode):
    """
    Validate US ZIP code format.

    Args:
        zipcode: ZIP code string

    Returns:
        bool: True if valid ZIP format (12345 or 12345-6789)
    """
    pattern = r'^\\d{5}(-\\d{4})?$'
    return bool(re.match(pattern, zipcode))

def sanitize_string(text, max_length=None):
    """
    Sanitize string by removing dangerous characters.

    Args:
        text: Input string
        max_length: Maximum allowed length

    Returns:
        str: Sanitized string
    """
    # Remove control characters
    sanitized = ''.join(char for char in text if char.isprintable())

    # Trim to max length if specified
    if max_length:
        sanitized = sanitized[:max_length]

    return sanitized.strip()
'''

# Create data_utils module
with open('data_utils.py', 'w') as f:
    f.write(data_utils_code)
print("\n✓ Created data_utils.py")

# Test data validation
from data_utils import (is_valid_email, is_valid_phone,
                       is_valid_url, is_valid_zipcode)

print("\n--- DATA VALIDATION ---")

# Test emails
emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.co.uk",
    "@invalid.com"
]
print("\nEmail validation:")
for email in emails:
    valid = "✓" if is_valid_email(email) else "✗"
    print(f"  {valid} {email}")

# Test phone numbers
phones = [
    "123-456-7890",
    "(555) 123-4567",
    "5551234567",
    "555-CALL"
]
print("\nPhone validation:")
for phone in phones:
    valid = "✓" if is_valid_phone(phone) else "✗"
    print(f"  {valid} {phone}")

# Test URLs
urls = [
    "https://www.example.com",
    "http://example.com/path",
    "not a url",
    "ftp://files.example.com"
]
print("\nURL validation:")
for url in urls:
    valid = "✓" if is_valid_url(url) else "✗"
    print(f"  {valid} {url}")

# Demonstrate module reloading
print("\n--- MODULE INTROSPECTION ---")
import text_utils
print(f"\ntext_utils module docstring:")
print(f"  {text_utils.__doc__.strip()}")

print(f"\nAvailable functions in text_utils:")
functions = [name for name in dir(text_utils) if not name.startswith('_')]
for func in functions:
    print(f"  - {func}")

print("\n" + "="*60)
print("Custom modules created and tested successfully!")
print("="*60)
