# Exercise 15: Prime Number Checker - SOLUTION
# Difficulty: Beginner
# Concepts: Functions, Loops, Conditional logic, Mathematical operations

# SOLUTION
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Test individual numbers
test_numbers = [1, 2, 7, 17, 20, 25, 29, 100]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

print("\n" + "="*40 + "\n")

def find_primes(limit):
    """Find all prime numbers up to a limit."""
    primes = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes

# Find primes up to 30
primes = find_primes(30)
print(f"Prime numbers up to 30: {primes}")

"""
EXPLANATION:
1. A prime number must be greater than 1
2. We check if the number is divisible by any number from 2 to n-1
3. If we find any divisor (n % i == 0), the number is not prime
4. If we check all numbers and find no divisors, it's prime
5. To find all primes up to a limit, we test each number

Key Concepts:
- Early return: if we find a divisor, we immediately return False
- range(2, n) generates numbers from 2 to n-1
- Modulo (%) operator checks for divisibility
- Building a list by appending elements that meet a condition
"""

# Optimized version: only check up to square root
print("\n--- OPTIMIZED VERSION ---")
import math

def is_prime_optimized(n):
    """Optimized prime check (only check up to sqrt(n))."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Even numbers (except 2) aren't prime
        return False

    # Only check odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

# Compare performance
import time

limit = 1000
start = time.time()
primes1 = [n for n in range(2, limit) if is_prime(n)]
time1 = time.time() - start

start = time.time()
primes2 = [n for n in range(2, limit) if is_prime_optimized(n)]
time2 = time.time() - start

print(f"Basic method: {len(primes1)} primes found in {time1:.4f} seconds")
print(f"Optimized method: {len(primes2)} primes found in {time2:.4f} seconds")

# Extension solution: Sieve of Eratosthenes
print("\n--- EXTENSION SOLUTION ---")

def sieve_of_eratosthenes(limit):
    """Find primes using Sieve of Eratosthenes algorithm."""
    # Create a boolean array and initialize all as true
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False  # 0 and 1 are not prime

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_arr[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False

    # Collect all numbers that are still marked as prime
    return [i for i in range(limit + 1) if is_prime_arr[i]]

# Test Sieve
start = time.time()
primes_sieve = sieve_of_eratosthenes(1000)
time_sieve = time.time() - start

print(f"Sieve of Eratosthenes: {len(primes_sieve)} primes in {time_sieve:.4f} seconds")
print(f"First 20 primes: {primes_sieve[:20]}")

# Calculate prime density
def prime_density(limit):
    """Calculate the percentage of primes up to a limit."""
    primes = sieve_of_eratosthenes(limit)
    density = (len(primes) / limit) * 100
    return len(primes), density

count, density = prime_density(1000)
print(f"\nUp to 1000: {count} primes ({density:.2f}% density)")

count, density = prime_density(10000)
print(f"Up to 10,000: {count} primes ({density:.2f}% density)")
