# Exercise 30: Mini Text Adventure Game - SOLUTION
# Difficulty: Intermediate-
# Concepts: Dictionaries, Functions, Control flow, User input, Game logic

# SOLUTION
import json
import os

class TextAdventureGame:
    """A simple text-based adventure game."""

    def __init__(self):
        self.world = self._create_world()
        self.player = {
            'location': 'forest',
            'inventory': [],
            'health': 100,
            'max_health': 100
        }
        self.game_over = False

    def _create_world(self):
        """Create the game world with locations and items."""
        return {
            'forest': {
                'name': 'Dark Forest',
                'description': 'You are in a dark, mysterious forest. Trees tower above you.',
                'exits': {'north': 'cave', 'east': 'village', 'south': 'river'},
                'items': ['stick', 'apple']
            },
            'cave': {
                'name': 'Mysterious Cave',
                'description': 'A damp cave with ancient writings on the walls.',
                'exits': {'south': 'forest', 'east': 'mountain'},
                'items': ['torch', 'gold coin']
            },
            'village': {
                'name': 'Peaceful Village',
                'description': 'A small village with friendly people and wooden houses.',
                'exits': {'west': 'forest', 'north': 'castle'},
                'items': ['bread', 'water']
            },
            'castle': {
                'name': 'Ancient Castle',
                'description': 'An imposing castle with tall stone walls.',
                'exits': {'south': 'village'},
                'items': ['sword', 'shield', 'treasure']
            },
            'mountain': {
                'name': 'Mountain Peak',
                'description': 'You stand at the peak of a tall mountain. The view is breathtaking.',
                'exits': {'west': 'cave'},
                'items': ['crystal']
            },
            'river': {
                'name': 'Flowing River',
                'description': 'A clear river flows peacefully here.',
                'exits': {'north': 'forest'},
                'items': ['fish', 'potion']
            }
        }

    def display_location(self):
        """Display current location information."""
        location = self.world[self.player['location']]

        print("\n" + "=" * 60)
        print(f"LOCATION: {location['name']}")
        print("=" * 60)
        print(location['description'])

        # Show exits
        if location['exits']:
            exits = ", ".join(location['exits'].keys())
            print(f"\nExits: {exits}")

        # Show items
        if location['items']:
            items = ", ".join(location['items'])
            print(f"Items here: {items}")

        print("\n" + "-" * 60)

    def display_status(self):
        """Display player status."""
        print(f"Health: {self.player['health']}/{self.player['max_health']}")
        print(f"Location: {self.world[self.player['location']]['name']}")

    def command_look(self):
        """Look around the current location."""
        self.display_location()

    def command_go(self, direction):
        """Move to another location."""
        if not direction:
            return "Go where? Specify a direction (north, south, east, west)"

        current_location = self.world[self.player['location']]

        if direction in current_location['exits']:
            self.player['location'] = current_location['exits'][direction]
            print(f"\nYou travel {direction}...")
            self.display_location()
            return ""
        else:
            return f"You cannot go {direction} from here."

    def command_take(self, item):
        """Pick up an item."""
        if not item:
            return "Take what? Specify an item."

        current_location = self.world[self.player['location']]

        if item in current_location['items']:
            current_location['items'].remove(item)
            self.player['inventory'].append(item)
            return f"You take the {item}."
        else:
            return f"There is no {item} here."

    def command_inventory(self):
        """Show player inventory."""
        if not self.player['inventory']:
            return "Your inventory is empty."

        print("\n" + "=" * 60)
        print("INVENTORY")
        print("=" * 60)
        for i, item in enumerate(self.player['inventory'], 1):
            print(f"{i}. {item}")
        print("=" * 60)
        return ""

    def command_drop(self, item):
        """Drop an item from inventory."""
        if not item:
            return "Drop what? Specify an item."

        if item in self.player['inventory']:
            self.player['inventory'].remove(item)
            current_location = self.world[self.player['location']]
            current_location['items'].append(item)
            return f"You drop the {item}."
        else:
            return f"You don't have a {item}."

    def command_use(self, item):
        """Use an item from inventory."""
        if not item:
            return "Use what? Specify an item."

        if item not in self.player['inventory']:
            return f"You don't have a {item}."

        # Item effects
        if item == 'potion':
            heal_amount = 30
            self.player['health'] = min(self.player['max_health'],
                                       self.player['health'] + heal_amount)
            self.player['inventory'].remove('potion')
            return f"You drink the potion and restore {heal_amount} health!"

        elif item in ['apple', 'bread']:
            heal_amount = 10
            self.player['health'] = min(self.player['max_health'],
                                       self.player['health'] + heal_amount)
            self.player['inventory'].remove(item)
            return f"You eat the {item} and restore {heal_amount} health!"

        else:
            return f"You can't use the {item} right now."

    def command_help(self):
        """Display available commands."""
        print("\n" + "=" * 60)
        print("AVAILABLE COMMANDS")
        print("=" * 60)
        print("look              - Look around current location")
        print("go <direction>    - Move in a direction (north, south, east, west)")
        print("take <item>       - Pick up an item")
        print("drop <item>       - Drop an item from inventory")
        print("inventory (inv)   - Show your inventory")
        print("use <item>        - Use an item from inventory")
        print("status            - Show your status")
        print("save              - Save the game")
        print("load              - Load a saved game")
        print("help              - Show this help message")
        print("quit              - Exit the game")
        print("=" * 60)
        return ""

    def command_save(self):
        """Save the game state."""
        save_data = {
            'player': self.player,
            'world': self.world
        }

        # Ensure directory exists
        if not os.path.exists('temp_files'):
            os.makedirs('temp_files')

        try:
            with open('temp_files/savegame.json', 'w') as f:
                json.dump(save_data, f, indent=2)
            return "Game saved successfully!"
        except Exception as e:
            return f"Error saving game: {e}"

    def command_load(self):
        """Load a saved game."""
        try:
            with open('temp_files/savegame.json', 'r') as f:
                save_data = json.load(f)

            self.player = save_data['player']
            self.world = save_data['world']
            return "Game loaded successfully!"
        except FileNotFoundError:
            return "No saved game found."
        except Exception as e:
            return f"Error loading game: {e}"

    def process_command(self, command_str):
        """Process a user command."""
        parts = command_str.lower().strip().split(maxsplit=1)

        if not parts:
            return ""

        command = parts[0]
        argument = parts[1] if len(parts) > 1 else None

        # Command routing
        if command in ['quit', 'exit', 'q']:
            self.game_over = True
            return "Thanks for playing!"

        elif command in ['look', 'l']:
            return self.command_look()

        elif command in ['go', 'move', 'walk']:
            return self.command_go(argument)

        elif command == 'take':
            return self.command_take(argument)

        elif command == 'drop':
            return self.command_drop(argument)

        elif command in ['inventory', 'inv', 'i']:
            return self.command_inventory()

        elif command == 'use':
            return self.command_use(argument)

        elif command in ['status', 'stats']:
            self.display_status()
            return ""

        elif command == 'save':
            return self.command_save()

        elif command == 'load':
            return self.command_load()

        elif command in ['help', 'h', '?']:
            return self.command_help()

        else:
            return f"Unknown command: '{command}'. Type 'help' for available commands."

    def play(self):
        """Main game loop."""
        print("\n" + "=" * 60)
        print("WELCOME TO THE TEXT ADVENTURE GAME!")
        print("=" * 60)
        print("\nType 'help' for a list of commands.")
        print("Your goal: Explore the world and find the treasure!")

        self.display_location()

        while not self.game_over:
            try:
                command = input("\n> ").strip()

                if not command:
                    continue

                result = self.process_command(command)

                if result:
                    print(result)

            except KeyboardInterrupt:
                print("\n\nGame interrupted. Type 'quit' to exit properly.")
            except Exception as e:
                print(f"Error: {e}")


