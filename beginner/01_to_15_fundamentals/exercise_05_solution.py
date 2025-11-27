# Exercise 5: Number Guessing Game - SOLUTION
# Difficulty: Beginner
# Concepts: While loops, Random numbers, Control flow, Comparison operators

import random

# SOLUTION
def number_guessing_game():
    """Simple number guessing game."""
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100...")

    # Loop until correct guess
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break  # Exit the loop

# Run the game
number_guessing_game()

"""
EXPLANATION:
1. We import the random module to generate random numbers
2. random.randint(1, 100) generates a random integer from 1 to 100 (inclusive)
3. We initialize attempts counter to 0
4. while True creates an infinite loop (we'll break out when guessed correctly)
5. We increment attempts with each guess using +=
6. We compare the guess to the secret number and give feedback
7. When correct, we print the result and use 'break' to exit the loop

Key Concepts:
- import statement brings in external modules
- random.randint(a, b) generates random integer from a to b
- while True creates an infinite loop
- break statement exits a loop early
- += operator adds to a variable (attempts += 1 is same as attempts = attempts + 1)
"""

# Extension solution: Difficulty levels and proximity hints
print("\n--- EXTENSION SOLUTION ---")

def advanced_guessing_game():
    """Guessing game with difficulty levels and hints."""
    print("Choose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    difficulty = int(input("Enter choice (1-3): "))

    if difficulty == 1:
        max_num = 50
    elif difficulty == 2:
        max_num = 100
    elif difficulty == 3:
        max_num = 500
    else:
        print("Invalid choice, defaulting to Medium")
        max_num = 100

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_num}...")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        difference = abs(guess - secret_number)

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break
        elif difference <= 5:
            print("You're very close!")
            if guess < secret_number:
                print("But still too low!")
            else:
                print("But still too high!")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

advanced_guessing_game()
