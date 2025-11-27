# Exercise 45: RPG Character System (OOP Project) - SOLUTION
# Difficulty: Intermediate
# Concepts: Classes, Inheritance, Methods, JSON, File I/O

import json
import random

# SOLUTION
class Character:
    """Base character class."""

    def __init__(self, name, health=100, level=1):
        """
        Initialize character.

        Args:
            name: Character name
            health: Starting health
            level: Starting level
        """
        self.name = name
        self.max_health = health
        self.health = health
        self.level = level
        self.experience = 0
        self.exp_to_level = 100

    def take_damage(self, damage):
        """
        Take damage.

        Args:
            damage: Amount of damage to take

        Returns:
            bool: True if still alive
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0

        print(f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")

        if self.health == 0:
            print(f"{self.name} has been defeated!")
            return False
        return True

    def heal(self, amount):
        """
        Heal character.

        Args:
            amount: Amount to heal
        """
        old_health = self.health
        self.health = min(self.health + amount, self.max_health)
        healed = self.health - old_health
        print(f"{self.name} heals for {healed}! Health: {self.health}/{self.max_health}")

    def gain_experience(self, exp):
        """
        Gain experience and potentially level up.

        Args:
            exp: Experience points gained
        """
        self.experience += exp
        print(f"{self.name} gains {exp} experience!")

        while self.experience >= self.exp_to_level:
            self.level_up()

    def level_up(self):
        """Level up the character."""
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)

        # Increase max health
        health_increase = 20
        self.max_health += health_increase
        self.health = self.max_health

        print(f"\n{'='*40}")
        print(f"{self.name} LEVELED UP to level {self.level}!")
        print(f"Max health increased by {health_increase}!")
        print(f"{'='*40}\n")

    def get_stats(self):
        """Display character statistics."""
        print(f"\n{'='*40}")
        print(f"{self.name} - Level {self.level} {self.__class__.__name__}")
        print(f"{'='*40}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Experience: {self.experience}/{self.exp_to_level}")
        print(f"{'='*40}\n")

    def attack(self):
        """Base attack method (to be overridden)."""
        damage = 10 + (self.level * 2)
        print(f"{self.name} attacks for {damage} damage!")
        return damage

    def to_dict(self):
        """Convert character to dictionary for JSON serialization."""
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'health': self.health,
            'max_health': self.max_health,
            'level': self.level,
            'experience': self.experience,
            'exp_to_level': self.exp_to_level
        }

    def save_to_file(self, filename):
        """Save character to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        print(f"Saved {self.name} to {filename}")

class Warrior(Character):
    """Warrior class with high health and physical attacks."""

    def __init__(self, name):
        """Initialize warrior with higher health."""
        super().__init__(name, health=150, level=1)
        self.strength = 15

    def attack(self):
        """Warrior's physical attack."""
        damage = self.strength + (self.level * 3) + random.randint(5, 15)
        print(f"{self.name} swings a mighty sword for {damage} damage!")
        return damage

    def power_strike(self):
        """Special powerful attack."""
        damage = (self.strength + self.level * 3) * 2
        print(f"{self.name} uses POWER STRIKE for {damage} damage!")
        return damage

    def level_up(self):
        """Warrior gains extra strength on level up."""
        super().level_up()
        self.strength += 5
        print(f"Strength increased to {self.strength}!")

class Mage(Character):
    """Mage class with lower health but magic attacks."""

    def __init__(self, name):
        """Initialize mage with lower health but magic."""
        super().__init__(name, health=80, level=1)
        self.mana = 100
        self.max_mana = 100
        self.magic_power = 20

    def attack(self):
        """Mage's magic attack."""
        if self.mana < 10:
            print(f"{self.name} doesn't have enough mana!")
            return 0

        self.mana -= 10
        damage = self.magic_power + (self.level * 4) + random.randint(10, 20)
        print(f"{self.name} casts a spell for {damage} damage! (Mana: {self.mana}/{self.max_mana})")
        return damage

    def fireball(self):
        """Powerful spell attack."""
        if self.mana < 30:
            print(f"{self.name} doesn't have enough mana for Fireball!")
            return 0

        self.mana -= 30
        damage = (self.magic_power + self.level * 4) * 2
        print(f"{self.name} casts FIREBALL for {damage} damage! (Mana: {self.mana}/{self.max_mana})")
        return damage

    def restore_mana(self, amount=50):
        """Restore mana."""
        old_mana = self.mana
        self.mana = min(self.mana + amount, self.max_mana)
        restored = self.mana - old_mana
        print(f"{self.name} restores {restored} mana! (Mana: {self.mana}/{self.max_mana})")

    def level_up(self):
        """Mage gains extra magic power on level up."""
        super().level_up()
        self.magic_power += 5
        self.max_mana += 20
        self.mana = self.max_mana
        print(f"Magic power increased to {self.magic_power}!")
        print(f"Max mana increased to {self.max_mana}!")

    def to_dict(self):
        """Include mage-specific attributes."""
        data = super().to_dict()
        data.update({
            'mana': self.mana,
            'max_mana': self.max_mana,
            'magic_power': self.magic_power
        })
        return data

