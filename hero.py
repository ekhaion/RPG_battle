import random
from weapon import Weapon
from characteristic import Characteristic


class Hero:
    def __init__(self, name: str = None, health: int = None,
                 strength: int = 20, defense: int = 20, weapon: Weapon = ("Sword", 7)):
        self.name = name or self.generate_random_name()
        # declaration value or random value
        self.health = health or Characteristic().health
        self.strength = strength or Characteristic().strength
        self.defense = defense or Characteristic().defense
        # set weapon or random weapon for hero
        self.weapon = weapon or Weapon()

    @staticmethod
    def generate_random_name():
        hero_names = ["Warrior", "Mage", "Rogue", "Paladin", "Ranger", "Valkyrie"]
        return random.choice(hero_names)

    def __str__(self):
        return f"{self.name} (🖤: {self.health}, 🦾: {self.strength}, 🛡: {self.defense}, ⚔: {self.weapon}) "
