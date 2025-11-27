# Exercise 14: List Reverser - SOLUTION
# Difficulty: Beginner
# Concepts: Lists, List slicing, Loops, Functions

# SOLUTION
def reverse_list(lst):
    """Reverse a list by swapping elements."""
    left = 0
    right = len(lst) - 1

    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]

        # Move pointers toward center
        left += 1
        right -= 1

    return lst

# Test with examples
test1 = [1, 2, 3, 4, 5]
test2 = ["apple", "banana", "cherry"]

print(f"Original: {test1}")
print(f"Reversed: {reverse_list(test1.copy())}")  # Use copy to preserve original

print(f"\nOriginal: {test2}")
print(f"Reversed: {reverse_list(test2.copy())}")

"""
EXPLANATION:
1. We use two pointers: left starts at 0, right starts at the last index
2. We swap the elements at these positions using tuple unpacking
3. We move left forward and right backward
4. We continue until the pointers meet (left < right)
5. This modifies the list in-place and also returns it

Key Concepts:
- Two-pointer technique: using two indices moving toward each other
- Tuple unpacking for swapping: a, b = b, a swaps values without temp variable
- len(lst) - 1 gives us the last index
- While loop continues as long as left < right
- .copy() creates a copy of the list (so we don't modify the original)
"""

# Alternative solution: Creating a new list
print("\n--- ALTERNATIVE SOLUTION ---")

def reverse_list_v2(lst):
    """Reverse a list by building a new one."""
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

test3 = [10, 20, 30, 40]
print(f"Original: {test3}")
print(f"Reversed (new list): {reverse_list_v2(test3)}")
print(f"Original unchanged: {test3}")

# Extension solution: Reverse portion of list
print("\n--- EXTENSION SOLUTION ---")

def reverse_portion(lst, start, end):
    """Reverse only a portion of the list."""
    # Make a copy to not modify original
    result = lst.copy()

    left = start
    right = end

    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return result

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal: {test_list}")
print(f"Reverse portion [2:6]: {reverse_portion(test_list, 2, 6)}")

# Reverse words in a sentence
def reverse_words(sentence):
    """Reverse each word while keeping word order."""
    words = sentence.split()
    reversed_words = []

    for word in words:
        # Convert word to list, reverse it, join back to string
        word_list = list(word)
        reverse_list(word_list)
        reversed_words.append(''.join(word_list))

    return ' '.join(reversed_words)

sentence = "Hello World Python"
print(f"\nOriginal sentence: {sentence}")
print(f"Reversed words: {reverse_words(sentence)}")

# Reverse word order in sentence
def reverse_word_order(sentence):
    """Reverse the order of words in a sentence."""
    words = sentence.split()
    reverse_list(words)
    return ' '.join(words)

print(f"Reversed word order: {reverse_word_order(sentence)}")