# Character loading function
def load_character(filename):
    """Load character from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)

    char_class = data['class']
    name = data['name']

    # Create appropriate character type
    if char_class == 'Warrior':
        char = Warrior(name)
    elif char_class == 'Mage':
        char = Mage(name)
    else:
        char = Character(name)

    # Restore attributes
    char.health = data['health']
    char.max_health = data['max_health']
    char.level = data['level']
    char.experience = data['experience']
    char.exp_to_level = data['exp_to_level']

    # Restore class-specific attributes
    if char_class == 'Mage' and 'mana' in data:
        char.mana = data['mana']
        char.max_mana = data['max_mana']
        char.magic_power = data['magic_power']

    print(f"Loaded {name} from {filename}")
    return char

# Test the character system
print("=== RPG Character System ===\n")

# Create characters
warrior = Warrior("Conan")
mage = Mage("Merlin")

# Display initial stats
warrior.get_stats()
mage.get_stats()

# Test combat
print("--- Combat Test ---")
warrior.attack()
warrior.power_strike()

mage.attack()
mage.fireball()
mage.restore_mana()

# Test damage and healing
print("\n--- Damage & Healing ---")
warrior.take_damage(30)
warrior.heal(20)

# Test leveling
print("\n--- Leveling Up ---")
warrior.gain_experience(100)
warrior.get_stats()

mage.gain_experience(150)
mage.get_stats()

# Save and load
print("\n--- Save & Load ---")
warrior.save_to_file("warrior_save.json")
mage.save_to_file("mage_save.json")

# Simulate game restart - load characters
print("\nLoading saved characters...")
loaded_warrior = load_character("warrior_save.json")
loaded_mage = load_character("mage_save.json")

loaded_warrior.get_stats()
loaded_mage.get_stats()

"""
EXPLANATION:
1. Character is the base class with common attributes and methods
2. Warrior and Mage inherit from Character and override attack()
3. Each subclass has unique abilities (power_strike, fireball)
4. level_up() is overridden to add class-specific bonuses
5. to_dict() converts objects to dictionaries for JSON serialization
6. load_character() recreates objects from JSON data
7. Polymorphism allows treating different classes uniformly

Key Concepts:
- Inheritance creates specialized versions of base class
- Method overriding customizes behavior for subclasses
- super() calls parent class methods
- JSON requires converting objects to serializable types
- Class design separates concerns (base vs specialized behavior)
"""

# Extension solution
print("\n--- EXTENSION SOLUTION ---")

class CharacterWithInventory(Character):
    """Character with inventory system."""

    def __init__(self, name, health=100, level=1):
        """Initialize with inventory."""
        super().__init__(name, health, level)
        self.inventory = []
        self.equipped_weapon = None

    def add_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"{self.name} picked up {item['name']}")

    def equip_weapon(self, weapon_name):
        """Equip a weapon from inventory."""
        for item in self.inventory:
            if item['name'] == weapon_name and item['type'] == 'weapon':
                self.equipped_weapon = item
                print(f"{self.name} equipped {weapon_name}!")
                return True
        print(f"Weapon {weapon_name} not found!")
        return False

    def show_inventory(self):
        """Display inventory."""
        print(f"\n{self.name}'s Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            for item in self.inventory:
                equipped = " (equipped)" if item == self.equipped_weapon else ""
                print(f"  - {item['name']} ({item['type']}){equipped}")

# Battle system
def battle(char1, char2):
    """Simple battle system."""
    print(f"\n{'='*50}")
    print(f"BATTLE: {char1.name} vs {char2.name}")
    print(f"{'='*50}\n")

    turn = 1
    while char1.health > 0 and char2.health > 0:
        print(f"--- Turn {turn} ---")

        # char1 attacks
        damage = char1.attack()
        if not char2.take_damage(damage):
            print(f"\n{char1.name} wins!")
            char1.gain_experience(50)
            break

        # char2 attacks
        damage = char2.attack()
        if not char1.take_damage(damage):
            print(f"\n{char2.name} wins!")
            char2.gain_experience(50)
            break

        turn += 1
        print()

# Test enhanced features
hero = CharacterWithInventory("Hero", 100, 1)
hero.add_item({'name': 'Iron Sword', 'type': 'weapon', 'damage': 15})
hero.add_item({'name': 'Health Potion', 'type': 'consumable', 'heal': 50})
hero.show_inventory()
hero.equip_weapon('Iron Sword')
hero.show_inventory()

# Test battle system
print("\n\nBattle System Test:")
warrior1 = Warrior("Aragorn")
warrior2 = Warrior("Boromir")
battle(warrior1, warrior2)
