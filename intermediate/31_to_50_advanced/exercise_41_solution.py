# Exercise 41: Random Module and Number Generation - SOLUTION
# Difficulty: Intermediate-
# Concepts: random module, Random numbers, Randomization

import random

# SOLUTION
print("=== Random Module Examples ===")

# Random integers
print("\n--- Random Integers ---")
random_int = random.randint(1, 10)
print(f"Random integer (1-10): {random_int}")

random_int_100 = random.randint(1, 100)
print(f"Random integer (1-100): {random_int_100}")

# Random float
print("\n--- Random Floats ---")
random_float = random.random()  # 0.0 to 1.0
print(f"Random float (0-1): {random_float:.4f}")

random_float_range = random.uniform(10, 20)  # Between 10 and 20
print(f"Random float (10-20): {random_float_range:.2f}")

# Random choice
print("\n--- Random Choice ---")
colors = ['red', 'blue', 'green', 'yellow', 'purple']
random_color = random.choice(colors)
print(f"Random color: {random_color}")

rps = ['rock', 'paper', 'scissors']
computer_choice = random.choice(rps)
print(f"Computer plays: {computer_choice}")

# Random sample (multiple unique items)
print("\n--- Random Sample ---")
numbers = list(range(1, 11))
random_sample = random.sample(numbers, 3)  # Pick 3 unique numbers
print(f"Random sample of 3 from {numbers}: {random_sample}")

# Shuffle
print("\n--- Shuffle ---")
deck = list(range(1, 10))
print(f"Original deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# Dice rolls
print("\n--- Dice Rolls ---")
def roll_dice(num_dice=1, sides=6):
    """Simulate rolling dice."""
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls)
    return rolls, total

rolls, total = roll_dice(2, 6)  # 2 six-sided dice
print(f"Rolling 2d6: {rolls[0]} + {rolls[1]} = {total}")

# Coin flip
print("\n--- Coin Flip ---")
def flip_coin():
    """Simulate coin flip."""
    return random.choice(['Heads', 'Tails'])

print(f"Coin flip: {flip_coin()}")

# Multiple flips
flips = [flip_coin() for _ in range(10)]
print(f"10 flips: {flips}")
print(f"Heads: {flips.count('Heads')}, Tails: {flips.count('Tails')}")

"""
EXPLANATION:
1. random.randint(a, b) - random integer from a to b (both inclusive)
2. random.random() - random float from 0.0 to 1.0
3. random.uniform(a, b) - random float from a to b
4. random.choice(seq) - random element from sequence
5. random.sample(seq, k) - k unique random elements from sequence
6. random.shuffle(list) - shuffles list in-place (modifies original)

Key Concepts:
- random module provides pseudo-random number generation
- Useful for games, simulations, sampling, and testing
- random.seed() can set seed for reproducible results
- For cryptographic purposes, use secrets module instead
"""

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

def generate_lottery_numbers(count=6, max_number=49):
    """
    Generate lottery numbers.

    Args:
        count: How many numbers to pick
        max_number: Highest number in range

    Returns:
        list: Sorted list of unique random numbers
    """
    numbers = random.sample(range(1, max_number + 1), count)
    return sorted(numbers)

def generate_password(length=12, use_symbols=True):
    """
    Generate a random password.

    Args:
        length: Password length
        use_symbols: Include special characters

    Returns:
        str: Random password
    """
    import string

    # Build character set
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Test lottery generator
print("\nLottery Numbers:")
for i in range(3):
    numbers = generate_lottery_numbers()
    print(f"  Ticket {i+1}: {numbers}")

# Test password generator
print("\nRandom Passwords:")
print(f"  Simple (8 chars): {generate_password(8, use_symbols=False)}")
print(f"  Medium (12 chars): {generate_password(12, use_symbols=True)}")
print(f"  Strong (16 chars): {generate_password(16, use_symbols=True)}")

# More practical examples
print("\n--- MORE RANDOM EXAMPLES ---")

# Random quote generator
def random_quote():
    """Return a random inspirational quote."""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "Life is what happens to you while you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

print(f"\nRandom quote:\n{random_quote()}")

# Weighted random choice
def weighted_choice():
    """Example of weighted random selection."""
    items = ['common', 'uncommon', 'rare', 'epic', 'legendary']
    weights = [50, 30, 15, 4, 1]  # Probability weights
    return random.choices(items, weights=weights, k=1)[0]

print("\nRandom loot drops (weighted):")
drops = [weighted_choice() for _ in range(10)]
print(f"  {drops}")

# Card deck simulation
print("\n--- CARD DECK SIMULATION ---")

def create_deck():
    """Create a standard deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    return deck

def deal_hand(deck, num_cards=5):
    """Deal a hand of cards."""
    hand = random.sample(deck, num_cards)
    return hand

deck = create_deck()
print(f"Deck has {len(deck)} cards")
hand = deal_hand(deck, 5)
print(f"Your hand: {hand}")

# Random event simulator
print("\n--- RANDOM EVENT SIMULATOR ---")

def random_weather():
    """Simulate random weather with probabilities."""
    weather_options = ['Sunny', 'Cloudy', 'Rainy', 'Stormy']
    probabilities = [0.4, 0.3, 0.2, 0.1]  # 40%, 30%, 20%, 10%
    return random.choices(weather_options, probabilities)[0]

print("Weather forecast for next 7 days:")
for day in range(1, 8):
    print(f"  Day {day}: {random_weather()}")

# Reproducible randomness
print("\n--- REPRODUCIBLE RANDOMNESS ---")
print("Setting random seed for reproducibility:")

random.seed(42)
print(f"Random 1: {random.randint(1, 100)}")
print(f"Random 2: {random.randint(1, 100)}")

random.seed(42)  # Reset to same seed
print(f"Random 1 (again): {random.randint(1, 100)}")  # Same as before
print(f"Random 2 (again): {random.randint(1, 100)}")  # Same as before
