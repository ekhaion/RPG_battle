import random
from characteristic import Characteristic


class Monster:
    def __init__(self, name: str = None, health: int = None,
                 strength: int = None, defense: int = None):
        self.monster = self.generate_random_monster()
        # set name with the first index of Tuple
        self.name = name or self.monster[0]

        # Base stats with random variation from second index of Tuple
        self.health = health or int(Characteristic().health * self.monster[1])
        self.strength = strength or int(Characteristic().strength * self.monster[1])
        self.defense = defense or int(Characteristic().defense * self.monster[1])

    @staticmethod
    def generate_random_monster():
        monster_names = [
            ("Goblin", 0.8),
            ("Ogre", 1.5),
            ("Troll", 1.8),
            ("Dragon", 2.0),
            ("Wolf", 1.0),
            ("Bear", 1.2),
            ("Snake", 0.5)
        ]
        random_monster = random.choice(monster_names)
        return random_monster

    def __str__(self):
        return f"{self.name} (🖤: {self.health}, 🦾: {self.strength}, 🛡: {self.defense})"
