# Number Guessing Game - Enhanced Version

## Overview
An interactive number guessing game where players try to guess a randomly generated number in as few attempts as possible. The game features multiple difficulty levels, score tracking, persistent high scores, and helpful hints.

## Concepts Covered
This project combines concepts from Phase 1 (Exercises 1-15):
- **Variables and Data Types**: integers, strings, tuples
- **Control Flow**: if/elif/else statements, comparison operators
- **Loops**: while loops for game logic, for loops for file reading
- **Functions**: multiple functions with parameters and return values
- **File I/O**: reading and writing high scores to a text file
- **Error Handling**: try/except for input validation and file operations
- **Random Module**: generating random numbers
- **String Formatting**: f-strings and formatted output

## Features
1. **Three Difficulty Levels**:
   - Easy: Guess a number 1-50 in 10 attempts
   - Medium: Guess a number 1-100 in 8 attempts
   - Hard: Guess a number 1-200 in 7 attempts

2. **Smart Hints**: The game tells you if you're:
   - Very close (within 5)
   - Getting warm (within 15)
   - Quite far off (more than 15 away)

3. **Score System**: Your score is based on how few attempts you use. Fewer attempts = higher score!

4. **High Score Tracking**: High scores are saved to a file and persist between game sessions.

5. **Input Validation**: The game handles invalid inputs gracefully and prompts you to try again.

6. **Play Multiple Rounds**: Keep playing as many times as you want!

## How to Run
1. Make sure you have Python 3 installed
2. Navigate to the project directory
3. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## How to Play
1. Start the game and you'll see a welcome message
2. Choose your difficulty level (1, 2, or 3)
3. The game will think of a secret number
4. Enter your guesses when prompted
5. The game will tell you if your guess is too high or too low
6. Keep guessing until you find the number or run out of attempts
7. See your score and check if you beat the high score!
8. Choose whether to play again

## Example Gameplay
```
==================================================
  WELCOME TO THE NUMBER GUESSING GAME!
==================================================

Try to guess the secret number in as few attempts
as possible. The fewer attempts, the higher your score!

Choose your difficulty level:
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 8 attempts)
3. Hard   (1-200, 7 attempts)

Enter 1, 2, or 3: 2

==================================================
Difficulty: Medium
I'm thinking of a number between 1 and 100...
You have 8 attempts to guess it!
==================================================

Attempt 1/8
Enter your guess (1-100): 50
Too low! You're quite far off.
You have 7 attempts remaining.

Attempt 2/8
Enter your guess (1-100): 75
Too high! You're getting warm!
You have 6 attempts remaining.

Attempt 3/8
Enter your guess (1-100): 68
**************************************************
  CONGRATULATIONS! You got it in 3 attempts!
**************************************************
Your score: 812
```

## Learning Objectives
By studying and modifying this project, you'll learn:
1. How to structure a complete program with multiple functions
2. How to use loops for game logic and input validation
3. How to work with files to persist data
4. How to handle errors gracefully
5. How to create an engaging user experience with clear output
6. How to use the random module for game mechanics

## Possible Enhancements
Try adding these features to practice more:
1. Add a "hint" system that costs points but reveals information
2. Track and display game statistics (total games, win rate, etc.)
3. Add a timer to limit how long players have to guess
4. Create an "expert" difficulty with even larger numbers
5. Allow players to enter their name for the high score board
6. Add sound effects (using a module like `winsound` on Windows)
7. Create a two-player mode where players take turns
8. Add a "guess history" showing all previous guesses

## Code Structure
The program is organized into clear functions:
- `display_welcome()`: Shows game introduction
- `choose_difficulty()`: Handles difficulty selection
- `get_valid_guess()`: Gets and validates player input
- `calculate_score()`: Computes score based on attempts
- `play_game()`: Main game logic for one round
- `load_high_scores()`: Reads high scores from file
- `save_high_scores()`: Writes high scores to file
- `update_high_score()`: Checks and updates high scores
- `display_high_scores()`: Shows all high scores
- `play_again()`: Asks if player wants another round
- `main()`: Orchestrates the entire game flow

## Files Created
- `high_scores.txt`: Automatically created to store high scores (format: difficulty:score)

## Tips for Understanding the Code
1. Start by reading `main()` to understand the overall flow
2. Follow the execution path through each function call
3. Pay attention to how functions return values and how they're used
4. Notice how error handling prevents crashes from bad input
5. See how file I/O is wrapped in try/except for safety
6. Observe how the score calculation formula works

## Common Modifications for Practice
1. Change the score calculation formula
2. Adjust the "closeness" thresholds for hints
3. Modify the number ranges for each difficulty
4. Add more difficulty levels
5. Change how high scores are stored (maybe use JSON?)
6. Add color to the output (using the `colorama` module)
