# Exercise 45: RPG Character System (OOP Project)
# Difficulty: Intermediate
# Concepts: Classes, Inheritance, Methods, JSON, File I/O

"""
PROBLEM:
Create a text-based RPG character system with:
1. Base Character class with: name, health, max_health, level, experience
2. Warrior class (high health, physical attacks)
3. Mage class (lower health, magic attacks)
4. Methods: attack, take_damage, heal, level_up, get_stats
5. Save/load characters to/from JSON file

Character features:
- Warriors have higher base health and strength
- Mages have lower health but higher magic power
- Characters gain experience and level up
- Character state can be saved and restored

EXAMPLE:
warrior = Warrior("Conan")
warrior.attack()  # "Conan swings a mighty sword!"
warrior.take_damage(20)  # Health reduced
warrior.get_stats()  # Display all stats

Save to JSON and reload later

HINTS:
1. Create base Character class first
2. Warrior and Mage inherit from Character
3. Override attack() method in each subclass
4. Use JSON to save character data (convert to dict first)
5. Create class method or function to load from JSON

EXTENSION:
Add an inventory system where characters can carry items (weapons, potions).
Add a battle system where two characters can fight each other.
"""

# Write your solution here
