# Exercise 22: String Methods Explorer - SOLUTION
# Difficulty: Beginner+
# Concepts: String methods, String manipulation, Text processing

# SOLUTION
print("STRING METHODS DEMONSTRATION")
print("=" * 60)

# Test string
text = "  Hello, World! Welcome to Python.  "
print(f"Original: '{text}'")
print()

# 1. CASE CONVERSION
print("1. CASE CONVERSION")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Swap case: '{text.swapcase()}'")
print()

# 2. STRING TRIMMING
print("2. STRING TRIMMING")
print(f"Strip (both ends): '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")
print()

# 3. STRING TESTING
print("3. STRING TESTING")
test_strings = ["Hello", "Hello123", "12345", "hello world", ""]

for s in test_strings:
    print(f"\nTesting: '{s}'")
    print(f"  isalpha: {s.isalpha()}")      # Only letters
    print(f"  isdigit: {s.isdigit()}")      # Only digits
    print(f"  isalnum: {s.isalnum()}")      # Letters or digits
    print(f"  isspace: {s.isspace()}")      # Only whitespace
    print(f"  islower: {s.islower()}")      # All lowercase
    print(f"  isupper: {s.isupper()}")      # All uppercase

print()

# 4. SEARCHING AND FINDING
print("4. SEARCHING AND FINDING")
sentence = "Python is powerful. Python is easy. Python is fun."
print(f"Sentence: {sentence}")
print(f"Find 'Python': {sentence.find('Python')}")  # First occurrence index
print(f"Find 'Java': {sentence.find('Java')}")      # Returns -1 if not found
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'fun.': {sentence.endswith('fun.')}")
print()

# 5. STRING REPLACING
print("5. STRING REPLACING")
print(f"Replace 'Python' with 'Programming': {sentence.replace('Python', 'Programming')}")
print(f"Replace first 2 occurrences: {sentence.replace('Python', 'Coding', 2)}")
print()

# 6. SPLITTING AND JOINING
print("6. SPLITTING AND JOINING")
words = text.strip().split()  # Split on whitespace
print(f"Words: {words}")
print(f"Word count: {len(words)}")

csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(',')
print(f"\nCSV data: {csv_data}")
print(f"Split on comma: {fruits}")

# Join list into string
joined = " | ".join(fruits)
print(f"Joined with ' | ': {joined}")
print()

# 7. PADDING AND ALIGNMENT
print("7. PADDING AND ALIGNMENT")
word = "Python"
print(f"Center (20): '{word.center(20)}'")
print(f"Left justify (20): '{word.ljust(20)}'")
print(f"Right justify (20): '{word.rjust(20)}'")
print(f"Zero padding: '{word.zfill(10)}'")

"""
EXPLANATION:
1. String methods return new strings; original strings are unchanged
2. Case conversion methods: .upper(), .lower(), .title(), .capitalize()
3. Testing methods return True/False: .isalpha(), .isdigit(), etc.
4. .find() returns index or -1, .count() returns number of occurrences
5. .split() creates a list from string, .join() creates string from list
6. .strip() removes whitespace, .replace() substitutes substrings

Key Concepts:
- Strings are immutable (methods return new strings)
- Many methods for validation (is* methods)
- Split and join are inverses of each other
- Methods can be chained: text.strip().lower().split()
"""

# Advanced string methods
print("\n--- ADVANCED STRING METHODS ---")

# Partition and rpartition
email = "user@example.com"
username, sep, domain = email.partition('@')
print(f"\nEmail: {email}")
print(f"Partition on '@': username={username}, separator={sep}, domain={domain}")

# Remove prefix/suffix (Python 3.9+)
filename = "document.pdf"
if filename.endswith('.pdf'):
    name_without_ext = filename[:-4]  # Remove last 4 characters
    print(f"\nFilename: {filename}")
    print(f"Without extension: {name_without_ext}")

# Expandtabs
tabbed = "Name\tAge\tCity"
print(f"\nWith tabs: '{tabbed}'")
print(f"Expanded: '{tabbed.expandtabs(15)}'")

# Extension solution: Text analyzer
print("\n--- EXTENSION SOLUTION: TEXT ANALYZER ---")

