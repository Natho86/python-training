# Exercise 43: Collections Module (Counter, defaultdict)
# Difficulty: Intermediate-
# Concepts: collections module, Counter, defaultdict, Specialized data structures

"""
PROBLEM:
Use the collections module to:
1. Count the frequency of words in a text using Counter
2. Find the most common words
3. Use defaultdict to group items by category
4. Use namedtuple to create simple data structures

EXAMPLE:
Text: "the quick brown fox jumps over the lazy dog the fox"
Word frequencies:
- 'the': 3
- 'fox': 2
- 'quick': 1
Most common words: [('the', 3), ('fox', 2)]

Items grouped by type:
- fruit: ['apple', 'banana', 'orange']
- vegetable: ['carrot', 'celery']

HINTS:
1. Counter is like a dictionary but specialized for counting
2. Counter.most_common(n) returns the n most frequent items
3. defaultdict automatically creates default values for missing keys
4. Import with: from collections import Counter, defaultdict

EXTENSION:
Create a program that analyzes a paragraph of text to find:
- Most common words (excluding common words like 'the', 'a', 'is')
- Average word length
- Word frequency distribution
"""

# Write your solution here
