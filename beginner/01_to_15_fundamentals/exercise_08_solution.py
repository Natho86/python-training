# Exercise 8: Palindrome Checker - SOLUTION
# Difficulty: Beginner
# Concepts: Strings, String slicing, Comparison operators, String methods

# SOLUTION
def is_palindrome(text):
    """Check if a string is a palindrome."""
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ""
    for char in text.lower():
        if char.isalnum():  # Check if character is alphanumeric
            cleaned += char

    # Compare with reverse
    return cleaned == cleaned[::-1]

# Test with examples
test_cases = [
    "racecar",
    "A man a plan a canal Panama",
    "hello",
    "Was it a car or a cat I saw?",
    "python"
]

for text in test_cases:
    if is_palindrome(text):
        print(f'"{text}" is a palindrome!')
    else:
        print(f'"{text}" is not a palindrome.')

"""
EXPLANATION:
1. We convert the string to lowercase using .lower() for case-insensitive comparison
2. We build a new string (cleaned) containing only alphanumeric characters
3. The isalnum() method returns True if a character is a letter or digit
4. We use slicing [::-1] to reverse the string
5. We compare the cleaned string with its reverse

Key Concepts:
- String slicing with [::-1] reverses a string
- .lower() converts all characters to lowercase
- .isalnum() checks if a character is alphanumeric (letter or number)
- Strings can be compared with == operator
- Building a new string character by character
"""

# Alternative solution using list comprehension and join
print("\n--- ALTERNATIVE SOLUTION ---")

def is_palindrome_v2(text):
    """Palindrome checker using list comprehension."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

print("\nUsing list comprehension:")
for text in test_cases[:3]:
    result = "is a palindrome!" if is_palindrome_v2(text) else "is not a palindrome."
    print(f'"{text}" {result}')

# Extension solution: Find longest palindromic substring
print("\n--- EXTENSION SOLUTION ---")

def longest_palindrome_substring(text):
    """Find the longest palindromic substring."""
    text = text.lower().replace(" ", "")
    longest = ""

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring

    return longest

test_string = "babad"
result = longest_palindrome_substring(test_string)
print(f"Longest palindromic substring in '{test_string}': '{result}'")

test_string2 = "racecar is a palindrome"
result2 = longest_palindrome_substring(test_string2)
print(f"Longest palindromic substring in '{test_string2}': '{result2}'")
