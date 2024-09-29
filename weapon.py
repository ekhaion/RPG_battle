import random
from random import randint
from typing import Tuple


class Weapon:
    def __init__(self, name: str =None, damage: int =None):
        self.enchanted = self.is_enchanted_weapon()
        self.random_weapon = self.generate_random_weapon(self.enchanted)
        self.name = name or self.random_weapon[0]
        self.damage = damage or self.random_weapon[1]

    @staticmethod
    def generate_random_weapon(enchanted) -> Tuple:
        weapons = [
            ("Sword", 7),
            ("Mace", 8),
            ("Spear", 6),
            ("Bow", 6),
            ("Crossbow", 8),
            ("Dagger", 4),
            ("Staff", 6),
            ("Spells", 9),]
        random_weapon = random.choice(weapons)
        # if enchanted add random damages
        if enchanted:
            return random_weapon[0], random_weapon[1] + randint(1, random_weapon[1])
        return random_weapon

    @staticmethod
    def is_enchanted_weapon():
        return random.randint(1, 10) == 1

    def __str__(self):
        if self.enchanted:
            return f"{self.name} 'Enchanted' ({self.damage} damage)"
        return f"{self.name} ({self.damage} damage)"