# Demonstration mode (non-interactive)
def demo_game():
    """Demonstrate the game with pre-scripted commands."""
    print("TEXT ADVENTURE GAME - DEMO MODE")
    print("=" * 60)
    print("Running pre-scripted commands to demonstrate functionality\n")

    game = TextAdventureGame()

    # Simulate commands
    commands = [
        "look",
        "take apple",
        "inventory",
        "go north",
        "look",
        "take torch",
        "go east",
        "look",
        "use apple",
        "status",
        "go west",
        "go south",
        "inventory",
        "save",
    ]

    for cmd in commands:
        print(f"\n{'>'*3} {cmd}")
        print("-" * 60)
        result = game.process_command(cmd)
        if result:
            print(result)

        # Prevent game over in demo
        game.game_over = False

    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nTo play interactively, uncomment the line at the bottom")
    print("and run: game = TextAdventureGame() then game.play()")


# Run demo
demo_game()

"""
EXPLANATION:
1. Game uses nested dictionaries for world structure
2. Each location has description, exits, and items
3. Player state stored in dictionary (location, inventory, health)
4. Command processing splits input and routes to appropriate method
5. JSON used for save/load game state
6. Error handling for invalid commands and file operations
7. String formatting for nice output display

Key Concepts:
- Dictionary-based data structure for game world
- Command parsing with string split
- State management with player and world dictionaries
- File I/O with JSON for persistence
- Error handling for robustness
- Game loop pattern with flag
- Method organization in a class
"""

