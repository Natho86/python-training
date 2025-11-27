# Exercise 47: Todo List Application with CLI
# Difficulty: Intermediate
# Concepts: Classes, JSON persistence, User input, DateTime, File I/O

"""
PROBLEM:
Create a command-line Todo List application with:
1. Add tasks with description, priority (high/medium/low), and due date
2. List all tasks (with filtering by priority or status)
3. Mark tasks as complete
4. Delete tasks
5. Save/load tasks from JSON file automatically
6. Show tasks due today or overdue

Features:
- Tasks have: id, description, priority, due_date, completed, created_date
- Interactive menu system
- Data persists between sessions
- Display tasks in formatted table

EXAMPLE INTERACTION:
=== Todo List Manager ===
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Choice: 1
Description: Finish Python project
Priority (high/medium/low): high
Due date (YYYY-MM-DD): 2024-12-01
Task added!

HINTS:
1. Create a Task class or use dictionaries
2. Use a TodoManager class to handle the task list
3. Save to JSON after every modification
4. Load from JSON when starting
5. Use datetime for date handling and comparisons

EXTENSION:
Add categories/tags for tasks, search functionality, and ability to edit existing tasks.
Add statistics showing completion rate and productivity trends.
"""

# Write your solution here
