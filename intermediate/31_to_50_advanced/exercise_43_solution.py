# Exercise 43: Collections Module (Counter, defaultdict) - SOLUTION
# Difficulty: Intermediate-
# Concepts: collections module, Counter, defaultdict, Specialized data structures

from collections import Counter, defaultdict, namedtuple, deque

# SOLUTION
print("=== Counter Example ===")

# Word frequency counting
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

word_count = Counter(words)
print(f"Text: {text}")
print(f"\nWord frequencies:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# Most common words
print(f"\nMost common words:")
most_common = word_count.most_common(2)
for word, count in most_common:
    print(f"  {word}: {count}")

# Counter operations
print("\n--- Counter Operations ---")
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"Counter 1: {c1}")
print(f"Most common: {c1.most_common(1)}")
print(f"Total count: {sum(c1.values())}")

# Adding counters
c2 = Counter(['a', 'b', 'd'])
combined = c1 + c2
print(f"Counter 2: {c2}")
print(f"Combined: {combined}")

# Defaultdict example
print("\n=== Defaultdict Example ===")

# Group items by category
items = [
    ('apple', 'fruit'),
    ('carrot', 'vegetable'),
    ('banana', 'fruit'),
    ('celery', 'vegetable'),
    ('orange', 'fruit')
]

# Using defaultdict with list
grouped = defaultdict(list)
for item, category in items:
    grouped[category].append(item)

print("Items grouped by type:")
for category, item_list in grouped.items():
    print(f"  {category}: {item_list}")

# Defaultdict with int (for counting)
print("\n--- Defaultdict for Counting ---")
text_chars = "hello world"
char_count = defaultdict(int)
for char in text_chars:
    if char != ' ':
        char_count[char] += 1

print(f"Character counts in '{text_chars}':")
for char, count in sorted(char_count.items()):
    print(f"  '{char}': {count}")

# Namedtuple example
print("\n=== Namedtuple Example ===")

# Create a namedtuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person1 = Person('Alice', 30, 'New York')
person2 = Person('Bob', 25, 'Boston')

print(f"Person 1: {person1}")
print(f"  Name: {person1.name}")
print(f"  Age: {person1.age}")
print(f"  City: {person1.city}")

# Namedtuples are immutable
print("\nNamedtuples are like lightweight classes:")
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(f"Point: {p1}, x={p1.x}, y={p1.y}")

"""
EXPLANATION:
1. Counter is a dict subclass for counting hashable objects
2. Counter.most_common(n) returns list of n most frequent elements
3. defaultdict never raises KeyError - creates default value for missing keys
4. defaultdict(list) creates empty list for new keys
5. defaultdict(int) creates 0 for new keys
6. namedtuple creates tuple subclasses with named fields

Key Concepts:
- collections module provides specialized container datatypes
- Counter simplifies counting and frequency analysis
- defaultdict eliminates need to check if key exists
- namedtuple creates simple classes without boilerplate
- These tools make code cleaner and more efficient
"""

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

def analyze_text(text, exclude_words=None):
    """
    Comprehensive text analysis.

    Args:
        text: Text to analyze
        exclude_words: Set of words to exclude (stop words)

    Returns:
        Dictionary with analysis results
    """
    if exclude_words is None:
        exclude_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on',
                        'at', 'to', 'for', 'of', 'with', 'is', 'was', 'are'}

    # Clean and split text
    words = text.lower().replace(',', '').replace('.', '').split()

    # Filter out excluded words
    filtered_words = [w for w in words if w not in exclude_words]

    # Count words
    word_count = Counter(filtered_words)

    # Calculate statistics
    total_words = len(words)
    unique_words = len(word_count)
    avg_word_length = sum(len(w) for w in filtered_words) / len(filtered_words) if filtered_words else 0

    # Word length distribution
    length_dist = Counter(len(w) for w in filtered_words)

    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'most_common': word_count.most_common(5),
        'avg_word_length': avg_word_length,
        'length_distribution': dict(length_dist)
    }

# Test text analysis
sample_text = """
Python is a high-level programming language. Python is widely used for web
development, data analysis, artificial intelligence, and scientific computing.
Python's syntax is clear and readable, making it an excellent choice for
beginners and experts alike.
"""

results = analyze_text(sample_text)
print("\nText Analysis Results:")
print(f"Total words: {results['total_words']}")
print(f"Unique words: {results['unique_words']}")
print(f"Average word length: {results['avg_word_length']:.1f} characters")
print(f"\nMost common words (excluding stop words):")
for word, count in results['most_common']:
    print(f"  {word}: {count}")
print(f"\nWord length distribution:")
for length, count in sorted(results['length_distribution'].items()):
    print(f"  {length} chars: {count} words")

# More collections examples
print("\n--- MORE COLLECTIONS EXAMPLES ---")

# Deque (double-ended queue)
print("\nDeque (efficient insertions/deletions at both ends):")
d = deque([1, 2, 3, 4, 5])
print(f"Initial: {d}")
d.append(6)  # Add to right
d.appendleft(0)  # Add to left
print(f"After appends: {d}")
d.pop()  # Remove from right
d.popleft()  # Remove from left
print(f"After pops: {d}")

# Deque with maxlen (circular buffer)
recent_items = deque(maxlen=3)
for i in range(5):
    recent_items.append(i)
    print(f"Added {i}: {list(recent_items)}")

# Practical example: Task tracker with priorities
print("\n--- PRACTICAL EXAMPLE: Task Tracker ---")

Task = namedtuple('Task', ['name', 'priority', 'status'])

tasks = [
    Task('Write report', 'high', 'in_progress'),
    Task('Send emails', 'medium', 'pending'),
    Task('Review code', 'high', 'pending'),
    Task('Update docs', 'low', 'completed'),
    Task('Fix bug', 'high', 'in_progress')
]

# Group tasks by priority
by_priority = defaultdict(list)
for task in tasks:
    by_priority[task.priority].append(task)

print("\nTasks by priority:")
for priority in ['high', 'medium', 'low']:
    if priority in by_priority:
        print(f"\n{priority.upper()}:")
        for task in by_priority[priority]:
            print(f"  - {task.name} ({task.status})")

# Count by status
status_count = Counter(task.status for task in tasks)
print(f"\nTasks by status:")
for status, count in status_count.items():
    print(f"  {status}: {count}")

# Character frequency analyzer
print("\n--- CHARACTER FREQUENCY ANALYZER ---")

def analyze_string(s):
    """Analyze character frequencies in a string."""
    char_count = Counter(s.lower())
    print(f"String: '{s}'")
    print(f"Length: {len(s)} characters")
    print(f"Unique characters: {len(char_count)}")
    print(f"\nTop 5 most common characters:")
    for char, count in char_count.most_common(5):
        if char != ' ':
            print(f"  '{char}': {count}")

analyze_string("Hello, World! This is a test.")

# Shopping cart with defaultdict
print("\n--- SHOPPING CART EXAMPLE ---")

cart = defaultdict(lambda: {'quantity': 0, 'price': 0})

def add_to_cart(item, quantity, price):
    """Add item to cart."""
    cart[item]['quantity'] += quantity
    cart[item]['price'] = price

add_to_cart('Apple', 5, 0.50)
add_to_cart('Banana', 3, 0.30)
add_to_cart('Apple', 2, 0.50)  # Add more apples

print("Shopping Cart:")
total = 0
for item, details in cart.items():
    item_total = details['quantity'] * details['price']
    total += item_total
    print(f"  {item}: {details['quantity']} x ${details['price']:.2f} = ${item_total:.2f}")
print(f"\nTotal: ${total:.2f}")