def analyze_text(text):
    """
    Comprehensive text analysis.

    Returns:
        dict: Statistics about the text
    """
    # Clean and prepare text
    cleaned = text.strip()

    # Count words
    words = cleaned.split()
    word_count = len(words)

    # Count sentences (simple: by periods, question marks, exclamation marks)
    sentence_endings = cleaned.count('.') + cleaned.count('?') + cleaned.count('!')
    sentence_count = max(sentence_endings, 1)  # At least 1 sentence

    # Calculate average word length
    if word_count > 0:
        total_chars = sum(len(word.strip('.,!?;:')) for word in words)
        avg_word_length = total_chars / word_count
    else:
        avg_word_length = 0

    # Count characters (excluding spaces)
    char_count = len(cleaned.replace(' ', ''))

    # Find longest and shortest words
    clean_words = [word.strip('.,!?;:') for word in words]
    longest_word = max(clean_words, key=len) if clean_words else ""
    shortest_word = min(clean_words, key=len) if clean_words else ""

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'char_count': char_count,
        'avg_word_length': avg_word_length,
        'longest_word': longest_word,
        'shortest_word': shortest_word
    }

# Test text analyzer
sample_text = """
Python is a high-level programming language. It emphasizes code readability
and simplicity. Python is widely used in web development, data science, and
automation. Learning Python is fun and rewarding!
"""

stats = analyze_text(sample_text)

print("\nText Analysis Results:")
print("-" * 50)
print(f"Words: {stats['word_count']}")
print(f"Sentences: {stats['sentence_count']}")
print(f"Characters: {stats['char_count']}")
print(f"Average word length: {stats['avg_word_length']:.1f}")
print(f"Longest word: {stats['longest_word']} ({len(stats['longest_word'])} chars)")
print(f"Shortest word: {stats['shortest_word']} ({len(stats['shortest_word'])} chars)")

# Text formatter
print("\n--- TEXT FORMATTER ---")

def format_text(text):
    """
    Format text by normalizing whitespace and capitalizing sentences.
    """
    # Normalize whitespace
    text = ' '.join(text.split())

    # Split into sentences (simple approach)
    sentences = []
    current_sentence = []

    for word in text.split():
        current_sentence.append(word)
        # Check if word ends with sentence terminator
        if word.endswith(('.', '!', '?')):
            sentences.append(' '.join(current_sentence))
            current_sentence = []

    # Add remaining words as a sentence
    if current_sentence:
        sentences.append(' '.join(current_sentence))

    # Capitalize first letter of each sentence
    formatted_sentences = [s[0].upper() + s[1:] if s else s for s in sentences]

    return ' '.join(formatted_sentences)

# Test formatter
messy_text = "   hello world.    this   is  python.   programming is   fun!  "
formatted = format_text(messy_text)
print(f"\nOriginal: '{messy_text}'")
print(f"Formatted: '{formatted}'")

# Practical example: Input validation
print("\n--- PRACTICAL EXAMPLE: INPUT VALIDATION ---")

def validate_username(username):
    """Validate username according to rules."""
    errors = []

    if len(username) < 3:
        errors.append("Username must be at least 3 characters")
    if len(username) > 20:
        errors.append("Username must be at most 20 characters")
    if not username.isalnum():
        errors.append("Username must contain only letters and numbers")
    if username[0].isdigit():
        errors.append("Username cannot start with a number")

    return len(errors) == 0, errors

def validate_email(email):
    """Simple email validation."""
    errors = []

    if '@' not in email:
        errors.append("Email must contain @")
    elif email.count('@') > 1:
        errors.append("Email must contain exactly one @")
    elif not email.endswith(('.com', '.org', '.net', '.edu')):
        errors.append("Email must end with common domain")

    return len(errors) == 0, errors

# Test validation
test_usernames = ["alice123", "ab", "user@name", "123user", "validusername"]
print("\nUsername Validation:")
for username in test_usernames:
    valid, errors = validate_username(username)
    status = "Valid" if valid else f"Invalid: {', '.join(errors)}"
    print(f"  {username:15} -> {status}")

test_emails = ["user@example.com", "invalid", "two@@example.com", "user@test.xyz"]
print("\nEmail Validation:")
for email in test_emails:
    valid, errors = validate_email(email)
    status = "Valid" if valid else f"Invalid: {', '.join(errors)}"
    print(f"  {email:20} -> {status}")
