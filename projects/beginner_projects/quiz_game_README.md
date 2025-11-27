# Simple Quiz Game

## Overview
An interactive multiple-choice quiz game with different categories. Test your knowledge on Python Basics, General Knowledge, or Math! Get immediate feedback on your answers and see your final score and grade.

## Concepts Covered
This project combines concepts from Phase 1 (Exercises 1-15):
- **Lists**: storing questions, options, and categories
- **Dictionaries**: organizing quiz data with keys and values
- **Loops**: for loops to iterate through questions, while loops for input validation
- **Functions**: multiple functions for code organization
- **Control Flow**: if/elif/else for answer checking and grading
- **String Formatting**: f-strings for displaying questions and results
- **List Indexing**: accessing specific elements
- **Error Handling**: try/except for input validation
- **Enumerate**: tracking question numbers while iterating

## Features
1. **Multiple Categories**:
   - Python Basics (5 questions)
   - General Knowledge (5 questions)
   - Math (5 questions)

2. **Multiple Choice Format**: Four options for each question

3. **Immediate Feedback**: After each answer, you'll see:
   - Whether you were correct or incorrect
   - The correct answer (if you were wrong)
   - An explanation to help you learn

4. **Score Tracking**: Keep track of correct answers throughout the quiz

5. **Grade Calculation**: Get a letter grade (A-F) based on your percentage:
   - A: 90-100%
   - B: 80-89%
   - C: 70-79%
   - D: 60-69%
   - F: Below 60%

6. **Multiple Quizzes**: Take as many quizzes as you want!

7. **Input Validation**: The game handles invalid inputs gracefully

## How to Run
1. Make sure you have Python 3 installed
2. Navigate to the project directory
3. Run the game:
   ```bash
   python quiz_game.py
   ```

## How to Play
1. Start the game and read the welcome message
2. Choose a category by entering its number (1-3)
3. Press Enter to begin the quiz
4. For each question:
   - Read the question carefully
   - Choose your answer by entering 1, 2, 3, or 4
   - See immediate feedback and explanation
   - Press Enter to continue to the next question
5. After all questions, view your final score and grade
6. Choose whether to take another quiz

## Example Gameplay
```
============================================================
  WELCOME TO THE QUIZ GAME!
============================================================

Test your knowledge with multiple-choice questions!
Choose a category, answer questions, and see your score.
You'll get immediate feedback on each answer.


Available Categories:
----------------------------------------
1. Python Basics (5 questions)
2. General Knowledge (5 questions)
3. Math (5 questions)
----------------------------------------

Enter category number (1-3): 1

============================================================
  Starting Python Basics Quiz!
============================================================

You'll be asked 5 questions.
Read carefully and choose the best answer.

Press Enter to begin...

============================================================
Question 1/5
============================================================

What is the correct way to create a variable in Python?

  1. int x = 5
  2. x = 5
  3. var x = 5
  4. dim x = 5

Your answer (1-4): 2

✓ CORRECT! Well done!
Explanation: Python uses dynamic typing, so you just write: x = 5

Press Enter for the next question...
```

## Learning Objectives
By studying and modifying this project, you'll learn:
1. How to organize data using nested dictionaries and lists
2. How to create a multi-category application
3. How to provide user feedback in an interactive program
4. How to validate user input effectively
5. How to calculate percentages and assign grades
6. How to structure a complete application with many functions
7. How to iterate through complex data structures

## Possible Enhancements
Try adding these features to practice more:
1. **Add More Questions**: Create more questions for existing categories
2. **New Categories**: Add new quiz categories (Science, History, etc.)
3. **Difficulty Levels**: Add easy, medium, and hard versions of questions
4. **Time Limits**: Add a timer for each question
5. **Randomize Questions**: Shuffle questions and answer options
6. **High Scores**: Save high scores to a file
7. **Review Mode**: Let players review all questions at the end
8. **Hints**: Add a hint system (maybe costs points)
9. **Multiple Players**: Track scores for different players
10. **Load from File**: Read questions from a text or JSON file
11. **True/False Questions**: Support different question types
12. **Question Bank**: Randomly select N questions from a larger pool

## Code Structure
The program is organized into clear functions:
- `create_quiz_questions()`: Defines all quiz questions and answers
- `display_welcome()`: Shows game introduction
- `display_categories()`: Lists available quiz categories
- `choose_category()`: Handles category selection
- `display_question()`: Shows a question with options
- `get_answer()`: Gets and validates user's answer
- `check_answer()`: Verifies answer and provides feedback
- `calculate_grade()`: Converts percentage to letter grade
- `display_results()`: Shows final score and grade
- `run_quiz()`: Main logic for running one quiz
- `play_again()`: Asks if user wants another quiz
- `main()`: Orchestrates the entire game flow

## Understanding the Data Structure
The quiz questions are stored in a nested dictionary:
```python
{
    "Category Name": [
        {
            "question": "Question text?",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": 0,  # Index of correct option (0-3)
            "explanation": "Why this is the correct answer"
        },
        # More questions...
    ],
    # More categories...
}
```

This structure allows for:
- Easy addition of new categories
- Simple addition of new questions
- Clear organization of question data
- Easy iteration through questions

## Tips for Understanding the Code
1. Start by examining the `create_quiz_questions()` function to see how data is structured
2. Read `main()` to understand the overall program flow
3. Follow how the category is selected and passed to `run_quiz()`
4. Notice how enumerate() is used to get both index and item in loops
5. See how list indexing works with `[choice - 1]` to convert user input
6. Observe how the percentage is calculated: `(score / total) * 100`

## Common Modifications for Practice
1. Change the grading scale (different percentage cutoffs)
2. Add more questions to existing categories
3. Create your own quiz category
4. Change the number of options per question
5. Modify the feedback messages
6. Add emojis or colors to make it more engaging
7. Change the format of how questions are displayed

## Adding Your Own Questions
To add new questions, edit the `create_quiz_questions()` function:

```python
"Your Category": [
    {
        "question": "Your question here?",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": 2,  # Index of correct answer (0=first, 1=second, 2=third, 3=fourth)
        "explanation": "Why this answer is correct"
    },
    # Add more questions...
]
```

Remember: The answer is the index (position) of the correct option, starting from 0!
