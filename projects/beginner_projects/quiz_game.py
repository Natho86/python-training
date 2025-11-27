"""
Simple Quiz Game
================
An interactive multiple-choice quiz game with different categories,
immediate feedback, and score tracking.

Concepts Used:
- Lists and dictionaries (data structures)
- Loops (for, while)
- Functions
- Control flow (if/elif/else)
- String methods and formatting
- List indexing
- Dictionary access
"""


def create_quiz_questions():
    """
    Create and return quiz questions organized by category.

    Returns:
        dict: Dictionary with categories as keys and question lists as values
    """
    quizzes = {
        "Python Basics": [
            {
                "question": "What is the correct way to create a variable in Python?",
                "options": [
                    "int x = 5",
                    "x = 5",
                    "var x = 5",
                    "dim x = 5"
                ],
                "answer": 1,  # Index of correct answer (0-based)
                "explanation": "Python uses dynamic typing, so you just write: x = 5"
            },
            {
                "question": "Which data type is mutable in Python?",
                "options": [
                    "tuple",
                    "string",
                    "list",
                    "integer"
                ],
                "answer": 2,
                "explanation": "Lists are mutable, meaning you can change their contents after creation."
            },
            {
                "question": "What does the 'len()' function do?",
                "options": [
                    "Returns the length of an object",
                    "Returns the type of an object",
                    "Converts to lowercase",
                    "Lengthens a string"
                ],
                "answer": 0,
                "explanation": "len() returns the number of items in an object like a list or string."
            },
            {
                "question": "Which loop is best for iterating over a list?",
                "options": [
                    "while loop",
                    "do-while loop",
                    "for loop",
                    "until loop"
                ],
                "answer": 2,
                "explanation": "For loops are ideal for iterating through sequences like lists."
            },
            {
                "question": "How do you start a function definition in Python?",
                "options": [
                    "function myFunc():",
                    "def myFunc():",
                    "func myFunc():",
                    "define myFunc():"
                ],
                "answer": 1,
                "explanation": "Functions in Python are defined using the 'def' keyword."
            }
        ],
        "General Knowledge": [
            {
                "question": "What is the capital of France?",
                "options": [
                    "London",
                    "Berlin",
                    "Paris",
                    "Madrid"
                ],
                "answer": 2,
                "explanation": "Paris is the capital and largest city of France."
            },
            {
                "question": "How many continents are there?",
                "options": [
                    "5",
                    "6",
                    "7",
                    "8"
                ],
                "answer": 2,
                "explanation": "There are 7 continents: Africa, Antarctica, Asia, Europe, North America, Oceania, and South America."
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": [
                    "Saturn",
                    "Jupiter",
                    "Neptune",
                    "Earth"
                ],
                "answer": 1,
                "explanation": "Jupiter is the largest planet, with a mass greater than all other planets combined."
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": [
                    "Charles Dickens",
                    "Jane Austen",
                    "William Shakespeare",
                    "Mark Twain"
                ],
                "answer": 2,
                "explanation": "William Shakespeare wrote Romeo and Juliet around 1595."
            },
            {
                "question": "What is H2O commonly known as?",
                "options": [
                    "Oxygen",
                    "Hydrogen",
                    "Water",
                    "Carbon Dioxide"
                ],
                "answer": 2,
                "explanation": "H2O is the chemical formula for water."
            }
        ],
        "Math": [
            {
                "question": "What is 12 x 12?",
                "options": [
                    "124",
                    "144",
                    "142",
                    "134"
                ],
                "answer": 1,
                "explanation": "12 multiplied by 12 equals 144."
            },
            {
                "question": "What is the square root of 64?",
                "options": [
                    "6",
                    "7",
                    "8",
                    "9"
                ],
                "answer": 2,
                "explanation": "8 x 8 = 64, so the square root of 64 is 8."
            },
            {
                "question": "What is 25% of 200?",
                "options": [
                    "25",
                    "50",
                    "75",
                    "100"
                ],
                "answer": 1,
                "explanation": "25% is one quarter, and one quarter of 200 is 50."
            },
            {
                "question": "What is the value of pi (π) approximately?",
                "options": [
                    "2.14",
                    "3.14",
                    "4.14",
                    "5.14"
                ],
                "answer": 1,
                "explanation": "Pi (π) is approximately 3.14159, often rounded to 3.14."
            },
            {
                "question": "What is 7 + 8 x 2?",
                "options": [
                    "30",
                    "23",
                    "22",
                    "15"
                ],
                "answer": 1,
                "explanation": "Following order of operations (PEMDAS), multiply first: 8 x 2 = 16, then add 7 = 23."
            }
        ]
    }

    return quizzes


def display_welcome():
    """Display welcome message and instructions."""
    print("\n" + "=" * 60)
    print("  WELCOME TO THE QUIZ GAME!")
    print("=" * 60)
    print("\nTest your knowledge with multiple-choice questions!")
    print("Choose a category, answer questions, and see your score.")
    print("You'll get immediate feedback on each answer.")
    print()


