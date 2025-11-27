# Exercise 24: File Reading and Writing - SOLUTION
# Difficulty: Intermediate-
# Concepts: File I/O, Context managers, File modes

# SOLUTION
import os
from datetime import datetime

print("FILE OPERATIONS DEMONSTRATION")
print("=" * 60)

# Create a temporary directory for our examples
if not os.path.exists('temp_files'):
    os.makedirs('temp_files')

# 1. WRITING TO A FILE
print("1. WRITING TO A FILE")
print("-" * 60)

filename = 'temp_files/example.txt'

# Using 'w' mode (write - creates new or overwrites existing)
with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python is great!\n")
    file.write("File I/O is important.\n")

print(f"Created and wrote to: {filename}")

# Writing multiple lines at once
lines = [
    "Line 1: Introduction\n",
    "Line 2: Body\n",
    "Line 3: Conclusion\n"
]

with open('temp_files/multiple_lines.txt', 'w') as file:
    file.writelines(lines)

print("Wrote multiple lines to: temp_files/multiple_lines.txt")
print()

# 2. READING ENTIRE FILE
print("2. READING ENTIRE FILE")
print("-" * 60)

with open(filename, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# 3. READING LINE BY LINE
print("3. READING LINE BY LINE")
print("-" * 60)

with open(filename, 'r') as file:
    line_num = 1
    for line in file:
        print(f"Line {line_num}: {line.strip()}")  # .strip() removes \n
        line_num += 1
print()

# 4. READING ALL LINES AS LIST
print("4. READING ALL LINES AS LIST")
print("-" * 60)

with open(filename, 'r') as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"Lines as list: {lines}")
print()

# 5. APPENDING TO FILE
print("5. APPENDING TO FILE")
print("-" * 60)

# Using 'a' mode (append - adds to end without overwriting)
with open(filename, 'a') as file:
    file.write("This line was appended.\n")
    file.write("So was this one!\n")

print("Appended new lines to file")

# Read and display updated content
with open(filename, 'r') as file:
    print("\nUpdated file content:")
    print(file.read())

"""
EXPLANATION:
1. open() function takes filename and mode ('r', 'w', 'a', etc.)
2. 'with' statement ensures file is automatically closed
3. 'w' mode creates new file or overwrites existing
4. 'a' mode appends to end of existing file
5. 'r' mode opens for reading (default mode)
6. .read() returns entire file as string
7. .readline() reads one line at a time
8. .readlines() returns list of all lines
9. Iterating over file object reads line by line (memory efficient)

Key Concepts:
- Always use 'with' statement (context manager)
- Files must be closed after use (with handles this automatically)
- Different modes for different operations
- .strip() is useful to remove newline characters
"""

# File modes comparison
print("\n--- FILE MODES EXPLAINED ---")
print("""
Common file modes:
- 'r'  : Read (default) - file must exist
- 'w'  : Write - creates new or overwrites existing
- 'a'  : Append - adds to end, creates if doesn't exist
- 'r+' : Read and write - file must exist
- 'w+' : Write and read - creates new or overwrites
- 'a+' : Append and read - creates if doesn't exist

Binary modes (add 'b'):
- 'rb' : Read binary
- 'wb' : Write binary
- 'ab' : Append binary
""")

# Extension solution: Log file system
print("\n--- EXTENSION SOLUTION: LOG FILE SYSTEM ---")

class SimpleLogger:
    """A simple logging system that writes timestamped entries."""

    def __init__(self, log_file='temp_files/application.log'):
        self.log_file = log_file

    def log(self, message, level='INFO'):
        """Add a log entry with timestamp."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, 'a') as file:
            file.write(log_entry)

    def read_logs(self):
        """Read and return all log entries."""
        try:
            with open(self.log_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "No log file found."

    def get_recent_logs(self, n=10):
        """Get the last N log entries."""
        try:
            with open(self.log_file, 'r') as file:
                lines = file.readlines()
                return ''.join(lines[-n:])
        except FileNotFoundError:
            return "No log file found."

# Test the logger
logger = SimpleLogger()
logger.log("Application started")
logger.log("User logged in", level='INFO')
logger.log("Processing data...", level='INFO')
logger.log("Connection timeout", level='WARNING')
logger.log("Critical error occurred", level='ERROR')

print("Log entries created. Recent logs:")
print(logger.get_recent_logs(5))

# Word counter function
print("\n--- WORD COUNTER ---")

def count_word_in_file(filename, word):
    """Count occurrences of a word in a file."""
    try:
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                count += line.lower().count(word.lower())
        return count
    except FileNotFoundError:
        return -1

# Create a test file
with open('temp_files/test_count.txt', 'w') as f:
    f.write("Python is great. Python is powerful.\n")
    f.write("I love Python. Python makes coding fun.\n")

word_to_count = 'python'
occurrences = count_word_in_file('temp_files/test_count.txt', word_to_count)
print(f"\nThe word '{word_to_count}' appears {occurrences} times")

# File statistics
print("\n--- FILE STATISTICS ---")

def get_file_stats(filename):
    """Get statistics about a text file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()

            return {
                'lines': len([l for l in lines if l.strip()]),  # Non-empty lines
                'words': len(words),
                'characters': len(content),
                'characters_no_spaces': len(content.replace(' ', '').replace('\n', ''))
            }
    except FileNotFoundError:
        return None

stats = get_file_stats('temp_files/example.txt')
if stats:
    print(f"\nFile statistics for example.txt:")
    print(f"  Lines: {stats['lines']}")
    print(f"  Words: {stats['words']}")
    print(f"  Characters (with spaces): {stats['characters']}")
    print(f"  Characters (without spaces): {stats['characters_no_spaces']}")

# Error handling examples
print("\n--- ERROR HANDLING ---")

def safe_read_file(filename):
    """Safely read a file with error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except PermissionError:
        return f"Error: No permission to read '{filename}'."
    except Exception as e:
        return f"Error: {str(e)}"

# Test with existing and non-existing files
print("\nReading existing file:")
print(safe_read_file('temp_files/example.txt')[:50] + "...")

print("\nReading non-existing file:")
print(safe_read_file('nonexistent.txt'))

# File operations best practices
print("\n--- BEST PRACTICES ---")

def copy_file(source, destination):
    """Copy file contents from source to destination."""
    try:
        with open(source, 'r') as src:
            with open(destination, 'w') as dst:
                # Copy in chunks for large files
                chunk_size = 1024
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break
                    dst.write(chunk)
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False

# Test file copy
copy_file('temp_files/example.txt', 'temp_files/example_copy.txt')
print("File copied successfully")

# Reading specific lines
print("\n--- READING SPECIFIC LINES ---")

def read_line_number(filename, line_num):
    """Read a specific line from a file (1-indexed)."""
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                if i == line_num:
                    return line.strip()
        return f"Line {line_num} not found (file has fewer lines)"
    except FileNotFoundError:
        return "File not found"

print(f"Line 2 of example.txt: {read_line_number('temp_files/example.txt', 2)}")

# File existence check
print("\n--- FILE OPERATIONS ---")

def file_exists(filename):
    """Check if a file exists."""
    return os.path.exists(filename)

def get_file_size(filename):
    """Get file size in bytes."""
    try:
        return os.path.getsize(filename)
    except OSError:
        return -1

print(f"example.txt exists: {file_exists('temp_files/example.txt')}")
print(f"example.txt size: {get_file_size('temp_files/example.txt')} bytes")

# Cleanup note
print("\n" + "=" * 60)
print("NOTE: Created files are in 'temp_files/' directory")
print("You can delete this directory when done practicing")
print("=" * 60)
