# Intermediate Projects

This folder contains comprehensive intermediate-level Python projects that combine concepts from Phase 2 and Phase 3 exercises (exercises 16-50).

## Projects Overview

### 1. Expense Tracker
**File**: `expense_tracker.py`
**Difficulty**: Intermediate
**Estimated Time**: 2-3 hours to understand and customize

**Description**:
A full-featured expense tracking application with categorization, reporting, and data persistence.

**Features**:
- Add, edit, and delete expenses
- Categorize expenses (Food, Transportation, Entertainment, etc.)
- View expenses by category
- Monthly expense reports with percentages
- Comprehensive statistics (total, average, min, max)
- Visual bar charts (text-based)
- JSON data persistence

**Key Concepts**:
- Object-Oriented Programming (Expense and ExpenseTracker classes)
- JSON serialization/deserialization
- datetime module for date handling
- collections.defaultdict for data aggregation
- List comprehensions and lambda functions
- Error handling and data validation

**How to Run**:
```bash
python3 expense_tracker.py
```

**Learning Objectives**:
- Design classes to model real-world entities
- Work with JSON for data storage
- Handle dates and time calculations
- Aggregate and analyze data
- Build menu-driven CLI applications

---

### 2. Contact Manager
**File**: `contact_manager.py`
**Difficulty**: Intermediate
**Estimated Time**: 2-3 hours to understand and customize

**Description**:
A comprehensive contact management system with full CRUD operations, search, validation, and CSV import/export.

**Features**:
- Create, Read, Update, Delete contacts
- Email and phone number validation using regex
- Search contacts by name, phone, or email
- Group contacts by category
- Export contacts to CSV
- Import contacts from CSV
- Automatic backup system
- Detailed contact information display

**Key Concepts**:
- Object-Oriented Programming (Contact and ContactManager classes)
- Regular expressions for validation
- CSV file handling (csv module)
- JSON for data persistence
- Error handling and input validation
- Static methods for utility functions

**How to Run**:
```bash
python3 contact_manager.py
```

**Learning Objectives**:
- Implement CRUD operations
- Validate user input with regex
- Work with both CSV and JSON formats
- Handle file I/O safely
- Build searchable data systems

---

### 3. Inventory Management System
**File**: `inventory_system.py`
**Difficulty**: Intermediate
**Estimated Time**: 2-3 hours to understand and customize

**Description**:
A text-based inventory system for managing products with stock tracking, alerts, and comprehensive reporting.

**Features**:
- Add, update, and delete products
- Track stock quantities with add/remove/set operations
- SKU-based product identification
- Low stock and out-of-stock alerts
- Category-based organization
- Multiple report types (low stock, category, summary)
- Top products by value analysis
- JSON data persistence

**Key Concepts**:
- Object-Oriented Programming (Product and InventorySystem classes)
- JSON for data storage
- Data validation and business logic
- collections.defaultdict for grouping
- List comprehensions and sorting with lambda
- Error handling and edge cases

**How to Run**:
```bash
python3 inventory_system.py
```

**Learning Objectives**:
- Model business entities with classes
- Implement business logic (stock alerts, value calculations)
- Create multiple types of reports
- Handle data relationships (categories, SKUs)
- Build robust data validation

---

## Learning Path

**Recommended Order**:
1. **Inventory System** - Start here for clearest OOP structure
2. **Contact Manager** - Learn CSV/JSON dual format and regex validation
3. **Expense Tracker** - Most complex reporting and data aggregation

## Common Patterns Across Projects

All three projects demonstrate these important patterns:

1. **Class-Based Design**: Each project uses classes to encapsulate data and behavior
2. **Data Persistence**: All use JSON for saving/loading data
3. **Menu-Driven Interface**: User-friendly command-line menus
4. **Input Validation**: Robust error handling and data validation
5. **CRUD Operations**: Create, Read, Update, Delete functionality
6. **Search and Filter**: Finding specific items in collections
7. **Reporting**: Generating summaries and statistics from data

## Concepts Covered

- **OOP**: Classes, methods, `__init__`, `__str__`, static methods
- **File I/O**: Reading/writing JSON and CSV files
- **Data Structures**: Dictionaries, lists, defaultdict
- **Error Handling**: try/except blocks, validation
- **Modules**: datetime, json, csv, collections, os, re
- **Functional Programming**: Lambda functions, list comprehensions
- **Data Processing**: Sorting, filtering, aggregating

## Extension Ideas

### For All Projects:
1. Add a graphical user interface (GUI) using tkinter
2. Add database support (SQLite) instead of JSON
3. Implement user authentication and multiple user support
4. Add data export to Excel format
5. Create unit tests for key functionality
6. Add logging for debugging and audit trails
7. Implement undo/redo functionality
8. Add data visualization with matplotlib

### Expense Tracker Specific:
- Budget limits and overspending alerts
- Recurring expenses support
- Multi-currency support
- Receipt image attachments
- Bank statement import

### Contact Manager Specific:
- Birthday reminders
- Email integration (send emails to contacts)
- Contact groups/tags
- Duplicate detection and merging
- vCard import/export

### Inventory System Specific:
- Barcode support
- Supplier management
- Purchase order system
- Price history tracking
- Reorder point automation

## Tips for Success

1. **Read the Code**: Start by reading through the entire program to understand structure
2. **Run It First**: Execute the program and try all features before modifying
3. **Small Changes**: Make small modifications and test frequently
4. **Add Features**: Pick one extension idea and implement it
5. **Debug**: Use print statements to understand data flow
6. **Comment**: Add comments explaining what you learn
7. **Experiment**: Try breaking things to understand error handling

## Getting Help

If you get stuck:
1. Read the docstrings - every function has one
2. Print variable values to see what's happening
3. Check the error messages carefully
4. Review the exercises that cover the concepts used
5. Try commenting out sections to isolate problems

## Next Steps

After completing these projects, you're ready for:
- Web development with Flask or Django
- Data analysis with pandas
- API development
- Database programming
- More advanced OOP patterns
- Testing and debugging techniques

Happy coding! 🐍
