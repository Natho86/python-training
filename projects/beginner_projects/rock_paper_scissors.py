"""
Rock Paper Scissors Game
========================
Play the classic game against the computer with score tracking,
best-of-5 rounds, and detailed statistics.

Concepts Used:
- Random module for computer choices
- Lists for storing valid choices and results
- Loops (while, for) for game rounds
- Functions for code organization
- Control flow (if/elif/else) for game logic
- Variables and data types
- String methods (upper, strip)
- Mathematical calculations for statistics
"""

import random


def display_welcome():
    """Display welcome message and game rules."""
    print("\n" + "=" * 60)
    print("  ROCK, PAPER, SCISSORS!")
    print("=" * 60)
    print("\nWelcome to the classic game of Rock, Paper, Scissors!")
    print("\nRules:")
    print("  - Rock crushes Scissors")
    print("  - Scissors cuts Paper")
    print("  - Paper covers Rock")
    print("\nYou'll play best of 5 rounds against the computer.")
    print("First to win 3 rounds wins the match!")
    print("=" * 60 + "\n")


def display_choices():
    """Display the available choices."""
    print("\nChoose your move:")
    print("  1. Rock")
    print("  2. Paper")
    print("  3. Scissors")


def get_player_choice():
    """
    Get the player's choice with validation.

    Returns:
        str: Player's choice ('rock', 'paper', or 'scissors')
    """
    choices = {
        "1": "rock",
        "r": "rock",
        "rock": "rock",
        "2": "paper",
        "p": "paper",
        "paper": "paper",
        "3": "scissors",
        "s": "scissors",
        "scissors": "scissors"
    }

    while True:
        display_choices()
        player_input = input("\nEnter your choice (1-3, or name): ").strip().lower()

        if player_input in choices:
            return choices[player_input]
        else:
            print("Invalid choice! Please try again.")


