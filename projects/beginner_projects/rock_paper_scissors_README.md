# Rock Paper Scissors Game

## Overview
Play the classic Rock, Paper, Scissors game against the computer! This enhanced version features best-of-5 matches, detailed statistics, win/loss/tie percentages, and round-by-round history tracking.

## Concepts Covered
This project combines concepts from Phase 1 (Exercises 1-15):
- **Random Module**: generating random computer choices
- **Lists**: storing valid choices and round history
- **Dictionaries**: organizing match results and statistics
- **Loops**: while loops for match continuation, for loops for data processing
- **Functions**: multiple functions with parameters and return values
- **Control Flow**: if/elif/else for game logic and win conditions
- **Variables and Data Types**: integers, strings, booleans, floats
- **String Methods**: upper(), lower(), strip() for input handling
- **Mathematical Operations**: percentage calculations, comparisons
- **List Comprehensions**: (implicitly through dictionary operations)

## Features
1. **Best of 5 Format**: First player to win 3 rounds wins the match

2. **Flexible Input**: Accept multiple input formats:
   - Numbers: 1, 2, 3
   - Letters: r, p, s
   - Full names: rock, paper, scissors

3. **Smart Computer Opponent**: Uses random selection for fair play

4. **Detailed Round Results**: See what each player chose and why they won

5. **Match Score Tracking**: Keep track of wins, losses, and ties throughout the match

6. **Comprehensive Statistics**:
   - Win/loss/tie percentages
   - Choice distribution (how often each move was used)
   - Most frequently used move
   - Computer's choice patterns

7. **Round History**: Review all rounds played in the match

8. **Multiple Matches**: Play as many matches as you want!

9. **Input Validation**: Handles invalid inputs gracefully

## How to Run
1. Make sure you have Python 3 installed
2. Navigate to the project directory
3. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```

## How to Play
1. Start the game and read the welcome message and rules
2. Each round, choose your move:
   - Enter 1, 2, or 3
   - Or type 'rock', 'paper', or 'scissors'
   - Or use shortcuts: 'r', 'p', 's'
3. See the result of each round with explanation
4. View the current match score after each round
5. Press Enter to continue to the next round
6. The match ends when someone wins 3 rounds
7. View final statistics and optionally see round history
8. Choose whether to play another match

## Example Gameplay
```
============================================================
  ROCK, PAPER, SCISSORS!
============================================================

Welcome to the classic game of Rock, Paper, Scissors!

Rules:
  - Rock crushes Scissors
  - Scissors cuts Paper
  - Paper covers Rock

You'll play best of 5 rounds against the computer.
First to win 3 rounds wins the match!
============================================================

============================================================
  MATCH START - First to 3 wins!
============================================================

Choose your move:
  1. Rock
  2. Paper
  3. Scissors

Enter your choice (1-3, or name): rock

------------------------------------------------------------
Round 1
------------------------------------------------------------
You chose:      ROCK
Computer chose: SCISSORS

YOU WIN this round!
Rock crushes Scissors!
------------------------------------------------------------

Current Match Score:
  You: 1 | Computer: 0 | Ties: 0

Press Enter for the next round...
```

## Learning Objectives
By studying and modifying this project, you'll learn:
1. How to use the random module for generating choices
2. How to implement game logic with conditional statements
3. How to track state across multiple rounds
4. How to calculate and display statistics
5. How to handle different input formats
6. How to structure a game with multiple matches
7. How to provide informative feedback to users
8. How to organize complex data in dictionaries

## Possible Enhancements
Try adding these features to practice more:
1. **Difficulty Levels**:
   - Easy: Computer choices are weighted (more predictable)
   - Hard: Computer tries to counter your patterns

2. **Advanced Statistics**:
   - Track overall stats across multiple matches
   - Save statistics to a file
   - Show winning streaks

3. **Tournament Mode**:
   - Best of 7 or best of 9
   - Multiple players taking turns

4. **AI Learning**:
   - Track player's patterns and adjust strategy
   - Use weighted randomness based on history

5. **Extended Game**:
   - Add "Lizard" and "Spock" (Rock-Paper-Scissors-Lizard-Spock)

6. **Visual Enhancements**:
   - ASCII art for each choice
   - Color-coded output (using colorama)
   - Animated countdowns

7. **Multiplayer**:
   - Two human players
   - Hide inputs from each other

8. **Score Persistence**:
   - Save win/loss records to file
   - Display all-time statistics
   - Leaderboard system

## Code Structure
The program is organized into clear functions:
- `display_welcome()`: Shows game introduction and rules
- `display_choices()`: Lists available moves
- `get_player_choice()`: Gets and validates player's move
- `get_computer_choice()`: Generates random computer move
- `determine_winner()`: Applies game rules to determine round winner
- `display_round_result()`: Shows outcome of a single round
- `display_match_score()`: Shows current match score
- `play_match()`: Main logic for one complete match
- `calculate_statistics()`: Computes percentages and frequencies
- `display_match_results()`: Shows final results with statistics
- `display_round_history()`: Lists all rounds played
- `play_again()`: Asks if user wants another match
- `main()`: Orchestrates the entire game flow

## Understanding the Game Logic
The winner is determined using a dictionary of winning combinations:
```python
winning_combinations = {
    "rock": "scissors",      # rock beats scissors
    "scissors": "paper",     # scissors beats paper
    "paper": "rock"          # paper beats rock
}
```

To check if player wins:
1. If both chose the same thing → tie
2. If player's choice beats computer's choice → player wins
3. Otherwise → computer wins

## Statistics Calculations
The game tracks various statistics:

**Percentages**:
- Win Rate = (Rounds Won / Total Rounds) × 100
- Loss Rate = (Rounds Lost / Total Rounds) × 100
- Tie Rate = (Ties / Total Rounds) × 100

**Choice Distribution**:
- Count how many times each choice was used
- Calculate percentage for each choice

## Tips for Understanding the Code
1. Start with `main()` to see the overall flow
2. Follow a single match through `play_match()`
3. Look at `determine_winner()` to understand the game rules
4. Examine `calculate_statistics()` to see how stats are computed
5. Notice how dictionaries store and organize data
6. See how the `max()` function with `key=` finds the most used choice
7. Observe how input validation allows multiple formats

## Common Modifications for Practice
1. Change the number of rounds needed to win (best of 7, etc.)
2. Add more detailed explanations for wins
3. Modify the statistics displayed
4. Change the input options (different shortcuts)
5. Add a running total across multiple matches
6. Implement a simple AI that favors certain choices
7. Add timing information (how long each round took)
8. Create ASCII art for rock, paper, and scissors

## Game Rules Reference
```
ROCK beats SCISSORS (rock crushes scissors)
SCISSORS beats PAPER (scissors cuts paper)
PAPER beats ROCK (paper covers rock)
```

## Data Structures Used
**Match Results Dictionary**:
```python
{
    "winner": "player" or "computer",
    "player_wins": int,
    "computer_wins": int,
    "ties": int,
    "total_rounds": int,
    "rounds": [
        {
            "round": int,
            "player": str,
            "computer": str,
            "winner": str
        },
        ...
    ]
}
```

**Statistics Dictionary**:
```python
{
    "win_percentage": float,
    "loss_percentage": float,
    "tie_percentage": float,
    "player_choices": {"rock": int, "paper": int, "scissors": int},
    "computer_choices": {"rock": int, "paper": int, "scissors": int},
    "most_used": str
}
```
