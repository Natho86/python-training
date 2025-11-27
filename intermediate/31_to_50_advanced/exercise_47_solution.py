# Exercise 47: Todo List Application with CLI - SOLUTION
# Difficulty: Intermediate
# Concepts: Classes, JSON persistence, User input, DateTime, File I/O

import json
from datetime import datetime, timedelta

# SOLUTION
class Task:
    """Represents a single task."""

    def __init__(self, description, priority="medium", due_date=None, task_id=None):
        """
        Initialize task.

        Args:
            description: Task description
            priority: high, medium, or low
            due_date: Due date string (YYYY-MM-DD)
            task_id: Unique task ID
        """
        self.id = task_id
        self.description = description
        self.priority = priority.lower()
        self.due_date = due_date
        self.completed = False
        self.created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        """Convert task to dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed,
            'created_date': self.created_date
        }

    def is_overdue(self):
        """Check if task is overdue."""
        if not self.due_date or self.completed:
            return False
        due = datetime.strptime(self.due_date, '%Y-%m-%d')
        return due.date() < datetime.now().date()

    def is_due_today(self):
        """Check if task is due today."""
        if not self.due_date or self.completed:
            return False
        due = datetime.strptime(self.due_date, '%Y-%m-%d')
        return due.date() == datetime.now().date()

    def __str__(self):
        """String representation."""
        status = "✓" if self.completed else " "
        priority_symbol = {"high": "!", "medium": "-", "low": "·"}[self.priority]
        due = f"Due: {self.due_date}" if self.due_date else "No due date"

        overdue = ""
        if self.is_overdue():
            overdue = " [OVERDUE]"
        elif self.is_due_today():
            overdue = " [DUE TODAY]"

        return f"[{status}] {priority_symbol} {self.id}. {self.description} ({due}){overdue}"

class TodoManager:
    """Manage todo list with persistence."""

    def __init__(self, filename="todos.json"):
        """
        Initialize todo manager.

        Args:
            filename: JSON file for persistence
        """
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file."""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for task_data in data:
                    task = Task(
                        description=task_data['description'],
                        priority=task_data['priority'],
                        due_date=task_data.get('due_date'),
                        task_id=task_data['id']
                    )
                    task.completed = task_data['completed']
                    task.created_date = task_data['created_date']
                    self.tasks.append(task)

                # Set next_id to one more than highest existing id
                if self.tasks:
                    self.next_id = max(t.id for t in self.tasks) + 1

                print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
        except FileNotFoundError:
            print(f"No existing todo file found. Starting fresh.")

    def save_tasks(self):
        """Save tasks to JSON file."""
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def add_task(self, description, priority="medium", due_date=None):
        """
        Add a new task.

        Args:
            description: Task description
            priority: Task priority
            due_date: Due date (YYYY-MM-DD)
        """
        task = Task(description, priority, due_date, self.next_id)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"✓ Task added: {description}")

    def get_task(self, task_id):
        """Find task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark task as complete."""
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.save_tasks()
            print(f"✓ Task {task_id} marked as complete!")
            return True
        print(f"Task {task_id} not found.")
        return False

    def delete_task(self, task_id):
        """Delete a task."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"✓ Task {task_id} deleted.")
            return True
        print(f"Task {task_id} not found.")
        return False

    def list_tasks(self, filter_by=None, show_completed=True):
        """
        List tasks with optional filtering.

        Args:
            filter_by: 'high', 'medium', 'low', 'today', 'overdue', or None
            show_completed: Whether to show completed tasks
        """
        filtered_tasks = self.tasks

        # Filter by completion status
        if not show_completed:
            filtered_tasks = [t for t in filtered_tasks if not t.completed]

        # Filter by priority
        if filter_by in ['high', 'medium', 'low']:
            filtered_tasks = [t for t in filtered_tasks if t.priority == filter_by]

        # Filter by due date
        elif filter_by == 'today':
            filtered_tasks = [t for t in filtered_tasks if t.is_due_today()]
        elif filter_by == 'overdue':
            filtered_tasks = [t for t in filtered_tasks if t.is_overdue()]

        if not filtered_tasks:
            print("No tasks found.")
            return

        print(f"\n{'='*70}")
        print("TODO LIST")
        print(f"{'='*70}")

        # Group by priority
        for priority in ['high', 'medium', 'low']:
            priority_tasks = [t for t in filtered_tasks if t.priority == priority]
            if priority_tasks:
                print(f"\n{priority.upper()} PRIORITY:")
                for task in priority_tasks:
                    print(f"  {task}")

        print(f"{'='*70}\n")

    def get_statistics(self):
        """Get todo list statistics."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        incomplete = total - completed
        overdue = sum(1 for t in self.tasks if t.is_overdue())
        due_today = sum(1 for t in self.tasks if t.is_due_today())

        return {
            'total': total,
            'completed': completed,
            'incomplete': incomplete,
            'overdue': overdue,
            'due_today': due_today,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }

