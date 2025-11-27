"""
Number Guessing Game - Enhanced Version
========================================
A fun interactive game where you try to guess a randomly generated number.
Features difficulty levels, score tracking, high scores, and replay option.

Concepts Used:
- Random number generation
- Loops (while, for)
- Functions
- Control flow (if/elif/else)
- File I/O (reading/writing high scores)
- Error handling
- String formatting
"""

import random
import os


def display_welcome():
    """Display welcome message and game instructions."""
    print("\n" + "=" * 50)
    print("  WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 50)
    print("\nTry to guess the secret number in as few attempts")
    print("as possible. The fewer attempts, the higher your score!")
    print()


def choose_difficulty():
    """
    Let the player choose a difficulty level.

    Returns:
        tuple: (range_max, max_attempts, difficulty_name)
    """
    print("Choose your difficulty level:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 8 attempts)")
    print("3. Hard   (1-200, 7 attempts)")
    print()

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 8, "Medium"
        elif choice == "3":
            return 200, 7, "Hard"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def get_valid_guess(min_val, max_val):
    """
    Get a valid integer guess from the player.

    Args:
        min_val: Minimum valid number
        max_val: Maximum valid number

    Returns:
        int: Valid guess from player
    """
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_val}): "))

            if guess < min_val or guess > max_val:
                print(f"Please enter a number between {min_val} and {max_val}!")
                continue

            return guess
        except ValueError:
            print("That's not a valid number! Try again.")


def calculate_score(attempts, max_attempts):
    """
    Calculate player's score based on attempts used.

    Args:
        attempts: Number of attempts used
        max_attempts: Maximum attempts allowed

    Returns:
        int: Calculated score (higher is better)
    """
    # Score formula: more attempts = lower score
    base_score = 1000
    penalty = (attempts / max_attempts) * 500
    return int(base_score - penalty)


def play_game(range_max, max_attempts, difficulty):
    """
    Main game logic for one round.

    Args:
        range_max: Maximum number in range
        max_attempts: Maximum allowed attempts
        difficulty: Difficulty level name

    Returns:
        int: Player's score (or 0 if they didn't win)
    """
    # Generate secret number
    secret_number = random.randint(1, range_max)
    attempts = 0

    print(f"\n{'='*50}")
    print(f"Difficulty: {difficulty}")
    print(f"I'm thinking of a number between 1 and {range_max}...")
    print(f"You have {max_attempts} attempts to guess it!")
    print(f"{'='*50}\n")

    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1

        print(f"\nAttempt {attempts}/{max_attempts}")
        guess = get_valid_guess(1, range_max)

        # Check the guess
        if guess == secret_number:
            print(f"\n{'*'*50}")
            print(f"  CONGRATULATIONS! You got it in {attempts} attempts!")
            print(f"{'*'*50}")
            score = calculate_score(attempts, max_attempts)
            print(f"Your score: {score}")
            return score
        elif guess < secret_number:
            print(f"Too low! ", end="")
        else:
            print(f"Too high! ", end="")

        # Give hint about how close they are (if not last attempt)
        if remaining > 0:
            difference = abs(guess - secret_number)
            if difference <= 5:
                print("But you're very close!")
            elif difference <= 15:
                print("You're getting warm!")
            else:
                print("You're quite far off.")

            print(f"You have {remaining} attempts remaining.")

    # Player ran out of attempts
    print(f"\n{'='*50}")
    print(f"  GAME OVER! You ran out of attempts.")
    print(f"  The secret number was: {secret_number}")
    print(f"{'='*50}")
    return 0


def load_high_scores():
    """
    Load high scores from file.

    Returns:
        dict: High scores for each difficulty level
    """
    default_scores = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0
    }

    # Check if high scores file exists
    if not os.path.exists("high_scores.txt"):
        return default_scores

    try:
        with open("high_scores.txt", "r") as file:
            scores = {}
            for line in file:
                line = line.strip()
                if line and ":" in line:
                    difficulty, score = line.split(":")
                    scores[difficulty] = int(score)
            return scores if scores else default_scores
    except (IOError, ValueError):
        # If there's any error reading, return defaults
        return default_scores


def save_high_scores(scores):
    """
    Save high scores to file.

    Args:
        scores: Dictionary of high scores by difficulty
    """
    try:
        with open("high_scores.txt", "w") as file:
            for difficulty, score in scores.items():
                file.write(f"{difficulty}:{score}\n")
    except IOError:
        print("Warning: Could not save high scores to file.")


def update_high_score(difficulty, score):
    """
    Update high score if the new score is better.

    Args:
        difficulty: Difficulty level name
        score: New score to compare

    Returns:
        bool: True if new high score was set
    """
    if score == 0:
        return False

    high_scores = load_high_scores()

    if score > high_scores.get(difficulty, 0):
        high_scores[difficulty] = score
        save_high_scores(high_scores)
        print(f"\n{'*'*50}")
        print(f"  NEW HIGH SCORE for {difficulty} difficulty!")
        print(f"{'*'*50}")
        return True

    return False


def display_high_scores():
    """Display all high scores."""
    high_scores = load_high_scores()

    print("\n" + "="*50)
    print("  HIGH SCORES")
    print("="*50)
    for difficulty in ["Easy", "Medium", "Hard"]:
        score = high_scores.get(difficulty, 0)
        print(f"{difficulty:10s}: {score:4d}")
    print("="*50)


def play_again():
    """
    Ask player if they want to play again.

    Returns:
        bool: True if player wants to play again
    """
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main function to run the game."""
    display_welcome()

    # Game loop - allows multiple rounds
    while True:
        # Choose difficulty
        range_max, max_attempts, difficulty = choose_difficulty()

        # Play one game
        score = play_game(range_max, max_attempts, difficulty)

        # Update high score if applicable
        update_high_score(difficulty, score)

        # Show current high scores
        display_high_scores()

        # Ask if they want to play again
        if not play_again():
            break

    # Goodbye message
    print("\n" + "="*50)
    print("  Thanks for playing! Goodbye!")
    print("="*50 + "\n")


# Run the game when script is executed directly
if __name__ == "__main__":
    main()
