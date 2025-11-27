# Exercise 12: Vowel Counter - SOLUTION
# Difficulty: Beginner
# Concepts: Strings, For loops, Conditional logic, String methods

# SOLUTION
def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

# Test with examples
test_strings = [
    "Hello World",
    "Python Programming",
    "AEIOU",
    "rhythm",
    "The quick brown fox jumps over the lazy dog"
]

for text in test_strings:
    vowel_count = count_vowels(text)
    print(f"'{text}'")
    print(f"Number of vowels: {vowel_count}\n")

"""
EXPLANATION:
1. We define a string containing all vowels (both upper and lowercase)
2. We initialize a counter to 0
3. We loop through each character in the text
4. We use the 'in' operator to check if the character is in our vowels string
5. If it's a vowel, we increment the counter
6. We return the final count

Key Concepts:
- The 'in' operator checks if an element exists in a sequence
- Strings can be iterated character by character
- We can include both cases in the vowels string to handle upper/lowercase
- Counter pattern: start at 0, increment when condition is met
"""

# Alternative solution using list comprehension
print("--- ALTERNATIVE SOLUTION ---")

def count_vowels_v2(text):
    """Count vowels using list comprehension and sum."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print("\nUsing list comprehension:")
for text in test_strings[:3]:
    print(f"'{text}': {count_vowels_v2(text)} vowels")

# Extension solution: Count each vowel separately
print("\n--- EXTENSION SOLUTION ---")

def count_vowels_detailed(text):
    """Count each vowel separately and calculate vowel/consonant ratio."""
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():  # Only count letters
            if char in vowel_counts:
                vowel_counts[char] += 1
            else:
                consonant_count += 1

    total_vowels = sum(vowel_counts.values())

    # Find most common vowel
    most_common = max(vowel_counts, key=vowel_counts.get)

    # Calculate ratio
    if consonant_count > 0:
        ratio = total_vowels / consonant_count
    else:
        ratio = 0

    return vowel_counts, total_vowels, consonant_count, most_common, ratio

# Test detailed analysis
text = "The quick brown fox jumps over the lazy dog"
vowels, total_v, consonants, common, ratio = count_vowels_detailed(text)

print(f"Text: '{text}'")
print(f"\nVowel breakdown:")
for vowel, count in sorted(vowels.items()):
    print(f"  {vowel}: {count}")

print(f"\nTotal vowels: {total_v}")
print(f"Total consonants: {consonants}")
print(f"Most common vowel: {common} ({vowels[common]} occurrences)")
print(f"Vowel/Consonant ratio: {ratio:.2f}")
