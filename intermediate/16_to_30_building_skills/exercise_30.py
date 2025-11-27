# Exercise 30: Mini Text Adventure Game
# Difficulty: Intermediate-
# Concepts: Dictionaries, Functions, Control flow, User input, Game logic

"""
PROBLEM:
Create a text-based adventure game that combines all Phase 2 concepts:
1. Use dictionaries to store game state (player stats, inventory, locations)
2. Implement different locations/rooms with descriptions
3. Handle user commands (go, take, use, look, inventory)
4. Store game data in files (save/load game)
5. Use error handling for invalid commands
6. Format output with f-strings for better display

EXAMPLE GAME STRUCTURE:
Locations:
{
    'forest': {
        'description': 'You are in a dark forest...',
        'exits': {'north': 'cave', 'east': 'village'},
        'items': ['sword', 'potion']
    }
}

Player:
{
    'location': 'forest',
    'inventory': [],
    'health': 100
}

Commands:
- go <direction>: Move to another location
- take <item>: Pick up an item
- look: Describe current location
- inventory: Show items carried
- save/load: Save or load game state

HINTS:
1. Use nested dictionaries for game world structure
2. Create functions for each command
3. Use a main game loop with input()
4. Store game state in JSON file for save/load
5. Use sets for valid commands
6. Format strings for nice output

EXTENSION:
Add combat system with enemies.
Implement item usage (healing potions, keys).
Add puzzles that require specific items.
Create a quest/objective system.
Add character stats (strength, magic, etc.).
"""

# Write your solution here
