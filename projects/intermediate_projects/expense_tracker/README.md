# Expense Tracker

A comprehensive command-line application for tracking and managing personal expenses with data persistence, reporting, and analytics.

## Overview

The Expense Tracker allows users to manage their expenses with features like categorization, tagging, date filtering, statistics, and CSV export capabilities. All data is persisted in JSON format for easy backup and portability.

## Features

### Core Functionality
- **Add Expenses**: Record expenses with amount, category, description, date, and tags
- **View Expenses**: Display all expenses or filter by various criteria
- **Update Expenses**: Modify existing expense details
- **Delete Expenses**: Remove unwanted expenses with confirmation
- **Search**: Find expenses by keyword in description, category, or tags

### Filtering & Reporting
- **Category Filter**: View expenses by specific categories
- **Date Range Filter**: Filter expenses within a date range
- **Statistics**: View comprehensive statistics including:
  - Total amount and count
  - Average expense amount
  - Breakdown by category with percentages
  - Visual text-based bar charts

### Data Management
- **JSON Persistence**: Automatic saving and loading of data
- **CSV Export**: Export filtered expenses to CSV format
- **Data Validation**: Input validation for amounts, dates, and other fields

## Project Structure

```
expense_tracker/
├── expense.py           # Expense class definition
├── expense_manager.py   # ExpenseManager class for data operations
├── main.py             # Main application with CLI interface
├── expenses.json       # Data file (created automatically)
└── README.md          # This file
```

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation & Usage

1. Navigate to the project directory:
   ```bash
   cd /home/nath/claude/python-training/projects/intermediate_projects/expense_tracker
   ```

2. Run the application:
   ```bash
   python main.py
   ```
   or
   ```bash
   chmod +x main.py
   ./main.py
   ```

## How to Use

### Adding an Expense

1. Select option 1 from the main menu
2. Enter the amount (e.g., 45.50)
3. Enter a category (e.g., Food, Transport, Entertainment)
4. Optionally add a description
5. Enter a date in YYYY-MM-DD format or press Enter for today
6. Optionally add comma-separated tags

Example:
```
Amount: $45.50
Category: Food
Description: Lunch at restaurant
Date (YYYY-MM-DD, press Enter for today): 2025-11-27
Tags (comma-separated, optional): restaurant, lunch
```

### Viewing Expenses

- **All Expenses**: Option 2 shows all recorded expenses
- **By Category**: Option 3 filters by a specific category
- **By Date Range**: Option 4 shows expenses within a date range

### Updating an Expense

1. Select option 5
2. Enter the expense ID (shown when viewing expenses as #ID)
3. Enter new values for fields you want to update
4. Press Enter to keep current values unchanged

### Viewing Statistics

Select option 7 to view comprehensive statistics including:
- Total number of expenses
- Total amount spent
- Average expense amount
- Breakdown by category with percentages and visual bars

### Exporting to CSV

1. Select option 8
2. Enter a filename (e.g., expenses.csv)
3. Optionally filter by date range
4. File will be created in the current directory

## Code Structure & Concepts

### Object-Oriented Programming (OOP)
- **Expense Class**: Represents a single expense with validation
- **ExpenseManager Class**: Manages collections of expenses
- **ExpenseTrackerApp Class**: Handles user interface and application flow

### Key Python Concepts Used

1. **Classes and Objects**
   - Custom classes with `__init__`, `__str__`, `__repr__`
   - Class methods (`@classmethod`) for factory pattern
   - Instance methods and properties

2. **File I/O**
   - JSON reading and writing
   - CSV export functionality
   - Error handling for file operations

3. **Data Structures**
   - Lists for storing expenses
   - Dictionaries for configuration and data transfer
   - Sets for unique collections (categories, tags)
   - defaultdict for statistics calculation

4. **Error Handling**
   - Try-except blocks for input validation
   - Custom error messages
   - ValueError for validation errors
   - IOError for file operation errors

5. **Datetime Module**
   - Date validation and formatting
   - Date comparison for filtering
   - Current date retrieval

6. **List Comprehensions**
   - Filtering expenses: `[e for e in expenses if condition]`
   - Data transformation and mapping

7. **Type Hints**
   - Function parameter and return type annotations
   - Improved code documentation and IDE support

8. **String Formatting**
   - f-strings for formatted output
   - Alignment and padding for tables

9. **Lambda Functions**
   - Sorting with custom keys
   - Filtering operations

10. **Collections Module**
    - defaultdict for category totals

## Data Persistence

### JSON Format
Expenses are stored in `expenses.json` with the following structure:
```json
{
  "next_id": 5,
  "expenses": [
    {
      "id": 1,
      "amount": 45.50,
      "category": "Food",
      "description": "Lunch at restaurant",
      "date": "2025-11-27",
      "tags": ["restaurant", "lunch"]
    }
  ]
}
```

### CSV Export Format
Exported CSV files contain the following columns:
- id
- date
- category
- amount
- description
- tags (semicolon-separated)

## Learning Objectives

This project demonstrates:

1. **Object-Oriented Design**: Creating well-structured classes with clear responsibilities
2. **Data Persistence**: Reading and writing JSON files with error handling
3. **Input Validation**: Validating user input and providing helpful error messages
4. **Data Filtering**: Implementing flexible filtering with multiple criteria
5. **Statistics Calculation**: Computing aggregates and percentages
6. **User Interface**: Creating an intuitive command-line interface
7. **Code Organization**: Separating concerns across multiple modules
8. **Documentation**: Using docstrings and type hints
9. **Error Handling**: Graceful error recovery and user feedback
10. **Data Export**: Converting data to different formats (CSV)

## Exercises & Extensions

Try these enhancements to practice more:

1. **Budget Tracking**: Add monthly budget limits with warnings
2. **Recurring Expenses**: Support for recurring expenses
3. **Multiple Currencies**: Currency conversion support
4. **Data Backup**: Automatic backup creation
5. **Import from CSV**: Add CSV import functionality
6. **Advanced Visualizations**: Add more chart types
7. **Expense Templates**: Create templates for common expenses
8. **Multi-user Support**: Add user accounts and authentication
9. **Database Integration**: Replace JSON with SQLite
10. **Web Interface**: Create a web-based frontend

## Testing

Test the application with these scenarios:

1. Add expenses with various categories and dates
2. Try invalid inputs (negative amounts, invalid dates)
3. Filter by different criteria
4. Update and delete expenses
5. Export to CSV and verify the output
6. Restart the application to verify data persistence
7. Test edge cases (empty data, date ranges with no expenses)

## Error Handling

The application handles various errors gracefully:
- Invalid amounts (negative or non-numeric)
- Invalid date formats
- Non-existent expense IDs
- File I/O errors
- JSON parsing errors
- User interrupts (Ctrl+C)

## Tips

- Use descriptive categories for better reporting
- Add tags for more flexible filtering
- Regularly export data to CSV for backup
- Use date ranges to analyze spending patterns
- Check statistics regularly to track spending habits

## License

This project is created for educational purposes as part of the Python Training program.