# Extension solution features
print("\n--- EXTENSION FEATURES ---")
print("""
Additional features that could be added:

1. COMBAT SYSTEM:
   - Add enemies to locations
   - Implement attack/defend commands
   - Use weapon items for bonus damage

2. QUEST SYSTEM:
   - Track objectives
   - Give rewards for completion
   - Create quest chains

3. PUZZLES:
   - Locked doors requiring keys
   - Riddles to solve
   - Item combinations

4. CHARACTER STATS:
   - Strength, Magic, Defense
   - Level up system
   - Skill progression

5. ADVANCED INVENTORY:
   - Weight limits
   - Item categories
   - Equipment slots

6. NPC INTERACTIONS:
   - Talk to characters
   - Trade items
   - Get quests from NPCs

7. TIME SYSTEM:
   - Day/night cycle
   - Timed events
   - Action costs

8. MULTIPLE ENDINGS:
   - Based on choices
   - Tracked decisions
   - Replay value
""")

# Example of extended game with combat
print("\n--- COMBAT SYSTEM EXAMPLE ---")

class CombatAdventureGame(TextAdventureGame):
    """Extended game with combat system."""

    def _create_world(self):
        """Create world with enemies."""
        world = super()._create_world()

        # Add enemies to some locations
        world['forest']['enemy'] = {
            'name': 'Wolf',
            'health': 30,
            'damage': 10
        }

        world['cave']['enemy'] = {
            'name': 'Goblin',
            'health': 40,
            'damage': 15
        }

        return world

    def command_attack(self):
        """Attack an enemy in current location."""
        location = self.world[self.player['location']]

        if 'enemy' not in location:
            return "There is nothing to attack here."

        enemy = location['enemy']

        # Player attacks
        weapon_bonus = 10 if 'sword' in self.player['inventory'] else 0
        player_damage = 15 + weapon_bonus

        enemy['health'] -= player_damage
        result = f"You attack the {enemy['name']} for {player_damage} damage!"

        # Check if enemy defeated
        if enemy['health'] <= 0:
            result += f"\nYou defeated the {enemy['name']}!"
            del location['enemy']
            return result

        # Enemy counter-attacks
        self.player['health'] -= enemy['damage']
        result += f"\nThe {enemy['name']} attacks you for {enemy['damage']} damage!"

        # Check if player defeated
        if self.player['health'] <= 0:
            result += "\n\nYou have been defeated! Game Over."
            self.game_over = True

        return result

    def display_location(self):
        """Display location with enemy info."""
        super().display_location()

        location = self.world[self.player['location']]
        if 'enemy' in location:
            enemy = location['enemy']
            print(f"\n⚔️  ENEMY: {enemy['name']} (Health: {enemy['health']})")

# Show combat example
print("\nCombat system adds:")
print("- Enemies in locations")
print("- Attack command")
print("- Health tracking for enemies")
print("- Weapon bonuses from inventory")
print("- Game over on defeat")

print("\n" + "=" * 60)
print("Adventure game complete! Files saved in temp_files/")
print("=" * 60)
