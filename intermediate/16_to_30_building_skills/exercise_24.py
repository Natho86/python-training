# Exercise 24: File Reading and Writing
# Difficulty: Intermediate-
# Concepts: File I/O, Context managers, File modes

"""
PROBLEM:
Create a program that demonstrates file operations:
1. Write text to a file
2. Read the entire file content
3. Read file line by line
4. Append text to an existing file
5. Use context managers (with statement) for automatic file closing

EXAMPLE:
Write to file:
  - Create "output.txt"
  - Write: "Hello, World!\nPython is great!"

Read from file:
  - Read entire content
  - Read line by line
  - Count lines and words

HINTS:
1. Use open() with modes: 'r' (read), 'w' (write), 'a' (append)
2. Always use 'with' statement to ensure files are closed
3. .read() reads entire file, .readline() reads one line
4. .readlines() returns a list of all lines
5. Use 'w' mode to create/overwrite, 'a' mode to append

EXTENSION:
Create a simple log file system that appends timestamped entries.
Build a function that counts specific words in a file.
Implement error handling for missing files.
"""

# Write your solution here