def display_categories(quizzes):
    """
    Display available quiz categories.

    Args:
        quizzes: Dictionary of quiz categories and questions
    """
    print("\nAvailable Categories:")
    print("-" * 40)

    categories = list(quizzes.keys())
    for i, category in enumerate(categories, 1):
        question_count = len(quizzes[category])
        print(f"{i}. {category} ({question_count} questions)")

    print("-" * 40)


def choose_category(quizzes):
    """
    Let player choose a quiz category.

    Args:
        quizzes: Dictionary of quiz categories and questions

    Returns:
        str: Selected category name
    """
    categories = list(quizzes.keys())

    while True:
        try:
            choice = int(input(f"\nEnter category number (1-{len(categories)}): "))

            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("That's not a valid number! Try again.")


def display_question(question_data, question_num, total_questions):
    """
    Display a single question with its options.

    Args:
        question_data: Dictionary containing question information
        question_num: Current question number
        total_questions: Total number of questions in quiz
    """
    print("\n" + "=" * 60)
    print(f"Question {question_num}/{total_questions}")
    print("=" * 60)
    print(f"\n{question_data['question']}")
    print()

    # Display options
    for i, option in enumerate(question_data['options'], 1):
        print(f"  {i}. {option}")
    print()


def get_answer():
    """
    Get the player's answer choice.

    Returns:
        int: Selected answer index (0-based)
    """
    while True:
        try:
            choice = int(input("Your answer (1-4): "))

            if 1 <= choice <= 4:
                return choice - 1  # Convert to 0-based index
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("That's not a valid number! Try again.")


def check_answer(question_data, user_answer):
    """
    Check if the answer is correct and provide feedback.

    Args:
        question_data: Dictionary containing question information
        user_answer: User's answer index (0-based)

    Returns:
        bool: True if answer is correct, False otherwise
    """
    correct_answer = question_data['answer']
    is_correct = user_answer == correct_answer

    print()
    if is_correct:
        print("✓ CORRECT! Well done!")
    else:
        correct_text = question_data['options'][correct_answer]
        print(f"✗ INCORRECT. The correct answer was: {correct_text}")

    # Show explanation
    print(f"Explanation: {question_data['explanation']}")

    return is_correct


def calculate_grade(score, total):
    """
    Calculate letter grade based on percentage.

    Args:
        score: Number of correct answers
        total: Total number of questions

    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    percentage = (score / total) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def display_results(score, total, category):
    """
    Display final quiz results.

    Args:
        score: Number of correct answers
        total: Total number of questions
        category: Category name
    """
    percentage = (score / total) * 100
    grade = calculate_grade(score, total)

    print("\n" + "=" * 60)
    print("  QUIZ COMPLETE!")
    print("=" * 60)
    print(f"\nCategory: {category}")
    print(f"Score: {score}/{total} ({percentage:.1f}%)")
    print(f"Grade: {grade}")
    print()

    # Provide encouraging message based on performance
    if percentage >= 90:
        print("Excellent work! You're a master of this topic!")
    elif percentage >= 80:
        print("Great job! You really know your stuff!")
    elif percentage >= 70:
        print("Good effort! You have a solid understanding.")
    elif percentage >= 60:
        print("Not bad! Keep studying to improve your score.")
    else:
        print("Keep practicing! Review the explanations to learn more.")

    print("=" * 60)


def run_quiz(category, questions):
    """
    Run a complete quiz for a given category.

    Args:
        category: Category name
        questions: List of question dictionaries

    Returns:
        tuple: (score, total_questions)
    """
    score = 0
    total_questions = len(questions)

    print(f"\n{'='*60}")
    print(f"  Starting {category} Quiz!")
    print(f"{'='*60}")
    print(f"\nYou'll be asked {total_questions} questions.")
    print("Read carefully and choose the best answer.")
    input("\nPress Enter to begin...")

    # Ask each question
    for i, question_data in enumerate(questions, 1):
        display_question(question_data, i, total_questions)
        user_answer = get_answer()
        is_correct = check_answer(question_data, user_answer)

        if is_correct:
            score += 1

        # Pause before next question (except after last question)
        if i < total_questions:
            input("\nPress Enter for the next question...")

    return score, total_questions


def play_again():
    """
    Ask if player wants to take another quiz.

    Returns:
        bool: True if player wants to continue
    """
    while True:
        choice = input("\nTake another quiz? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main function to run the quiz game."""
    # Load all quiz questions
    quizzes = create_quiz_questions()

    display_welcome()

    # Main game loop
    while True:
        # Show categories and let player choose
        display_categories(quizzes)
        category = choose_category(quizzes)

        # Run the quiz for chosen category
        questions = quizzes[category]
        score, total = run_quiz(category, questions)

        # Show results
        display_results(score, total, category)

        # Ask if they want to play again
        if not play_again():
            break

    # Goodbye message
    print("\n" + "=" * 60)
    print("  Thanks for playing! Keep learning!")
    print("=" * 60 + "\n")


# Run the game when script is executed directly
if __name__ == "__main__":
    main()
