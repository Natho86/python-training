# Exercise 10: Shopping List Manager - SOLUTION
# Difficulty: Beginner
# Concepts: Lists, List methods (append, remove), While loops, Control flow

# SOLUTION
def shopping_list_manager():
    """Simple shopping list manager."""
    shopping_list = []

    while True:
        print("\n=== Shopping List Manager ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Clear list")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the list.")

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':
            if shopping_list:
                print("\nShopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")

        elif choice == '4':
            shopping_list.clear()
            print("Shopping list cleared.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

# Run the program
shopping_list_manager()

"""
EXPLANATION:
1. We create an empty list to store items
2. We use while True for an infinite menu loop
3. We use if/elif to handle different menu choices
4. .append() adds an item to the end of the list
5. We check if an item is in the list before removing it
6. .remove() removes the first occurrence of an item
7. enumerate() gives us both index and value when looping
8. .clear() removes all items from the list
9. break exits the while loop when user chooses to exit

Key Concepts:
- Lists are mutable (can be changed after creation)
- .append(item) adds to the end of a list
- .remove(item) removes first occurrence of an item
- 'item in list' checks if an item exists in the list
- enumerate(list, start) provides index and value
- .clear() empties a list
"""

# Extension solution: Mark purchased and file persistence
print("\n--- EXTENSION SOLUTION ---")

def advanced_shopping_list():
    """Shopping list with purchase tracking and file persistence."""
    shopping_list = {}  # Dictionary: {item: is_purchased}

    def save_to_file():
        """Save shopping list to file."""
        with open('shopping_list.txt', 'w') as f:
            for item, purchased in shopping_list.items():
                status = "PURCHASED" if purchased else "PENDING"
                f.write(f"{item}|{status}\n")
        print("List saved to shopping_list.txt")

    def load_from_file():
        """Load shopping list from file."""
        try:
            with open('shopping_list.txt', 'r') as f:
                for line in f:
                    item, status = line.strip().split('|')
                    shopping_list[item] = (status == "PURCHASED")
            print("List loaded from shopping_list.txt")
        except FileNotFoundError:
            print("No saved list found.")

    while True:
        print("\n=== Advanced Shopping List ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. Mark as purchased")
        print("4. View list")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list[item] = False  # Not purchased yet
            print(f"Added '{item}' to the list.")

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                del shopping_list[item]
                print(f"Removed '{item}' from the list.")
            else:
                print(f"'{item}' not found.")

        elif choice == '3':
            item = input("Enter item to mark as purchased: ")
            if item in shopping_list:
                shopping_list[item] = True
                print(f"Marked '{item}' as purchased.")
            else:
                print(f"'{item}' not found.")

        elif choice == '4':
            if shopping_list:
                print("\nShopping List:")
                for item, purchased in shopping_list.items():
                    status = "✓" if purchased else " "
                    print(f"[{status}] {item}")
            else:
                print("Shopping list is empty.")

        elif choice == '5':
            save_to_file()

        elif choice == '6':
            load_from_file()

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

advanced_shopping_list()