def get_computer_choice():
    """
    Generate a random choice for the computer.

    Returns:
        str: Computer's choice ('rock', 'paper', or 'scissors')
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player, computer):
    """
    Determine the winner of a single round.

    Args:
        player: Player's choice
        computer: Computer's choice

    Returns:
        str: 'player', 'computer', or 'tie'
    """
    if player == computer:
        return "tie"

    # Define winning combinations
    winning_combinations = {
        "rock": "scissors",      # rock beats scissors
        "scissors": "paper",     # scissors beats paper
        "paper": "rock"          # paper beats rock
    }

    if winning_combinations[player] == computer:
        return "player"
    else:
        return "computer"


def display_round_result(round_num, player_choice, computer_choice, winner):
    """
    Display the result of a single round.

    Args:
        round_num: Current round number
        player_choice: What the player chose
        computer_choice: What the computer chose
        winner: Who won ('player', 'computer', or 'tie')
    """
    print("\n" + "-" * 60)
    print(f"Round {round_num}")
    print("-" * 60)
    print(f"You chose:      {player_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    print()

    if winner == "tie":
        print("It's a TIE! You both chose the same thing.")
    elif winner == "player":
        print("YOU WIN this round!")
        # Show why they won
        if player_choice == "rock":
            print("Rock crushes Scissors!")
        elif player_choice == "paper":
            print("Paper covers Rock!")
        else:
            print("Scissors cuts Paper!")
    else:
        print("COMPUTER WINS this round!")
        # Show why computer won
        if computer_choice == "rock":
            print("Rock crushes Scissors!")
        elif computer_choice == "paper":
            print("Paper covers Rock!")
        else:
            print("Scissors cuts Paper!")

    print("-" * 60)


def display_match_score(player_wins, computer_wins, ties):
    """
    Display the current match score.

    Args:
        player_wins: Number of rounds player has won
        computer_wins: Number of rounds computer has won
        ties: Number of tied rounds
    """
    print("\nCurrent Match Score:")
    print(f"  You: {player_wins} | Computer: {computer_wins} | Ties: {ties}")


def play_match():
    """
    Play a complete match (best of 5 rounds).

    Returns:
        dict: Match results with statistics
    """
    player_wins = 0
    computer_wins = 0
    ties = 0
    round_num = 0
    rounds_played = []

    print("\n" + "=" * 60)
    print("  MATCH START - First to 3 wins!")
    print("=" * 60)

    # Continue until someone wins 3 rounds
    while player_wins < 3 and computer_wins < 3:
        round_num += 1

        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        # Determine winner
        winner = determine_winner(player_choice, computer_choice)

        # Update scores
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        else:
            ties += 1

        # Store round data
        rounds_played.append({
            "round": round_num,
            "player": player_choice,
            "computer": computer_choice,
            "winner": winner
        })

        # Display result
        display_round_result(round_num, player_choice, computer_choice, winner)
        display_match_score(player_wins, computer_wins, ties)

        # Pause before next round (unless match is over)
        if player_wins < 3 and computer_wins < 3:
            input("\nPress Enter for the next round...")

    # Determine match winner
    match_winner = "player" if player_wins > computer_wins else "computer"

    return {
        "winner": match_winner,
        "player_wins": player_wins,
        "computer_wins": computer_wins,
        "ties": ties,
        "total_rounds": round_num,
        "rounds": rounds_played
    }


def calculate_statistics(match_results):
    """
    Calculate detailed statistics from match results.

    Args:
        match_results: Dictionary containing match data

    Returns:
        dict: Calculated statistics
    """
    total_rounds = match_results["total_rounds"]
    player_wins = match_results["player_wins"]
    computer_wins = match_results["computer_wins"]
    ties = match_results["ties"]

    # Calculate percentages
    win_percentage = (player_wins / total_rounds) * 100 if total_rounds > 0 else 0
    loss_percentage = (computer_wins / total_rounds) * 100 if total_rounds > 0 else 0
    tie_percentage = (ties / total_rounds) * 100 if total_rounds > 0 else 0

    # Count choice frequencies
    player_choices = {"rock": 0, "paper": 0, "scissors": 0}
    computer_choices = {"rock": 0, "paper": 0, "scissors": 0}

    for round_data in match_results["rounds"]:
        player_choices[round_data["player"]] += 1
        computer_choices[round_data["computer"]] += 1

    # Find most used choice
    most_used = max(player_choices, key=player_choices.get)

    return {
        "win_percentage": win_percentage,
        "loss_percentage": loss_percentage,
        "tie_percentage": tie_percentage,
        "player_choices": player_choices,
        "computer_choices": computer_choices,
        "most_used": most_used
    }


def display_match_results(match_results):
    """
    Display complete match results with statistics.

    Args:
        match_results: Dictionary containing match data
    """
    stats = calculate_statistics(match_results)

    print("\n" + "=" * 60)
    print("  MATCH COMPLETE!")
    print("=" * 60)

    # Display winner
    if match_results["winner"] == "player":
        print("\n🎉 CONGRATULATIONS! YOU WON THE MATCH! 🎉")
    else:
        print("\n💻 COMPUTER WINS THE MATCH! Better luck next time!")

    # Display final score
    print(f"\nFinal Score:")
    print(f"  You: {match_results['player_wins']}")
    print(f"  Computer: {match_results['computer_wins']}")
    print(f"  Ties: {match_results['ties']}")
    print(f"  Total Rounds: {match_results['total_rounds']}")

    # Display statistics
    print("\n" + "-" * 60)
    print("MATCH STATISTICS")
    print("-" * 60)

    print(f"\nWin Rate: {stats['win_percentage']:.1f}%")
    print(f"Loss Rate: {stats['loss_percentage']:.1f}%")
    print(f"Tie Rate: {stats['tie_percentage']:.1f}%")

    print("\nYour Choice Distribution:")
    for choice, count in stats['player_choices'].items():
        percentage = (count / match_results['total_rounds']) * 100
        print(f"  {choice.capitalize()}: {count} ({percentage:.1f}%)")

    print(f"\nYour most used move: {stats['most_used'].upper()}")

    print("\nComputer's Choice Distribution:")
    for choice, count in stats['computer_choices'].items():
        percentage = (count / match_results['total_rounds']) * 100
        print(f"  {choice.capitalize()}: {count} ({percentage:.1f}%)")

    print("=" * 60)


def display_round_history(match_results):
    """
    Display a summary of all rounds played.

    Args:
        match_results: Dictionary containing match data
    """
    print("\n" + "-" * 60)
    print("ROUND-BY-ROUND SUMMARY")
    print("-" * 60)

    for round_data in match_results["rounds"]:
        round_num = round_data["round"]
        player = round_data["player"]
        computer = round_data["computer"]
        winner = round_data["winner"]

        winner_text = "TIE" if winner == "tie" else ("YOU" if winner == "player" else "COMPUTER")

        print(f"Round {round_num}: {player.ljust(9)} vs {computer.ljust(9)} - Winner: {winner_text}")

    print("-" * 60)


def play_again():
    """
    Ask if player wants to play another match.

    Returns:
        bool: True if player wants to play again
    """
    while True:
        choice = input("\nPlay another match? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main function to run the game."""
    display_welcome()

    # Game loop - allows multiple matches
    while True:
        # Play one match
        match_results = play_match()

        # Display results and statistics
        display_match_results(match_results)

        # Ask if they want to see round history
        show_history = input("\nView round-by-round history? (yes/no): ").strip().lower()
        if show_history in ["yes", "y"]:
            display_round_history(match_results)

        # Ask if they want to play again
        if not play_again():
            break

    # Goodbye message
    print("\n" + "=" * 60)
    print("  Thanks for playing! See you next time!")
    print("=" * 60 + "\n")


# Run the game when script is executed directly
if __name__ == "__main__":
    main()
