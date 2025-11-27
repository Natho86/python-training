# Exercise 16: Word Frequency Counter - SOLUTION
# Difficulty: Beginner+
# Concepts: Dictionaries, String methods, Loops

# SOLUTION
def word_frequency(text):
    """Count frequency of each word in text."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Test with example
text = "the quick brown fox jumps over the lazy dog the fox"
freq = word_frequency(text)

# Sort by frequency (most common first)
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(f"Text: {text}\n")
print("Word frequencies:")
for word, count in sorted_freq:
    print(f"{word}: {count}")

"""
EXPLANATION:
1. We convert text to lowercase for case-insensitive counting
2. .split() breaks text into words (splits on whitespace)
3. We use a dictionary to map words to their counts
4. For each word, we check if it exists and increment, or create new entry
5. sorted() with key=lambda sorts dictionary items by value
6. reverse=True gives us descending order (highest first)

Key Concepts:
- Dictionaries map keys to values {key: value}
- Checking 'if key in dict' before accessing prevents errors
- .items() returns key-value pairs for iteration
- lambda x: x[1] is an anonymous function that returns the second element (count)
- sorted() returns a list of tuples
"""

# Alternative using .get() method
print("\n--- ALTERNATIVE SOLUTION ---")

def word_frequency_v2(text):
    """Count using .get() method."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

freq2 = word_frequency_v2(text)
print(f"\nUsing .get() method: {freq2}")

# Extension solution: Ignore stop words and handle punctuation
print("\n--- EXTENSION SOLUTION ---")
import string

def advanced_word_frequency(text, n_most_common=5):
    """Count words, ignoring stop words and punctuation."""
    # Common stop words to ignore
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                  'of', 'with', 'is', 'was', 'are', 'were', 'be', 'been', 'have', 'has'}

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    words = cleaned_text.split()
    frequency = {}

    for word in words:
        if word and word not in stop_words:  # Ignore empty strings and stop words
            frequency[word] = frequency.get(word, 0) + 1

    # Get N most common words
    most_common = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:n_most_common]

    return frequency, most_common

# Test with more complex text
complex_text = """The quick brown fox jumps over the lazy dog. The dog was sleeping,
                  but the fox was quick and clever. The fox jumped twice!"""

all_freq, top_5 = advanced_word_frequency(complex_text, 5)

print(f"\nText: {complex_text}\n")
print(f"Total unique words (excluding stop words): {len(all_freq)}")
print(f"\nTop 5 most common words:")
for word, count in top_5:
    print(f"  {word}: {count}")