def main():
    """Main application loop."""
    manager = TodoManager()

    while True:
        print("\n" + "="*50)
        print("TODO LIST MANAGER")
        print("="*50)

        # Show quick stats
        stats = manager.get_statistics()
        print(f"Tasks: {stats['incomplete']} pending, {stats['completed']} completed")
        if stats['overdue'] > 0:
            print(f"⚠️  {stats['overdue']} overdue tasks!")
        if stats['due_today'] > 0:
            print(f"📅 {stats['due_today']} tasks due today!")

        print("\nOptions:")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View by priority")
        print("5. Complete task")
        print("6. Delete task")
        print("7. Statistics")
        print("8. Exit")

        choice = input("\nChoice: ").strip()

        if choice == '1':
            # Add task
            description = input("Description: ").strip()
            if not description:
                print("Description cannot be empty.")
                continue

            priority = input("Priority (high/medium/low) [medium]: ").strip().lower() or "medium"
            if priority not in ['high', 'medium', 'low']:
                print("Invalid priority. Using 'medium'.")
                priority = "medium"

            due_date = input("Due date (YYYY-MM-DD) [optional]: ").strip()
            if due_date:
                try:
                    datetime.strptime(due_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Task added without due date.")
                    due_date = None

            manager.add_task(description, priority, due_date)

        elif choice == '2':
            # View all tasks
            manager.list_tasks()

        elif choice == '3':
            # View pending tasks
            manager.list_tasks(show_completed=False)

        elif choice == '4':
            # View by priority
            priority = input("Priority (high/medium/low): ").strip().lower()
            manager.list_tasks(filter_by=priority)

        elif choice == '5':
            # Complete task
            manager.list_tasks(show_completed=False)
            try:
                task_id = int(input("Task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Invalid task ID.")

        elif choice == '6':
            # Delete task
            manager.list_tasks()
            try:
                task_id = int(input("Task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")

        elif choice == '7':
            # Statistics
            stats = manager.get_statistics()
            print(f"\n{'='*50}")
            print("STATISTICS")
            print(f"{'='*50}")
            print(f"Total tasks: {stats['total']}")
            print(f"Completed: {stats['completed']}")
            print(f"Incomplete: {stats['incomplete']}")
            print(f"Overdue: {stats['overdue']}")
            print(f"Due today: {stats['due_today']}")
            print(f"Completion rate: {stats['completion_rate']:.1f}%")
            print(f"{'='*50}")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

"""
EXPLANATION:
1. Task class represents individual tasks with all attributes
2. TodoManager handles the collection and persistence
3. JSON saves/loads task data automatically
4. datetime module handles date comparisons
5. Menu system provides interactive interface
6. Tasks are identified by unique IDs
7. Filtering allows viewing subsets of tasks

Key Concepts:
- Class-based organization separates concerns
- JSON provides simple data persistence
- datetime enables date-based features
- User input validation prevents errors
- Statistics provide overview of task status
- Auto-save ensures data is never lost
"""

# Run the application
if __name__ == "__main__":
    # Create some sample tasks for demonstration
    print("Creating sample tasks for demonstration...\n")
    demo_manager = TodoManager("demo_todos.json")

    if len(demo_manager.tasks) == 0:
        demo_manager.add_task("Complete Python exercises", "high",
                            datetime.now().strftime('%Y-%m-%d'))
        demo_manager.add_task("Review OOP concepts", "medium",
                            (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'))
        demo_manager.add_task("Build portfolio project", "high",
                            (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'))
        demo_manager.add_task("Read documentation", "low")

    # Show initial state
    demo_manager.list_tasks()

    # Show statistics
    stats = demo_manager.get_statistics()
    print(f"Completion rate: {stats['completion_rate']:.1f}%")

    print("\n\nTo run interactive mode, uncomment the line below:")
    print("# main()")
